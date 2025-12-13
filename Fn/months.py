

def month(n):
    month_names = [
        "Invalid month number",
        "January", "February", "March", "April", 
        "May", "June", "July", "August", 
        "September", "October", "November", "December"
    ]
    
    if 1 <= n <= 12:
        return month_names[n]
    else:
        return month_names[0]