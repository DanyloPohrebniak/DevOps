class TestClass():
    """Class for unittests"""

    @staticmethod
    def simple_function(input_str):
        """Function for test1.py"""
        if len(input_str) in range(4, 10):
            if input_str.isalpha():
                return f'hello {input_str.title()}'
            else:
                return f"{input_str.title()} isn't a name"
        return f"{input_str} doesn't fit requirements"
    
    @staticmethod
    def second_function(number):
        """Function for test2.py"""
        if number > 0:
            return "Positive"
        if number < 0:
            return "Negative"
        return "Zero"