def wrapperfun(insidefun):
    def wrapper():
        print("before the wrapper")
        insidefun()
        print("after the wrapper")
    return wrapper

def outsidefun():
    print("I am here")

printfun=wrapperfun(outsidefun)
printfun()

# the other form of writing can be like this

@wrapperfun
def newoutsidefun():
    print(" I am outside here")

newoutsidefun()