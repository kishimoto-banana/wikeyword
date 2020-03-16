from typing import List

import MeCab


class MecabMorphologicalAnalyzer:
    def __init__(
        self,
        dic_path: str = "/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd",
    ):
        self.mecab = MeCab.Tagger(f"-d {dic_path}")
        self.mecab.parse("")

    def parse(self, text: str) -> List[str]:
        result = self.mecab.parse(text)
        words = []
        for x in result.split("\n"):
            items = x.split("\t")
            if len(items) == 1:
                continue
            words.append(items[0])
        return words
