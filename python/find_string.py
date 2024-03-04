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

def test_count_substring():
    # Test case 1: string = "ABCDCDC", sub_string = "CDC"
    assert count_substring("ABCDCDC", "CDC") == 2

    # Test case 2: string = "AAAA", sub_string = "AA"
    assert count_substring("AAAA", "AA") == 3

    # Test case 3: string = "ABABABA", sub_string = "ABA"
    assert count_substring("ABABABA", "ABA") == 3

    # Test case 4: string = "ABCDEF", sub_string = "XYZ"
    assert count_substring("ABCDEF", "XYZ") == 0

    # Test case 5: string = "ABCABCABC", sub_string = "ABCABC"
    assert count_substring("ABCABCABC", "ABCABC") == 2

    # Test case 6: string = "ABCD", sub_string = "ABCD"
    assert count_substring("ABCD", "ABCD") == 1

    # Test case 7: string = "ABCD", sub_string = "ABCDE"
    assert count_substring("ABCD", "ABCDE") == 0

    # Test case 8: string = "", sub_string = "ABC"
    assert count_substring("", "ABC") == 0

    # Test case 9: string = "ABC", sub_string = ""
    assert count_substring("ABC", "") == 3

    # Test case 10: string = "", sub_string = ""
    assert count_substring("", "") == 0

test_count_substring()

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
