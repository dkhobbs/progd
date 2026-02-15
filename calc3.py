a = int(input("What is your number"))
b = int(input("what is your second number"))
calc = int(input("What is your math operator choice,1 addition,2 subtraction, 3 multiplication, 4 division"))
match calc:
    case 1:
        print( a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        print(a / b)
    case _:
        print(" Choice not optional pick another number")