from whoosh import index
from whoosh import qparser
from .create_whoosh_index import INDEX_DIR


def exhaustive_search(search_string):
    for tail_index in range(len(search_string), 0, -1):
        search_result = _search_query(search_string[:tail_index] + '*')
        if search_result:
            return search_result
    return []


def _search_query(search_string):
    search_index = index.open_dir(INDEX_DIR)
    searcher = search_index.searcher()
    query_parser = qparser.QueryParser("content", schema=search_index.schema)
    query_parser.add_plugin(qparser.PrefixPlugin())
    query_parser.add_plugin(qparser.FuzzyTermPlugin())
    results = searcher.search(query_parser.parse(search_string), limit=10)
    return [dict(result) for result in results]
