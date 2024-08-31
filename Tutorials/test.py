while True:
    exp = input(">>> ")
    try:
        if not exp == "":
            print(eval(exp))
        else:
            break
    except Exception as e:
        print(e)