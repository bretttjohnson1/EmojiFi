from whoosh import index
from whoosh import qparser
from .create_whoosh_index import INDEX_DIR
from .create_whoosh_index import INDEX_DIR_FALLBACK


def exhaustive_search(search_string):
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
