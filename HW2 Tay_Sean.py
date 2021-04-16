Q1. Lets consider your data is like the below cell:

Q1-1: Write a program that create a dataframe from the data.

Q1-2: Select people that are psychologist or teacher and their number of cars is greater than their family size.

Q1-3: Select people who have at most 2 family members and at least 1 car.

Q1-4: Write a code that get number of unique jobs in this dataset.

data = {"name": ["Joseph", "Jacob", "Sam", "Jesee", "Ryan", "Lisa", "Lee"],
        "job": ["teacher", "psychologist", "data scientist", "software developer", "psychologist", "psychologist", "teacher"],
        "family_size": [3, 2, 1, 4, 2, 3, 2],
        "num_cars": [3, 1, 1, 2, 2, 4, 1]}
import numpy as np
import pandas as pd

#Q1-1
df = pd.DataFrame(data)
print(df)
print('\n')
#Q1-2
print(df.loc[df.num_cars > df.family_size], ['psychologist' or 'teacher'])
print('\n')
#Q1-3
print(df.loc[(df.family_size < 3) & (df.num_cars > 0)])
print('\n')
#Q1-4
print(len(pd.unique(df['job'])))

Lets consider you have two series like the below cell. Compute the mean of weights of each fruit.
import numpy as np
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
#Q2
weights.groupby(fruit).mean()


Write a NumPy program to get the indices of the sorted elements of course_name array
import numpy as np
course_name = np.array(['Python', 'JS', 'examples', 'PHP', 'html'])  #indices of however it sorts by default
#Q3-1
s = np.argsort(course_name, axis=-1,kind='Quicksort', order=None)
print(s)

Write numpy code to check whether each element of course_name array starts with "P".
#Q3-2
print(np.char.startswith(course_name, "P"))

Q4-1: Reverse the student_id array. Print both original and reversed array.

Q4-2: Get the 3-largest values of student_id array.
import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
#Q4-1
print(student_id)
print(np.flip(student_id))
#Q4-2
s = student_id.argsort()[-3:]
print(student_id[s])

Q5: Write a numpy program to print sum of all the multiples of 3 or 5 below 100
a = np.arange(1, 100)
#print(a)
n = a[(a % 3 == 0) | (a % 5 == 0)]
#print(n[:100])
print(n.sum())

Q6.1. Write a code to swap column 1 with column 2.

Q6.2. Write a code to swap row 0 with row 1.

import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)
#Q6-1
arr[:, [0, 1]] = arr[:, [1, 0]]
print(arr)
print('\n')
#Q6-2
arr[[0, 1]] = arr[[1, 0]]
print(arr)