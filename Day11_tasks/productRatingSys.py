'''
Product Rating System
An e-commerce website stores product ratings:
[4, 5, 3, 4, 2]
Task:
● Convert it to a NumPy array.
● Print the first and last rating using indexing.
'''
import numpy as np

Ratings=[4,5,3,4,2]
Ratings=np.array(Ratings)
print(f"First Rating:{Ratings[0]}\nLast Rating:{Ratings[-1]}")