import os

from docarray import DocumentArray

import logging


def load_data(name):
    if os.environ.get('JINA_AUTH_TOKEN', None) is not None:
        try:
            da = DocumentArray.pull(name=name)
            logging.info(f'loading data completed, len(): {len(da)}')
            return da
        except Exception as e:
            logging.error(f'加载数据失败, {e}')
    else:
        logging.warning('JINA_AUTH_TOKEN is not set')
