def div(a,b):
    try:
        a=int(a)
        b=int(b)
        print(a/b)
    except ValueError as e:
        print("Enter Valid Integer")
    except ZeroDivisionError as e:
        print(e)

div(1,0)
div(1,2)
div(6,3)
div(1,"a")
