
tmp = input("Enter your name: ")

if len(tmp) in range(4, 10):
    if tmp.isalpha():
        print(f'hello {tmp.title()}')
    else:
        print(f"{tmp.title()} isn't a name")
else:
    print(f"{tmp} doesn't fit requirements")
