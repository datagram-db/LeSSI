from collections import defaultdict
from enum import Enum

from logical_repr.Sentences import FVariable, FNot, FBinaryPredicate, FUnaryPredicate


class ExpandConstituents:
    def __init__(self, expander):
        self.expander = expander
        self.constituent_expansion_map = defaultdict(set)

    def expand_formula(self, formula):
        ### Defining the expansion of one single rule
        if formula is None or formula in self.constituent_expansion_map:
            return
        for expansion in self.expander(formula):
            self.constituent_expansion_map[formula].add(expansion)
            self.expand_formula(formula)
        if formula not in self.constituent_expansion_map:
            self.constituent_expansion_map[formula] = set()

    def getExpansionLeaves(self):
        return {x for x, y in self.constituent_expansion_map.items() if len(y) == 0}

# def get_formula_expansion(expander, formula):
#     ec = ExpandConstituents(expander)
#     ec.expand_formula(formula)
#     return ec.getExpansionLeaves()


class CasusHappening(Enum):
    EQUIVALENT = 0
    IMPLICATION = 1
    EXCLUSIVES = 2
    INDIFFERENT = 3
    NONE = 4

def transformCaseWhenOneArgIsNegated(orig:CasusHappening):
    d = {CasusHappening.NONE: CasusHappening.NONE,
     CasusHappening.INDIFFERENT: CasusHappening.INDIFFERENT,
    CasusHappening.EQUIVALENT: CasusHappening.EXCLUSIVES,
     CasusHappening.EXCLUSIVES: CasusHappening.EQUIVALENT}
    return d[orig]


def compare_variable(d, lhs, rhs, kb):
    cp = (lhs, rhs)
    if (cp not in d) and (lhs == rhs):
        d[cp] = CasusHappening.EQUIVALENT
    if cp in d:
        return d[cp]
    assert isinstance(lhs, FVariable)
    assert isinstance(rhs, FVariable)
    nameEQ = kb.name_eq(lhs.name, rhs.name)
    specEQ = kb.name_eq(lhs.specification, rhs.specification)
    copCompare = compare_variable(d, lhs.cop, rhs.cop, kb)
    val = CasusHappening.INDIFFERENT
    if (nameEQ == specEQ) and (specEQ == copCompare):
        return specEQ
    if nameEQ == CasusHappening.INDIFFERENT:
        nameAgainstSpec = kb.name_eq(lhs.name, rhs.specification)
        if nameAgainstSpec == CasusHappening.EQUIVALENT:
            val = CasusHappening.IMPLICATION
    elif nameEQ == CasusHappening.EQUIVALENT:
        if (specEQ == copCompare):
            val = specEQ
        elif (specEQ == CasusHappening.EQUIVALENT):
            val = copCompare
        else:
            val = specEQ
    elif nameEQ == CasusHappening.EXCLUSIVES:
        if (specEQ == copCompare) and (specEQ == CasusHappening.EQUIVALENT):
            val = CasusHappening.EXCLUSIVES
    # if (rhs.specification is None) and (lhs.specification is None):
    #     d[cp] = CasusHappening.INDIFFERENT
    # else:
    #     nameSpecEQ = kb.name_eq(lhs.name, rhs.specification)
    #     nameSpec2EQ = kb.name_eq(lhs.specification, rhs.specification)
    #
    #     raise ValueError("More refined comparison in ExpandConstituents::compare_variable: YET TO BE IMPLEMENTED!")
    d[cp] = val
    return d[cp]

def simplifyConstituents(constituentCollection):
    if isinstance(constituentCollection, CasusHappening):
        return constituentCollection
    elif CasusHappening.EXCLUSIVES in constituentCollection:
        return CasusHappening.EXCLUSIVES
    elif CasusHappening.EQUIVALENT in constituentCollection:
        return CasusHappening.EQUIVALENT
    elif CasusHappening.IMPLICATION in constituentCollection:
        return CasusHappening.IMPLICATION
    else:
        return CasusHappening.INDIFFERENT

