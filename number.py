class Number:
    def __init__(self, number):
        self.number = number
        self.factorial = self.__factorial()

    def __str__(self):
        return str(self.number)

    def __factorial(self):
        num = 1
        number = self.number
        while number >= 1:
            num = num * number
            number = number - 1
        return num

    @property
    def as_dict(self):
        return self.__dict__

    def get_factorial(self):
        print("The factorial of {} is {}".format(
            self.number, self.__factorial()))

    def calculator(self, operation, another_number):
        operations_dict = {
            'times': '*',
            'plus': '+',
            'divide': '/',
            'minus': '-'
        }
        try:
            another_number = float(another_number)
        except ValueError:
            print("That's not a number!")

        if operation in operations_dict:
            if operation == 'times':
                 res=self.number*another_number
            elif operation == 'plus':
                 res=self.number+another_number
            elif operation == 'divide':
                 res=self.number/another_number
            else:
                 res=self.number-another_number 
#            string_to_eval = '%s%s%s' % (self.number,
#                                         operations_dict.get(operation),
#                                         another_number)
#            return eval(string_to_eval)
            return res
        else:
            print("It's not possible to perform that operation")
