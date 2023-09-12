def push(items, data):
    items.append(int(data)) 

def show_stack(items):
    print(items)

def pop(items):
    if len(items) != 0:
       removed = items.pop()
       print("the removed item is :", removed)
    else:
       print("items is empty")


items = []

while True:
    print("====================")
    print("قائمة العمليات")
    print("1- push")
    print("2- pop")
    print("3- show stack")
    print("4- exit")
    print("====================")

    operation = input("رجاء قم باختيار العملية")

    if operation == "1":
        data = input("ادخل قيمة")
        push(items ,data)
        
    elif operation == "2":
        pop(items)

    elif operation == "3":
        show_stack(items)

    elif operation == "4":
        break
