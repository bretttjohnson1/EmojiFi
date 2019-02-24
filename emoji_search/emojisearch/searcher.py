from whoosh import index
from whoosh import qparser
from .create_whoosh_index import INDEX_DIR
from .create_whoosh_index import INDEX_DIR_FALLBACK
from emojisearch.util.word_transform import lematize_words
from emojisearch.util.word_transform import synonyms
from emojisearch.util.cleaning import cleaned_of_punctuation
from collections import defaultdict


def search(word):
    freqs = defaultdict(int)
    word = cleaned_of_punctuation(word)
    word = lematize_words([word])[0]

    for synonym in synonyms(word):
        results = _exhaustive_search(synonym)
        for result in results:
            freqs[result['emoji']] += 1 if synonym == word else 1

    return [
        emoji
        for emoji, score in sorted(
            freqs.items(),
            key=lambda x: (x[1], len(x[0]), x[0]),
            reverse=True
        )
    ]


def _exhaustive_search(search_string):
    search_results = _search_query(search_string, INDEX_DIR)
    if search_results:
        return search_results

    search_results = _search_query(search_string, INDEX_DIR_FALLBACK)
    if search_results:
        return search_results
    return {}


def _search_query(search_string, index_dir):
    search_index = index.open_dir(index_dir)
    searcher = search_index.searcher()
    query_parser = qparser.QueryParser('content', schema=search_index.schema)
    query_parser.add_plugin(qparser.PrefixPlugin())
    query_parser.add_plugin(qparser.FuzzyTermPlugin())
    results = searcher.search(query_parser.parse(search_string), limit=20)
    return [dict(result) for result in results]
