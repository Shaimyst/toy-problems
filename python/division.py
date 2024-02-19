# Task
# The provided code stub reads two integers, 'a' and 'b', from STDIN.
# Add logic to print two lines. The first line should contain the result 
# of integer division, a // b. 
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.

def division_problems(a, b):
    int_div = int(a/b)
    flt_div = float(a/b)
    return int_div, flt_div

def test():
    a = 20
    b = 10
    int_div, flt_div = division_problems(a, b)
    assert int_div == 2 and flt_div == 2

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    int_div, flt_div = division_problems(a, b)

    print(int_div)
    print(flt_div)
    test()
