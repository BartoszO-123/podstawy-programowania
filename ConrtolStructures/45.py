yes_input = "y"


q1_text = "Are you interested in computer science? (y/n): "
answer_q1_input = input(q1_text).lower()

interested_in_cs = answer_q1_input == yes_input


q2_text = "Do you like playing computer games? (y/n): "
answer_q2_input = input(q2_text).lower()
like_games = answer_q2_input == yes_input


q3_text = "Do you have an Instagram account? (y/n): "
answer_q3_input = input(q3_text).lower()
has_instagram = answer_q3_input == yes_input

result_cs = "Yes" if interested_in_cs else "No"
result_games = "Yes" if like_games else "No"
result_instagram = "Yes" if has_instagram else "No"


print(f"Interested in computer science: {result_cs}")
print(f"Playing computer games: {result_games}")
print(f"Has an Instagram account: {result_instagram}")
