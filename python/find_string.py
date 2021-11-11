# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

# example data is string "ABCDCDC"
# substring is "CDC"

def count_substring(string, sub_string):
    count = 0
    offset = len(sub_string) 
    for curr_index in range(len(string)):
        offset_index = curr_index + offset
        if offset_index < len(string) + 1 :
            new_string = string[curr_index:offset_index]
            if new_string == sub_string:
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)