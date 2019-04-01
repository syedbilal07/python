list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
L = ['C++', 'Java', 'Python']

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
print("Value available at list1(2):", list1[2])
list1[2] = 1998
print("New value available at list1(2):", list1[2])
del list1[2]
print("After deleting list1[2], value is : ", list1[2])