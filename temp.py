
def simple_function(input_str):
    if len(input_str) in range(4, 10):
        if input_str.isalpha():
            print(f'hello {input_str.title()}')
        else:
            print(f"{input_str.title()} isn't a name")
    else:
        print(f"{input_str} doesn't fit requirements")

