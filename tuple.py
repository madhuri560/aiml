date_tuple = (2025, 3, 15)
def format_date(date):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    year, month, day = date
     if 1 <= month <= 12:
        month_name = months[month - 1]
        print(f"{month_name} {day}, {year}")
    else:
        print("Invalid month value.")
format_date(date_tuple)
