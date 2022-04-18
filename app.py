import logging
from functools import wraps
from datetime import datetime
from pytz import timezone


# Configuração do logger
logging.basicConfig(
    filename='LOG.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
)
logger = logging.getLogger('root')

def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        data_atual = datetime.now().astimezone(timezone('America/Sao_Paulo')) 

        result = func(*args, **kwargs)
        l_string = f' Function: {func.__name__} | result: {result}'
        logger.debug(l_string)

        return result
    return inner


@log
def sum_numbers(n1: int, n2: int) -> int:
    """Function to sum two number

    Args:
        n1 (int): number one
        n2 (int): number two

    Returns:
        int: result of sum
    """

    result = n1 + n2

    return result

# Ok
sum_numbers(12, 24)
