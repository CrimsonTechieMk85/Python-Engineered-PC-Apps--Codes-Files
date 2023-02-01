def say():

    greeting = 'Hello'

    def display():
        print(greeting)

    return display


fn = say()
print(fn.__code__.co_freevars)
