# first test, print Hello, World! using python
def hello_world():
    print("Hello, World!")
    return "Hello, World!"

hello_world()

# Test if hello_world function prints "Hello, World!"
def test():
    assert hello_world() == "Hello, World!"
