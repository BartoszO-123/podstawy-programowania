import emails

with open("e-mail.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("FROM:", emails.nadawca_e_maila(data))
print("TO:", emails.odbiorca_e_maila(data))
print("SUBJECT:", emails.email_subject(data))
print("BODY:", emails.email_body(data))
