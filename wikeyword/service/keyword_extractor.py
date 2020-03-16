from collections import OrderedDict
from typing import Dict

from wikeyword.service.entity_extractor import EntityExtractor
from wikeyword.service.morphological_analyzer import MecabMorphologicalAnalyzer


def extract(text: str) -> Dict[str, str]:

    parser = MecabMorphologicalAnalyzer()
    words = parser.parse(text)

    entity_extractor = EntityExtractor()
    word_entities = OrderedDict()
    for word in words:
        entity = entity_extractor.extract(word)
        if entity:
            word_entities[word] = entity

    return word_entities
