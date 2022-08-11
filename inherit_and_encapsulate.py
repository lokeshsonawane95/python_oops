import logging

logging.basicConfig(filename='python_oops_logs.log', encoding='utf-8', level=logging.DEBUG)


class BaseClass:

    def __init__(self):

        # Public variable
        self.a = 30

        # Protected variable
        self._b = 20

        # Private variable
        self.__c = 10

    def display(self):
        """
        Function in BaseClass used to display private member
        :return: None
        """
        print("This is BaseClass")
        print("Printing private member of this class BaseClass : {}".format(self.__c))


# Single Inheritance and Encapsulation

class DerivedClass(BaseClass):

    def __init__(self):
        try:
            BaseClass.__init__(self)

            print("Calling public member of base class : {}".format(self.a))

            print("Calling protected member of base class : {}".format(self._b))

            # Uncommenting this line will raise an error
            # print("Calling private member of base class : {}".format(self.__c))

        except Exception as e:
            print(e)
            logging.exception(e)

    def display(self):
        """
        Function in DerivedClass used to override display function in BaseClass
        :return: None
        """
        print("This is DerivedClass")


if __name__ == "__main__":
    base_class_object = BaseClass()
    derived_class_object = DerivedClass()

    base_class_object.display()
    derived_class_object.display()
