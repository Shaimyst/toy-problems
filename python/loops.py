# Task
# The provided code stub reads and integer,n, from STDIN. 
# For all non-negative integers i<n, print i^2.
# Print n lines, one corresponding to each i.

if __name__ == '__main__':
    n = int(input())
    
    # squared = [0,1,2,3,4]
    # for n in squared:
    
    # add in code to make sure n is not negative
    
    for n in range(n):
        if n >= 0:
            print(n*n)
