import os
import numpy as np
from elasticsearch import Elasticsearch

# path to features
input_dir = "/home/khalil/image_search_enginedata/features/"

# elasticsearch client connection 
esclient = Elasticsearch("http://localhost:9200")


index_name = "image_features"

# feature vectors index mapping
def create_index(es_client, index_name):
    mapping = {
        "mappings": {
            "properties": {
                "image_id": {"type": "keyword"},
                "image_name": {"type": "text"},
                "feature_vector": {"type": "dense_vector", "dims": 4096}
            }
        }
    }
    # index creation (with verification if it already exists)
    if not es_client.indices.exists(index=index_name):
        es_client.indices.create(index=index_name, body=mapping)
        print(f"Index '{index_name}' created.")
    else:
        print(f"Index '{index_name}' already exists.")

# document creation for index
def create_document(image_name, feature_vector):
    feature_vector = feature_vector.flatten() #flatten the vector w hothom fi liste wahda khater lezm 1D
    return {
        "_index": index_name,
        "_source": {
            "image_id": image_name.split('.')[0],  
            "image_name": image_name,
            "feature_vector": feature_vector.tolist()  #mel numpy nrodouha list bch najmou nhotouha json w nabaathouha ll elastic
        }
    }

def index_features(es_client, input_dir):
    for feature_file in os.listdir(input_dir):
        feature_path = os.path.join(input_dir, feature_file)
        try:
            feature_vector = np.load(feature_path) #loadi l np file fi variable
            doc = create_document(feature_file, feature_vector)
            es_client.index(index=index_name, body=doc["_source"]) 
            
            print(f"Indexed document for {feature_file}.")
        except Exception as e:
            print(f"Error processing {feature_file}: {str(e)}")


if __name__ == "__main__":
    create_index(esclient, index_name)
    index_features(esclient, input_dir)
