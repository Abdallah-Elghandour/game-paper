from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# mappings = {
#         "properties": {
#             "name": {"type": "text", "analyzer": "english"},
#             "win": {"type": "integer"},
#             "playing_counter": {"type": "integer"},
#     }
# }
# es.indices.create(index="players", mappings=mappings)