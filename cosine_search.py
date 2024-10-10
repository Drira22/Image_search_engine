import numpy as np
from elasticsearch import Elasticsearch

# Elasticsearch client connection
esclient = Elasticsearch("http://localhost:9200")
index_name = "image_features"

def search_similar_images(feature_vector, top_n=10):
    # Construct the search query for cosine similarity
    query = {
        "size": top_n,
        "query": {
            "script_score": {
                "query": {
                    "match_all": {}
                },
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'feature_vector') + 1.0",
                    "params": {
                        "query_vector": feature_vector.tolist()
                    }
                }
            }
        }
    }
    
    response = esclient.search(index=index_name, body=query)
    similar_images = []

    for hit in response['hits']['hits']:
        similar_images.append({
            'image_id': hit['_source']['image_id'],
            'image_path': f"/data/images/{hit['_source']['image_id']}.jpg"  
        })
    
    return similar_images
