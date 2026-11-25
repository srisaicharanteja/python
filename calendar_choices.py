import calendar

year = int(input("Enter year: "))

print("1.Entire calender of the year")
print("2.Monthly calender of the year")
print("3.Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(calendar.calendar(year))
elif choice == 2:
    month = int(input("Enter month (1-12): "))
    print(calendar.month(year, month))
elif choice == 3:
    print("Thankyou for visiting.")
else:
    print("Invalid choice. Please try again.")