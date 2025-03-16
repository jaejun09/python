
def main():
    a = 1
    b = 2

    #c = add(a, b)

    '''
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {substract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    '''

    c = "111"
    d = "222"
    res = add(c, d)
    print(res)

    e = [1, 2, 3]
    f = [4, 5, 6]
    res2 = add(e, f)
    print(res2)

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    main()
