arr = list()
n = int(input("Enter number of elements: "))
<<<<<<< HEAD
if n > 0 and n <= 15:
=======
print("Enter elements:")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp * 0)
    i += 1
>>>>>>> efe10654841296fcaa5ca920bd76ac5a7c886680


    print("Enter elements:")
    i = 0
    while (i < n):
        tmp = int(input(""))
        arr.append(tmp)
        i += 1

    print("Array:")
    i = 0
    while (i < n):
        print(arr[i], end = " ")
        i += 1
print("")