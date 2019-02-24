from whoosh import index
from whoosh import qparser
from .create_whoosh_index import INDEX_DIR
from .create_whoosh_index import INDEX_DIR_FALLBACK
from emojisearch.util.word_transform import lemmatize_words
from emojisearch.util.word_transform import synonyms
from emojisearch.util.cleaning import cleaned_of_punctuation
from collections import defaultdict


def search(word, scores=False):
    freqs = defaultdict(int)
    word = cleaned_of_punctuation(word)
    word = lemmatize_words([word.lower()])[0]

    for synonym in synonyms(word):
        name_results = _exhaustive_search(synonym, 'name')
        content_results = _exhaustive_search(synonym, 'content')

        for result, base_points in result_score_iterable(name_results):
            real_points = 3 * base_points if word == synonym else base_points
            freqs[result['emoji']] += real_points

        for result, base_points in result_score_iterable(content_results):
            freqs[result['emoji']] += base_points

    return [
        emoji if not scores else (emoji, score)
        for emoji, score in sorted(
            freqs.items(),
            key=lambda x: (x[1], x[0]),
            reverse=True
        )
    ]


def result_score_iterable(results, base=5):
    for i in range(len(results)):
        yield results[i], 5 / (i + 1)


def _exhaustive_search(search_string, search_field):
    search_results = _search_query(search_string, INDEX_DIR, search_field)
    if search_results:
        return search_results

    search_results = _search_query(search_string, INDEX_DIR_FALLBACK, search_field)
    if search_results:
        return search_results
    return {}


def _search_query(search_string, index_dir, search_field):
    search_index = index.open_dir(index_dir)
    searcher = search_index.searcher()
    query_parser = qparser.QueryParser(search_field, schema=search_index.schema)
    query_parser.add_plugin(qparser.PrefixPlugin())
    query_parser.add_plugin(qparser.FuzzyTermPlugin())
    results = searcher.search(query_parser.parse(search_string), limit=20)
    return [dict(result) for result in results]
