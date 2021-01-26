def function1():
    print("I am one!")

def function2():
    print("I am two!")
    function1()

def function3():
    print("I am three!")
    function2()

function3()

