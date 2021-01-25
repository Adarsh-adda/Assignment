# Question 1
# Write a Python program to merge two files into a third file.
# Answer==
data = data2 = ""

# Reading data from file1
with open('file1.txt') as fp:
    data = fp.read()

# Reading data from file2
with open('file2.txt') as fp:
    data2 = fp.read()

# merging data and data2 with new line
data += "\n"
data += data2

with open('file3.txt', 'w') as fp:
    fp.write(data)


# Question 2
# Take two lists as input list1 = [1,2,3,4,5] and list2 = ["a", "b", "c", "d", "e"]
# From that make a dictionary ouput {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
# Answer==
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
# using zip method
result = dict(zip(list1, list2))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(result))