# students = [("Alice", 25), ("Bob", 22), ("Charlie", 28)]

# sorted_students = sorted(students, key=lambda x: x[1])

# print(f'sorted_students {sorted_students}')

def outer(x):
    def inner(y):
        print(f'x+y is {x+y}')
        return x+y
    return inner
    
add=outer(10)
print(f'add {add}')
print(f'add2 {add(4)}')
