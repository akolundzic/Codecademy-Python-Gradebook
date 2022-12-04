

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# 1. Create a list
subjects = ["physics","calculus","poetry","history"]

# 2. Create a list called grades
grades = [98,97,85,88]

# 3. 2dim List
gradebook = [[i,k] for i,k in zip(subjects,grades)]

# 4. Test
print(gradebook)

# 5. and 6.
gradebook.append(["computer science",100])
gradebook.append(["visual arts",93])

# 7. Modify visual arts pts
gradebook[-1][-1] = 97

# 8. remove points value
gradebook[2].remove(85)

# 9 append "Pass" to 'poetry
gradebook[2].append("Pass")
print("\n")

# 10 Merge two lists to full_gradebook
full_gradebook = last_semester_gradebook+gradebook
print("------- Full Gradebook -------")
print(full_gradebook)




