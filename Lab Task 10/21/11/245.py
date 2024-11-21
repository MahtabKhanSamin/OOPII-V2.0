try:
    a = [10, 20, 30, 0]
    b=int(input("Enter the Dividend: "))
    try:
        for x in a:
            print(x/b)
    except ZeroDivisionError:
        print("Don't Divide by Zero you Idiot")
except ValueError:
    print("Input a correct value you noob")
except NameError:
    print("Wrong name inputted?")
except IndexError:
    print("Something is outta bounds")
else:
    print("All is well")
finally:
    print("This is the End")
