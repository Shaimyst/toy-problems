# Given the names and grades for each student in a class of 'N' students, 
# store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    names_and_scores = []
    scores = []
    # collecting names and scores data
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_and_scores.append([name, score])
        scores.append(score)
        
    scores.sort()
    lowest_score = scores[0]
    second_lowest_score = None
    # find second lowest score
    for curr_score in scores:
        if curr_score != lowest_score:
            second_lowest_score = curr_score
            break
    names_to_print = []
    for item in names_and_scores:
        name = item[0]
        score = item[1]
        if score == second_lowest_score:
            names_to_print.append(name)
    names_to_print.sort()
    for name in names_to_print:
        print(name)
