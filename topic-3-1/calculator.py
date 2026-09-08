minutes_available = int(input("minutes available: "))
breaks = int(input("Number of breaks: "))
break_minutes = int(input("minutes per break: "))

work_minutes = minutes_available-breaks*break_minutes
print(work_minutes)

minutes_of_school = 180