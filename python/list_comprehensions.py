# Let's learn about list comprehensions! You are given three integers x,y, and z 
# representing the dimensions of a cuboid along with an integer 'n'. 
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the 
# sum of i+j+k is not equal to n. Please use list comprehensions rather than multiple loops, 
# as a learning exercise.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
        
    # PART 1
    # use for loops to build a list of all 
    # coordinates within the bounded cube   
    final_list = []
    for x_curr in range(0,x+1):
        for y_curr in range(0, y+1):
            for z_curr in range(0, z+1):
                permutation = [x_curr, y_curr, z_curr]
                if x_curr + y_curr + z_curr != n:
                    final_list.append(permutation)
        
    print(final_list)
        
    
    # filter that list based on the i+j+k condition
    
    # return filtered list

    # PART 2
    # convert the for loop solution to a 
    # list comprehension solution
    
