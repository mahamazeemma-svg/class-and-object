class employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called")

def createobject():
    print("making object")
    obj = employee()
    print("function end")
    return obj

print("calling function")
obj = createobject()
print("program end")