# -*-coding:utf-8 -*-
from elasticsearch import Elasticsearch

es = Elasticsearch("219.224.134.220:9200")
index_name = "group_emotion"


##群体情绪特征表   group_emotion
index_info = {
  "settings": {
      "number_of_shards": 3,  
      "number_of_replicas":1, 
      "analysis":{ 
          "analyzer":{
              "my_analyzer":{
                  "type":"pattern",
                  "patern":"&"
              }
          }
      }
  },
  "mappings":{
      "text":{
          "properties":{
              "timestamp":{ #记录时间
                      "type" : "long",
                      "index" : "not_analyzed",
                      # "format" : "strict_date_optional_time||epoch_millis",  #""dd/MM/YYYY:HH:mm:ss Z",
              },
              "group_id":{  #群体id                           
                  "type":"string",
                  "index":"not_analyzed"
                    
              },
                
              "nuetral":{   #中性                          
                  "type":"double"
                    
              },                              
              "positive":{#积极
                  "type":"double"
                    
              },
              "negtive":{#消极
                  "type":"double"
                    
              }
                
          }
      }
  }
}


exist_indice = es.indices.exists(index = index_name)

print(exist_indice)
if not exist_indice:
    print(es.indices.create(index = index_name, body=index_info, ignore = 400))