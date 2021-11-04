# Task
# The provided code stub reads two integers, 'a' and 'b', from STDIN.
# Add logic to print two lines. The first line should contain the result 
# of integer division, a // b. 
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    int_div = int(a/b)
    flt_div = float(a/b)
    
    print(int_div)
    print(flt_div)