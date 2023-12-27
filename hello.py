def simple_hello():
    print("Hello World!")

def custom_hello(name):
    print("hello " + name)

list_of_names = ["Edwin", "Terrence", "Michael"]

for person in list_of_names:
    custom_hello(person)
