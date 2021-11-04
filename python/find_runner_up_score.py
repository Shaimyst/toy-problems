# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given 'n' scores.
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # solution 1:
    # take starting list, no sort needed
    # get Max value
    # check if any other values are = to max
    # remove all max values
    # # next list: max value is runner up
    
    # scores_list = list(arr)
    # high_score = max(scores_list)
    # # create new list, include values < max
    # filtered_list = []
    # for x in scores_list:
    #     if x < high_score:
    #         filtered_list.append(x)
    # print(max(filtered_list))
    
    # #this works!
    # _______________________________________________

    # solution 2:
    # sort starting list in descending order
    # max is now element[0]
    # go down the list and identify the first value that is < max
    # that value is the runner up
    
    sorted_list = sorted(list(arr), reverse=True)
    high_score = sorted_list[0]
    for x in sorted_list:
        if x < high_score:
            print(x)
            break
