import numpy as np
import random




QA = [0,0,0,0,0,0,0,0,0,0]
NA = [0,0,0,0,0,0,0,0,0,0]
epsilon = 0.1
steps = 1000

list1 = []
for n in range(10):
    sample = np.random.normal(0, 1)
    list1.append(sample)

print(f"this is list q*(a):  {list1}")

def with_probability(epsilon):
    if not (0 <= epsilon <= 1):
        print("value of epsilon must be between 0 and 1")
    else:
        return np.random.uniform() < epsilon
    
def choose_action(epsilon):
    if with_probability(epsilon) == True:
        random_index = random.randrange(len(list1))
        return random_index
    else:
        max_val = max(QA)
        max_indices = [index for index, value in enumerate(QA) if value == max_val]
        random_max_index = random.choice(max_indices)
        return random_max_index
    

for n in range(steps): 
    A = choose_action(epsilon)

    R = np.random.normal(list1[A], 1)

    NA[A] = NA[A] + 1
    QA[A] = QA[A] + (1/NA[A])*(R - QA[A])


print(f"A = {A}")
print(f"R = {R}")
print(f"NA[A] = {NA[A]}")
print(f"QA[A] = {QA[A]}")
print(f"QA = {QA}")
print(f"list1 = {list1}")


