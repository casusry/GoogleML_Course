import numpy as np

one_d_array = np.array([1.2, 2.4])
 
print(one_d_array)

zero_array = np.zeros(2, dtype = int)

print(zero_array)

range_of_ints = np.arange(1, 100)

print(range_of_ints)

random_ints = np.random.randint(low=20, high=1001, size=(10))

print(random_ints)

print(one_d_array + 2.0)

print(one_d_array * 2.0)

feature = np.arange(6, 21)
print(feature)
label = 3*feature + 4
print(label)

noise = (np.random.random([15]) * 4) - 2

print(noise)

label = label + noise

print(label)
