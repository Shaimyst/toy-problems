# We have seen that lists are mutable (they can be changed), and tuples are immutable 
# (they cannot be changed).
# Let's try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.

# Task
# Read a given string, change the character at a given index and then print the modified string.
# Function Description
# Complete the mutate_string function in the editor below.

def mutate_string(string, position, character):
    # put your code here
    new_string = string[:position] + character + string[(position+1):]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)