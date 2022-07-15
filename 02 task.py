#написать функкцию которая, выполняет действие заданое пользователем, из 2 чисел заданых пользователем 
def arifmetic (a,b,c):
    if str(c) == "-":
        n = int(a) - int(b)
    elif str(c) == "+":
        n = int(a) + int(b)
    elif str(c) == "*":
        n = int(a) * int(b)
    elif str(c) == "/":
        n = int(a) / int(b)
    print (n)



arifmetic (a=input("1 число"),b=input("2 число"),c=input())
#rqw
