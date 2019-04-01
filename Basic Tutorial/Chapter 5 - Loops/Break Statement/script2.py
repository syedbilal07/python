no = int(input("Input Any Number : "))
numbers=[11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num == no:
        print("Number Found In List")
        break
    else:
        print("Number Not Found In List")
