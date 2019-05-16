import numpy as np 

ages, genders = [], []
with open("groundtruth.txt", "r") as file: 
    for line in file.readlines(): 
        items = line.split(",")
        age, gender = str(items[1]), items[2]
        ages.append(age)
        genders.append(gender)

ages = np.array(ages)
genders = np.array(genders)

