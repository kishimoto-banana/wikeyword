import re
from typing import List

import MeCab

NUMBER_SUFFIX_PATTERN = re.compile(
    r"(\d+)(丁目|万|万人|万円|世|世代|世紀|人|人目|人衆|代|代目|件|位|佐|作品|倍|億|億円|兆円|児|円|円玉|冠|分|分間|"
    "列目|割|勝|区|号|号機|周|周年|回|回戦|回目|回転|基|夜|失点|学期|安打|巻|年|年代|年前|年度|年後|年生|年目|年間|"
    "度|度目|強|得点|戦|才|打|打差|打席|打点|敗|日|日目|日間|星座|時|時間|曲|月|期|期生|期目|本|条|杯|枚|次|次元|"
    "歳|歳下|点|点差|番|番手|発|着|秒|種|種類|節|系|色|試合|話|軍|連休|連勝|連敗|連覇|週|週前|週目|週間|選手|部|階|階級|馬身)"
)


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
            if not NUMBER_SUFFIX_PATTERN.match(items[0]):
                words.append(items[0])
        return words
