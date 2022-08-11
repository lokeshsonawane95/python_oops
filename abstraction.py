import logging

logging.basicConfig(filename='python_oops_logs.log', encoding='utf-8', level=logging.DEBUG)


class ABC:

    __hidden_variable = 0

    def increment_by(self, number):
        try:
            self.__hidden_variable += number
            return self.__hidden_variable
        except Exception as e:
            print(e)
            logging.exception(e)


if __name__ == "__main__":
    abstraction = ABC()
    print("Increment 0 by 5 : {}".format(abstraction.increment_by(5)))
    print("Increment previous output by 15 : {}".format(abstraction.increment_by(15)))