def test_pairwise_sentence_similarity(d, x, y, store=True, kb=None):
    val = CasusHappening.NONE
    if y is None and x is None:
        val = CasusHappening.EQUIVALENT
    elif y is None:
        val = CasusHappening.IMPLICATION
    elif x is None:
        val = CasusHappening.INDIFFERENT
    elif (x == y):
        val = CasusHappening.EQUIVALENT
    elif (x == FNot(y)) or (y == FNot(x)):
        val = CasusHappening.EXCLUSIVES
    elif isinstance(x, FNot):
        val = transformCaseWhenOneArgIsNegated(test_pairwise_sentence_similarity(d, x.arg, y, False))
    elif isinstance(y, FNot):
        val = transformCaseWhenOneArgIsNegated(test_pairwise_sentence_similarity(d, x, y.arg, False))
    else:
        if (x.meta != y.meta):
            val = CasusHappening.INDIFFERENT
        else:
            assert isinstance(x,FBinaryPredicate) or isinstance(x, FUnaryPredicate)
            assert isinstance(y,FBinaryPredicate) or isinstance(y, FUnaryPredicate)
            xprop = set() if x.properties is None else x.properties
            yprop = set() if y.properties is None else y.properties
            keyCmp = defaultdict(set)
            keys = set(map(lambda z: z[0], xprop)).union(map(lambda z: z[0], yprop))
            dLHS = dict(xprop)
            dRHS = dict(yprop)
            for key in keys:
                if key in dLHS and key in dRHS:
                    for xx in dLHS:
                        for yy in dRHS:
                            keyCmp[key].add(test_pairwise_sentence_similarity(d, xx, yy, store, kb))
                elif key in dLHS:
                    keyCmp[key].add(CasusHappening.INDIFFERENT)
                else:
                    keyCmp[key].add(CasusHappening.IMPLICATION)
            keyCmpElements = CasusHappening.EQUIVALENT
            if len(keyCmp)>0:
                keyCmpElements = simplifyConstituents({simplifyConstituents(keyCmp[key]) for key in keyCmp })
            if isinstance(x,FBinaryPredicate) and isinstance(y,FBinaryPredicate):
                if (x.rel != y.rel):
                    val = CasusHappening.INDIFFERENT
                else:
                    srcCmp = compare_variable(d, x.src, y.src, kb)
                    dstCmp = compare_variable(d, x.dst, y.dst, kb)
                    if (srcCmp == CasusHappening.EXCLUSIVES) and (dstCmp == CasusHappening.EXCLUSIVES):
                        val = CasusHappening.INDIFFERENT
                    elif (srcCmp == CasusHappening.EXCLUSIVES) and (dstCmp != CasusHappening.INDIFFERENT):
                        val = CasusHappening.EXCLUSIVES
                    elif (dstCmp == CasusHappening.EXCLUSIVES) and (srcCmp != CasusHappening.INDIFFERENT):
                        val = CasusHappening.EXCLUSIVES
                    elif srcCmp == CasusHappening.EQUIVALENT:
                        val = dstCmp
                    elif dstCmp == CasusHappening.EQUIVALENT:
                        val = srcCmp
                    else:
                        val = simplifyConstituents({srcCmp, dstCmp})
            elif isinstance(y,FUnaryPredicate) and isinstance(x, FUnaryPredicate):
                if (x.rel != y.rel):
                    val = CasusHappening.INDIFFERENT
                else:
                    val = compare_variable(d, x.arg, y.arg, kb)
            else:
                raise ValueError("Unexpected comparison between "+str(x)+" and"+str(y))
            if val != CasusHappening.INDIFFERENT:
                if val == CasusHappening.EQUIVALENT:
                    val = keyCmpElements
                elif val == CasusHappening.IMPLICATION:
                    if keyCmpElements != CasusHappening.EQUIVALENT:
                        val = keyCmpElements
                elif val == CasusHappening.EXCLUSIVES:
                    if keyCmpElements == CasusHappening.INDIFFERENT:
                        val = CasusHappening.INDIFFERENT
                    elif keyCmpElements == CasusHappening.EXCLUSIVES:
                        val = CasusHappening.INDIFFERENT
    if store:
        d[(x, y)] = val
    return val

class ExpandConstituents:
    def __init__(self, expander, list_of_rules):
        print("Setting up the rule expander...")
        self.set_of_rules = list(list_of_rules)
        self.expander = expander
        #Expanding the constituents
        self.expander
        if not all(map(lambda x: isinstance(x, FBinaryPredicate) or isinstance(x, FUnaryPredicate), self.set_of_rules)):
            raise ValueError("Error: all the rules within the set of rules must represent Predicates to be assessed, be them unary or binary")
        self.expansion_dictionary = dict()
        for rule in self.set_of_rules:
            s = set(self.expander(rule))
            if len(s) == 0:
                s.add(rule)
            self.expansion_dictionary[rule] = s
        with open("/home/giacomo/dump.json", "w") as f:
            from gsmtosimilarity.graph_similarity import EnhancedJSONEncoder
            import json
            json.dump({str(k):[str(x) for x in v] for k,v in self.expansion_dictionary.items()}, f, cls=EnhancedJSONEncoder, indent=4)
            exit(1)
        self.result_cache = dict()
        self.constituents = set()
        for y in self.expansion_dictionary.values():
            self.constituents = self.constituents.union(set(y))
        self.outcome_implication_dictionary = {(x,y):CasusHappening.NONE for x in self.constituents for y in self.constituents}
        for x in self.constituents:
            for y in self.constituents:
                test_pairwise_sentence_similarity(self.outcome_implication_dictionary, x, y, True, self.expander.g)

    def determine(self, i:int, j:int):
        assert i<len(self.set_of_rules)
        assert j<len(self.set_of_rules)
        if (i,j) in self.result_cache:
            return self.result_cache[(i,j)]
        from logical_repr.sentence_expansion import PairwiseCases
        val = PairwiseCases.NonImplying
        expansionLeft = self.expansion_dictionary[self.set_of_rules[i]]
        y = self.set_of_rules[j]
        # expansionRight = self.expansion_dictionary[self.set_of_rules[j]]
        result = set()
        for x in expansionLeft:
            #for y in expansionRight:
                assert (x,y) in self.outcome_implication_dictionary
                tmp = self.outcome_implication_dictionary[(x,y)]
                if tmp == CasusHappening.EXCLUSIVES:
                    val = PairwiseCases.MutuallyExclusive
                    break
                else:
                    result.add(tmp)
            # if val == PairwiseCases.MutuallyExclusive:
            #     break
        if val != PairwiseCases.MutuallyExclusive:
            if CasusHappening.EQUIVALENT in result:
                val = PairwiseCases.Equivalent
            elif CasusHappening.IMPLICATION in result:
                val = PairwiseCases.Implying
            else:
                val = PairwiseCases.NonImplying
        self.result_cache[(i, j)] = val
        return val










