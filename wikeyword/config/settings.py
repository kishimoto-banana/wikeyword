import os

WIKI_DICTIONARY_PATH = os.environ.get("WIKI_DICTIONARY_PATH", "/app/models/jawiki_dic.pkl")
WIKI_MENTION_DB_PATH = os.environ.get(
    "WIKI_MENTION_DB_PATH", "/app/models/jawiki_mention.pkl"
)
