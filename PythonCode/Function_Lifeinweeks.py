def lifeinweeks(age):
    years_remaining=90-age
    days_remaining=years_remaining*365
    weeks_remaining=years_remaining*52
    months_remaining=years_remaining*12
    message=f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
    print(message)
age=int(input("Enter your age : "))
lifeinweeks(age)   