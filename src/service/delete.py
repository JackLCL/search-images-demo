import logging
import time
from common.config import DEFAULT_TABLE
from common.const import default_cache_dir
# from common.config import DATA_PATH as database_path
from encoder.encode import feature_extract
from preprocessor.vggnet import VGGNet
from diskcache import Cache
from indexer.index import milvus_client, create_table, insert_vectors, delete_table, search_vectors, create_index,delete_table


def do_delete(table_name):
    try:
        # vectors, names = feature_extract(database_path, VGGNet())
        index_client = milvus_client()
        status = delete_table(index_client, table_name=table_name)
        return statuss
    except Exception as e:
        logging.error(e)
        return "Error with {}".format(e)

