from whoosh import index
from whoosh import qparser
from .create_whoosh_index import INDEX_DIR


def exhaustive_search(search_string):
    title_search_result = _search_query(search_string, search_on='title')
    if title_search_result:
        return title_search_result

    content_search_result = _search_query(search_string, search_on='content')
    if content_search_result:
        return content_search_result
    return {}


def _search_query(search_string, search_on):
    search_index = index.open_dir(INDEX_DIR)
    searcher = search_index.searcher()
    query_parser = qparser.QueryParser(search_on, schema=search_index.schema)
    query_parser.add_plugin(qparser.PrefixPlugin())
    query_parser.add_plugin(qparser.FuzzyTermPlugin())
    results = searcher.search(query_parser.parse(search_string), limit=1)
    return [dict(result) for result in results]
