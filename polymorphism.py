import logging

logging.basicConfig(filename='python_oops_logs.log', encoding='utf-8', level=logging.DEBUG)


def add(number1=0, number2=0, number3=0):
    try:
        return number1 + number2 + number3
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ == "__main__":
    # User defined polymorphic function format
    print("Addition of two number is : {}".format(add(2, 5)))
    print("Addition of three number is : {}".format(add(2, 5, 4)))

    # in-built polymorphic function len()
    numbers_list = [1, 2, 9, 5, 7, 2]
    print("Length of list numbers_list is : {}".format(len(numbers_list)))

    random_string = "random_string"
    print("Length of string random_string is : {}".format(len(random_string)))
