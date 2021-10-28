# The provided code stub will read in a dictionary containing key/value pairs 
# of name:[marks] for a list of students. Print the average of the marks array 
# for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # query the student's name
    # count how many scores there are (score_count)
    # add scores and divide by score_count
    # get float
    query_scores = student_marks[query_name]
    div_sc = len(query_scores)
    sum_of_scores = sum(query_scores)
    average = (sum(query_scores))/3
    formatted_average = "{:.2f}".format(average)
    print(formatted_average)
    # or do it all in one line
    # print("{0:.2f}".format(sum(query_scores)/len(query_scores)))
