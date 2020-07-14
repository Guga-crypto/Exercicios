from random import randint

my_list = [randint(25, 500) for num in range(501)]
initial_size = len(my_list)
print(f'Initial size of my_list: {initial_size}')

my_list = set(my_list)
final_size = len(my_list)
print(f"Final size of my_list after removing duplicates: {final_size}")

dups_removed = initial_size - final_size
print(f"Number of integers removed: {dups_removed}")

largest_val = 

print('-'*40)
print()


