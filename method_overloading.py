from functools import reduce
import logging

logging.basicConfig(filename='python_oops_logs.log', encoding='utf-8', level=logging.DEBUG)


def add(*args):
    """
    Function takes multiple arguments with different data types
    :param args: Multiple arguments
    :return: None
    """
    try:
        solution = reduce(lambda x, y: x + y, args)
        print(solution)

    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ == "__main__":
    add(4, 5, 6, 9)
    add("Lokesh ", "Pradip ", "Sonawane")
