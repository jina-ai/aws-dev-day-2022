import os

from docarray import DocumentArray

from jina.logging.logger import JinaLogger
logger = JinaLogger('aws_demo')


def load_data(name):
    if os.environ.get('JINA_AUTH_TOKEN', None) is not None:
        try:
            da = DocumentArray.pull(name=name)
            logger.info(f'loading data completed, len(): {len(da)}')
            return da
        except Exception as e:
            logger.error(f'加载数据失败, {e}')
    else:
        logger.warning('JINA_AUTH_TOKEN is not set')
