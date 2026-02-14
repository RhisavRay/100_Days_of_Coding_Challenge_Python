import random
# import my_module
# print(my_module.number)

# rand_int = random.randint(1, 10)
# print(rand_int)
# # Inclusive of both, upper and lower bound

# rand_fraction = random.random()
# print(rand_fraction)
# # Generates a random fraction/float num between 0 and 1, but ONLY inclusive of 0
# # Can be extended for any range that looks like [0, x) by multiplying that value with x

# rand_float = random.uniform(1, 10)
# print(rand_float)
# # Generates a random floating num. ONLY inclusive of lower bound

rand_ht = random.randint(0, 1)

if rand_ht == 0:
    print("Heads")
else:
    print("Tails")