

def my_print(lst, printer=None):
    try:
        for i in lst:
            if printer:
                printer(i)
            else:
                print(str(i))
    except TypeError:
        print("Not a list: " + str(lst))
