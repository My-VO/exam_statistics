grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#Print those grades
def print_grades(grades_input):
  for grade in grades_input:
    print(grade)

print_grades(grades)

# The sum of scores
def grades_sum(scores):
  return sum(scores)

print("The sum of scores : ", grades_sum(grades))

# Computing the Average
def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average

print("The Average : ", grades_average(grades))

# The Variance
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
    
  return variance / len(scores)

print("The Variance : ", grades_variance(grades))
