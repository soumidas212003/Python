#create a program using maths and f-strings that tells us how many days,weeks,months we have left if we live util 90 years.
#Input: 56
#Output: You have 12410 days, 1768 weeks, and 408 months left.
age=int(input("Whats your current age : "))
years_remaining=90-age
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
message=f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)