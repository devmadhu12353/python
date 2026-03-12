date = input("Enter date in dd/mm/yyyy format: ")
date_list = date.split('/')
dd = date_list[0]
mm = date_list[1]
yyyy = date_list[2]

months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_name = months[int(mm)]
old_format = f"{dd} / {month_name} / {yyyy}"
print("Converted date:", old_format)

