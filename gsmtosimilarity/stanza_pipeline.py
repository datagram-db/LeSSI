import stanza

from crawltogsm.write_to_log import write_to_log


# from crawltogsm.write_to_log import write_to_log


class StanzaService:
    _instance = None

    nlp_token = None
    nlp = None

    def __init__(self):
        if self.nlp is None:
            write_to_log(None, "Initialising Stanza Pipeline...")
            self.nlp = stanza.Pipeline(lang='en')

        if self.nlp_token is None:
            write_to_log(None, "Initialising Stanza Tokenization...")
            self.nlp_token = stanza.Pipeline(lang='en', processors='tokenize')

    def __new__(cls):
        if cls._instance is None:
            write_to_log(None, "Initialising Stanza...")
            stanza.download('en')
            cls._instance = super(StanzaService, cls).__new__(cls)

        return cls._instance
