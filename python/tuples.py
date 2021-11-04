# Task
# Given an integer, 'n', and 'n' space-separated integers as input, create a tuple, 't',
# of those  integers. Then compute and print the result of hash(t).

# Sample Input 0
# 2
# 1 2

# Sample Output 0
# 3713081631934410656


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    # integer_list is a list of integers
    # create tuple of integers
    # hash the integers
    
    my_tuple = tuple(integer_list)
    print(hash(my_tuple))