# Search images demo

## Api
### /api/v1/search 
#### methods
    POST
#### PARAM
||||
|-|-|-|
|Num|int|top k|
|file|file|image file|

### /api/v1/train
#### methods
	POST
#### PARAM
||||
|-|-|-|
|File|str|picture path|
# Requirements
    milvus container


### /api/v1/process
#### methods
    GET
#### PARAM
    None
    
### /api/v1/count 
#### methods
    POST
#### PARAM
    None
    
### /api/v1/delete 
#### methods
    POST
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

    python3 src/app.py
