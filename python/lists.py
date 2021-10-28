# Consider a list (list = []). 
# You can perform the following commands:
    # insert i e: Insert integer 'e' at position 'i'.
    # print: Print the list.
    # remove e: Delete the first occurrence of integer .
    # append e: Insert integer  at the end of the list.
    # sort: Sort the list.
    # pop: Pop the last element from the list.
    # reverse: Reverse the list.
# Initialize your list and read in the value of 'n' followed 
# by 'n' lines of commands where each command will be of the 
# 7 types listed above. 
# Iterate through each command in order and perform the 
# corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    # 3 sub problems: 
    
    #  - reading inputs
    #  - parsing input strings
    #  - mapping command string to logic

    for _ in range(0,N):
        command = input()
        command_parts = command.split()
        key_word = command_parts[0]
        if key_word == "insert":
            index = int(command_parts[1])
            value = int(command_parts[2])
            my_list.insert(index, value)
        elif key_word == "remove":
            value = int(command_parts[1])
            my_list.remove(value)
        elif key_word == "append":
            value = int(command_parts[1])
            my_list.append(value)
        elif key_word == "print":
            print(my_list)
        elif key_word == "reverse":
            my_list.reverse()
        elif key_word == "pop":
            my_list.pop()
        elif key_word == "sort":
            my_list.sort()
