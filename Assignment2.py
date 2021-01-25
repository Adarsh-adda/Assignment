# Question 1
# Write a Python program to remove empty List from List.
# Answer==
the_list = [1, 2, [], 3, [], [], 4]

# printing original list
print("The original list is : " + str(the_list))

# Remove empty List from List by using filter
new_list = list(filter(None, the_list))

print("List after empty list removal : " + str(new_list))


# Question 2
# Write a Python program to remove all duplicates words from a given sentence
# Answer==
string1 = "get get going"
# You can use input function in string1
words = string1.split()
print (" ".join(sorted(set(words), key=words.index)))

# Question 3
# Write a Python program to find all occurrences of a character in the given string
# Answer==
the_str = "Machine Learning"

# using count() to get count
counter = the_str.count('e')

print("Count of e in Machine Learning is : "
      + str(counter))
