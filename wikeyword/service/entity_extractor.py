import numpy as np
from wikipedia2vec.dictionary import Dictionary
from wikipedia2vec.mention_db import MentionDB

from wikeyword.config.settings import (WIKI_DICTIONARY_PATH,
                                       WIKI_MENTION_DB_PATH)


class EntityExtractor:
    def __init__(self):
        self.dic = Dictionary.load(WIKI_DICTIONARY_PATH)
        self.db = MentionDB.load(WIKI_MENTION_DB_PATH, self.dic)

    def extract(self, word: str) -> str:
        try:
            entities = self.db.query(word)
            if len(entities) == 1:
                return entities[0].entity.title
            else:
                max_idx = np.argmax([entity.commonness for entity in entities])
                entity = entities[max_idx].entity.title
                return entity
        except KeyError:
            return None
