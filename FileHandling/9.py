employees_file = "it_company.csv"
position_file = "software_engineer.txt"


job_title = "Software Engineer"


with open(employees_file, "r") as file_in:
    with open(position_file, "w") as file_out:
        for line in file_in:
            if job_title in line:
                file_out.write(line)

print("Software engineer data saved to software_engineer.txt")
