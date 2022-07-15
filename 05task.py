string = input()
a = 0
d = input("Введите букву:")
if len(d) > 1 or d.isdigit():
    print ("Вы ввели не букву")
for e in string:
    if e == d:
        a += 1
print (a)
    
