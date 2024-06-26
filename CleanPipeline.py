import json
import os.path
import sys

import numpy as np
import stanza
import yaml

from crawltogsm.LegacyPipeline import LegacyPipeline
from crawltogsm.generate_gsm_cypher_db import load_sentences, stanford_nlp_to_gsm, multi_named_entity_recognition
# from crawltogsm.write_to_log import write_to_log
from gsmtosimilarity.conceptnet.ConceptNet5 import ConceptNetService
from gsmtosimilarity.database.FuzzyStringMatchDatabase import FuzzyStringMatchDatabase
from gsmtosimilarity.geonames.GeoNames import GeoNamesService
from gsmtosimilarity.stanza_pipeline import StanzaService
from newscrawl.NewsCrawl import NewsCrawl

class CleanPipeline:
    _instance = None
    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance

    @classmethod
    def write_to_log(cls, text):
        CleanPipeline.instance().writeself_to_log(text)

    def writeself_to_log(self, text):
        if self.cfg is not None and 'web_dir' in self.cfg and self.cfg['web_dir'] is not None:
            with open(f"{self.cfg['web_dir']}/log.txt", 'w') as f:
                f.write(f"{text}")
                f.close()
        else:
            print(text)

    def init(self, conf):
        try:
            with open(conf) as f:
                self.cfg = yaml.load(f, Loader=yaml.FullLoader)
        except FileNotFoundError:
            raise Exception("Error: missing configuration file")
        if 'should_generate_final_stanza_db' not in self.cfg or not self.cfg['should_generate_final_stanza_db']:
            self.cfg['should_generate_final_stanza_db'] = True
        if 'should_run_datagram_db' not in self.cfg or not self.cfg['should_run_datagram_db']:
            self.cfg['should_run_datagram_db'] = self.cfg['similarity'].startswith('IDEAS24')
        if 'rewritten_dataset' not in self.cfg:
            self.cfg['rewritten_dataset'] = 'rewritten_dataset.txt'
        self.write_to_log("Starting the pipeline...")
        # TODO: your current configuration uses this as a server, right?
        #       Then, at initialization phase, we should move the time-consuming
        #       initialization at this point, so to reduce the warm-up time
        self.stanza_service = StanzaService()
        self.crawler = NewsCrawl()
        self.sentences = None
        # TODO: also add the initialization for the GeoNames resolution.
        #       Be warned! It takes a lot of primary memory
        # self.geo_names = None
        # Temp init locations
        # geo_names.no_file_init("Newcastle Upon Tyne", "n/t/uk/e/w")
        # geo_names.no_file_init("Tyne and Wear", "t/uk/e/w")
        # geo_names.no_file_init("London", "l/uk/e/w")
        # geo_names.no_file_init("Rome", "r/l/i/e/w")
        # TODO:
        # self.concept_net = None
        # self.FuzzyStringMatchDatabase.instance()

        if self.sentences is None:
            if 'hand_dataset' in self.cfg:
                self.cfg['rewritten_dataset'] = self.cfg['hand_dataset']+'_rewritten.txt'
        else:
            self.cfg['sentences'] = self.sentences
            self.cfg['rewritten_dataset'] = 'rewritten_user_input.txt'
        if 'gsm_sentences' not in self.cfg:
            self.cfg['gsm_sentences'] = self.cfg['rewritten_dataset'].replace("rewritten","")+'_gsm_sentences.txt'
        if 'crawl_to_gsm' not in self.cfg:
            self.cfg['crawl_to_gsm'] = {}
        if 'stanza_db' not in self.cfg['crawl_to_gsm']:
            self.cfg['crawl_to_gsm']['stanza_db'] = self.cfg['rewritten_dataset'].replace("rewritten","")+'_stanza_db.json'

        ## DB Initialisation
        (FuzzyStringMatchDatabase
         .instance()
         .init(self.cfg["db"]["db"], self.cfg["db"]["uname"], self.cfg["db"]["pw"], self.cfg["db"]["host"], self.cfg["db"]["port"]))
        FuzzyStringMatchDatabase.instance().create("conceptnet", self.cfg["conceptnet"])
        FuzzyStringMatchDatabase.instance().create("geonames", self.cfg["geonames"])
        # global geo_names
        self.geo_names = GeoNamesService()
        # global concept_net
        self.concept_net = ConceptNetService()
        self.legacy_pipeline = LegacyPipeline(self.cfg)
        self.db = []
        self.sentences = []
        if os.path.isfile(self.cfg['transitive_verbs']):
            with open(self.cfg['transitive_verbs'], "r") as f:
                self.transitive_verbs = set(map(lambda x: x.strip(), f.readlines()))
        else:
            self.transitive_verbs = set()
        if os.path.isfile(self.cfg['rejected_edge_types']):
            with open(self.cfg['rejected_edge_types'], 'r') as f:
                self.rejected_edges = set(map(lambda x: x.strip(), f.readlines()))
        else:
            self.rejected_edges = set()
        if os.path.isfile(self.cfg['non_verbs']):
            with open(self.cfg['non_verbs'], "r") as f:
                self.non_verbs = set(f.readlines())
        else:
            self.non_verbs = set()
        self.simplistic = self.cfg['rewriting_strategy'] == 'simplistic'
        return self

    def getSentences(self):
        # if "should_generate_final_stanza_db" in self.cfg and self.cfg["should_generate_final_stanza_db"]:
        if 'sentences' in self.cfg and len(self.cfg['sentences']) > 0:
            self.sentences = self.cfg['sentences']
            with open("automated_dataset.txt", "w") as f:
                f.writelines(self.sentences)
            self.cfg['hand_dataset'] = "automated_dataset.txt"
        else:
            load_sentences(self.legacy_pipeline, self.sentences)
        return self.sentences

    def run(self):
        import json
        self.write_to_log("Starting pipeline...")
        sentences = self.getSentences()
        f = self.getSimilarityFunction()
        result = None
        if self.cfg['similarity'].startswith('IDEAS24'):
            result = self.transformSentences(sentences)
        else:
            result = sentences

        M = []
        for x in result:
            ls = []
            for y in result:
                ls.append(f(x, y))
            M.append(ls)
        M = np.array(M)
        return json.dumps({"similarity_matrix": M.tolist(), "sentences": sentences})

    def apply_graph_grammar(self, gsm_dbs):
        from gsmtosimilarity.graph_similarity import read_graph_from_file
        directory = self.legacy_pipeline.graph_grammars_with_datagramdb(gsm_sentences=gsm_dbs)
        graphs = []
        import os
        for x in os.walk(directory):
            graphs = [None for _ in range(len(x[1]))]
            for result_folder in x[1]:
                resultFile = os.path.join(x[0], result_folder, "result.json")
                graphs[int(result_folder)] = read_graph_from_file(resultFile)
            break  # // Skipping the remaining subfolder
        return graphs

    def doGraphOperations(self, graphs, stanza_db):
        # TODO: find a more explicative name
        from gsmtosimilarity.graph_similarity import toInternalGraph
        return [toInternalGraph(graph, stanza_db, self.rejected_edges, self.non_verbs, True, self.simplistic) for graph in graphs]

    def getLogicalRepresentation(self, graph_e_n_list):
        from gsmtosimilarity.graph_similarity import create_sentence_obj
        # graph, edges, nodes = graph_e_n
        sentences = [create_sentence_obj(self.cfg, graph.edges, nodes, self.transitive_verbs, self.legacy_pipeline) for graph, edges, nodes in graph_e_n_list]
        return sentences

    def transformSentences(self, sentences):
        #Performing MultiNamedEntity Recognition

        stanza_db = {}
        if 'crawl_to_gsm' in self.cfg and\
            'stanza_db' in self.cfg['crawl_to_gsm'] and\
            os.path.isfile(self.cfg['crawl_to_gsm']['stanza_db']):
                with open(self.cfg['crawl_to_gsm']['stanza_db']) as f:
                    self.write_to_log("READING PREVIOUS COMPUTATION FOR: stanza_db")
                    stanza_db = json.load(f)
        else:
            stanza_db = multi_named_entity_recognition(0, None, self.legacy_pipeline, sentences)
        # with open("/home/giacomo/dumping_ground/stanzadb.json", "w") as f:
        #     print("STANZADB.json")
        #     import json
        #     json.dump(stanza_db, f)

        #Converting into the C++ format
        gsm_dbs = ""
        filepath = ""
        if 'gsm_sentences' in self.cfg and os.path.isfile(self.cfg['gsm_sentences']):
            filepath = os.path.abspath(self.cfg['gsm_sentences'])
            with open(filepath) as f:
                self.write_to_log("READING PREVIOUS COMPUTATION FOR: gsm_dbs")
                gsm_dbs = f.read()
        else:
            gsm_dbs, filepath = stanford_nlp_to_gsm(self, sentences) #some strings
        # with open("/home/giacomo/dumping_ground/gsm.txt", "w") as f:
        #     print("gsm.txt")
        #     import json
        #     f.write(gsm_dbs)

        #Running the Graph Grammar Rewriting

        gsmout_graphlist_file = self.cfg["hand_dataset"]+"_out_gsm.json"
        if os.path.isfile(gsmout_graphlist_file):
            with open(gsmout_graphlist_file) as f:
                self.write_to_log("READING PREVIOUS COMPUTATION FOR: graphs")
                graphs = json.load(f)
        else:
            graphs = self.apply_graph_grammar(filepath)
            with open(gsmout_graphlist_file, "w") as f:
                json.dump(graphs, f, indent=4)
        # with open("/home/giacomo/dumping_ground/after_graph_grammar.json", "w") as f:
        #     print("gsm.txt")
        #     import json
        #     json.dump(graphs, f)

        #Perform the internal rewriting
        graphs = self.doGraphOperations(graphs, stanza_db)
        # with open("/home/giacomo/dumping_ground/after_internal_rewriting.json", "w") as f:
        #     print("gsm.txt")
        #     import json
        #     from gsmtosimilarity.graph_similarity import EnhancedJSONEncoder
        #     json.dump([graph[0] for graph in graphs], f, cls=EnhancedJSONEncoder)

        # TODO If transform into graphs, then return directly graphs
        #      Otherwise, call getLogicalRepresentation and return those instead
        if "graphs" in self.cfg['similarity']:
            return [graph[0] for graph in graphs]
        else:
            return self.getLogicalRepresentation(graphs)

    def getSimilarityFunction(self):
        if self.cfg['similarity'] == 'IDEAS24':
            if 'graphs' in self.cfg['similarity']:
                return self.legacy_pipeline.graph_similarity
            else:
                return self.legacy_pipeline.bogus
            # TODO If transform into graphs, then return self.legacy_pipeline.graph_similarity
            #      Otherwise, return the new logical-based metric [TODO]

        else:
            return self.legacy_pipeline.sc.string_similarity



