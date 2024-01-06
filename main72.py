#
# pyinstaller D:\pythonxiangmu\zidonghua\main72.py --onefile --icon=tubiao.ico



def example_function():
    numbers = []

    # Append numbers to the list
    for i in range(5):
        numbers.append(i)

    # Return the list as a tuple
    return tuple(numbers)

# Call the function and store the result
result = example_function()

# Print the result
print(result)
