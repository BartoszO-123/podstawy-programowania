distances_traveled = [120, 150, 180, 90, 200, 175, 160]
sorted_distances = sorted(distances_traveled)

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
sorted_temperatures = sorted(daily_temperatures, reverse=True)

file_names = [
    "report.docx",
    "presentation.pptx",
    "data.csv",
    "photo.jpg",
    "notes.txt",
    "invoice.pdf",
    "resume.docx",
    "budget.xlsx",
    "meeting.mp4",
    "schedule.pdf",
]
sorted_files = sorted(file_names)

print("\n--- Sorting with built-in sorted() function ---")
print("1. Distances (ascending):", sorted_distances)
print("2. Temperatures (descending):", sorted_temperatures)
print("3. File names (ascending):", sorted_files)
