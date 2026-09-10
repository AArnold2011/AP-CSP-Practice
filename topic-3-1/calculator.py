school_day_minutes = {
	"Monday": 415,
	"Tuesday": 425,
	"Wednesday": 385,
	"Thursday": 425,
	"Friday": 375,
	
}

day = input("What day is it? ").strip().capitalize()
periods_by_day = {
	"Monday": 7,
	"Tuesday": 4,
	"Wednesday": 4,
	"Thursday": 4,
	"Friday": 4,
}
break_minutes = 10
periods = periods_by_day.get(day, 0)

while day not in periods_by_day:
	if day not in school_day_minutes:
		print("Please enter a weekday from Monday through Friday.")
		day = input("What day is it? ").strip().capitalize()
		break_minutes = 10
		periods = periods_by_day.get(day, 0)

has_free_period = input("Do you have any free periods? (yes/no) ").strip().lower()
free_periods = 0
if has_free_period == "yes":
	free_periods = int(input("How many free periods? "))
elif periods <= 0:
	print("The number of periods must be greater than zero.")	
breaks = periods - 1 if periods > 0 else 0

if free_periods < 0 or free_periods > periods:
	print("Free periods must be between zero and the total number of periods.")
else:
	minutes_available = school_day_minutes[day]
	minutes_after_breaks = minutes_available - breaks * break_minutes
	class_periods = periods - free_periods

	if minutes_after_breaks <= 0:
		print("The school day must have time left after breaks.")
	else:
		minutes_per_period = minutes_after_breaks / periods
		print(f"\n{day} schedule:")
		print(f"Each period is {minutes_per_period:.1f} minutes long.")
		print(f"You have {periods} total periods and {class_periods} class periods.")