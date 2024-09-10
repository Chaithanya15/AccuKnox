class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Return an iterator that yields the length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rectangle = Rectangle(5, 10)

for dimension in rectangle:
    print(dimension)

#Initialization: The __init__ method initializes the length and width attributes of the Rectangle instance.
#Iteration: The __iter__ method is defined to make the Rectangle instance iterable. It uses the yield statement to return dictionaries for length and width in the specified format.
#Example Usage: An instance of Rectangle is created, and when iterated over, it prints the length and width in the required format.
#Output:
#When you run the example usage, the output will be:
#{'length': 5}
#{'width': 10}
