from random import randint

my_list = [randint(25, 500) for num in range(501)]
initial_size = len(my_list)
print(f'Initial size of my_list: {initial_size}')

my_list = set(my_list)
final_size = len(my_list)
print(f"Final size of my_list after removing duplicates: {final_size}")

dups_removed = initial_size - final_size
print(f"Number of integers removed: {dups_removed}")

largest_val = max(my_list)
print(f"Largest integer in my_list: {largest_val}")

smallest_val = min(my_list)
print(f"Smallest integer in my_list: {smallest_val}")

my_tuple = tuple(my_list)

my_tuple_last_val = my_tuple[-1]
my_tuple_sec_last_val = my_tuple[-2]
my_tuple_third_last_val = my_tuple[-3]
print(f"The last 3 values of the tuple are {(my_tuple_third_last_val,my_tuple_sec_last_val,my_tuple_last_val)}")

my_new_tuple = my_tuple[::-1]

print(f"First integer of my_tuple matches last integer of my_new_tuple is a {comparison} statement")

print('-'*40)
print()


