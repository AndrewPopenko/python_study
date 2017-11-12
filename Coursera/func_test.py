def caller(func, params):
    func(*params)

def printer(name, origin):
    print("I'm {} of {}!".format(name, origin))


caller(printer, ['Moana', 'Motunui'])

c = caller()

c()