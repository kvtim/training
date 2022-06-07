from flask import current_app


class ES_CRUD:
    @staticmethod
    def add_to_index(index, item):
        if not current_app.elasticsearch:
            return
        current_app.elasticsearch.index(index=index, doc_type=index, id=item['id'], body=item)

    @staticmethod
    def remove_from_index(index, item):
        if not current_app.elasticsearch:
            return
        current_app.elasticsearch.delete(index=index, doc_type=index, id=item[['id']])

    @staticmethod
    def query_index(index, query):
        if not current_app.elasticsearch:
            return []
        search = current_app.elasticsearch.search(index=index, doc_type=index, body={
            'query':
                {
                    'match':
                        {
                            'query': query,
                            'fields': ['*']
                        }
                }
        })

        return [hit['_source'] for hit in search['hits']['hits']]
    # ids = [int(hit['_id']) for hit in search['hits']['hits']]
    # return ids, search['hits']['total']
