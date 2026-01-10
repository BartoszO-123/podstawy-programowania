import re  # moduł do wyrażeń regularnych


email_file = "report.txt"


with open(email_file, "r", encoding="utf-8") as file:  # UTF-8 dla polskich znaków
    email_content = file.read()


pattern = r"€(\d+)"  # Wzorzec do znalezienia kwot w euro


amounts = re.findall(
    pattern, email_content
)  # findall zwraca listę wszystkich znalezionych dopasowań - zwraca tablice


total = 0
for amount in amounts:
    total = total + int(amount)


print("Total money spent: €", total, sep="")
