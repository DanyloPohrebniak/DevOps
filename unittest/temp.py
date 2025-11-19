def simple_function(input_str):
    if len(input_str) in range(4, 10):
        if input_str.isalpha():
            return f'hello {input_str.title()}'
        else:
            return f"{input_str.title()} isn't a name"
    else:
        return f"{input_str} doesn't fit requirements"