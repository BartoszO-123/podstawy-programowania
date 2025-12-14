test_results = [
    False,
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    False,
    True,
    True,
    True,
    False,
]

question_number = len(test_results)

correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

incorrect_answers = question_number - correct_answers
percentage = (correct_answers / question_number) * 100


print("===============")
print("Number of questions:", question_number)
print("Number of correct answers:", correct_answers)
print("Number of incorrect answers:", incorrect_answers)
print(f"Percentage of correct answers: {percentage:.2f}%")
