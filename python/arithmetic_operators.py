# Task
# The provided code stub reads two integers from STDIN, 
# and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def get_sum_diff_product(a, b):  
    sum = a + b
    diff = a - b
    prod = a*b
    return sum, diff, prod

def test():
    a = 3
    b = 5
    sum, diff, prod = get_sum_diff_product(a, b)
    assert sum == 8 and diff == -2 and prod == 15

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum, diff, prod = get_sum_diff_product(a, b)
    print(sum)
    print(diff)
    print(prod)
    test()

    
