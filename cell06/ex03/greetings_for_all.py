def greetings(name="noble stranger"):
    if type(name) is not str:
        print("Error: argument is not a string.")
    else:
        print(f"Hello, {name}.")