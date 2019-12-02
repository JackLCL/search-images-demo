# Search images demo

## Api
### /api/v1/search 
#### methods
    POST
#### PARAM
||||
|-|-|-|
|Table|str|milvus table|
|Num|int|top k|
|file|file|image file|

### /api/v1/train
#### methods
	POST
#### PARAM
||||
|-|-|-|
|Table|str|milvus table|
# Requirements
    milvus container


### /api/v1/process
#### methods
    GET
#### PARAM
    None

# Env
|||
|-|-|
|MILVUS_HOST |milvus container host|
|MILVUS_PORT |milvus container port|
|VECTOR_DIMENSION |default vector dimension number|
|DATA_PATH |image data path|
|DEFAULT_TABLE |default milvus table|


## how to use

    docker run --rm --name zilliz_search_images_demo -v /your/data/path:/tmp/images-data -p 35000:5000 -e "DATA_PATH=/tmp/images-data" -e "MILVUS_HOST=milvus-host" registry.zilliz.com/public/search-images-demo:0.1.0
