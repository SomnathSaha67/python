from datetime import date, timedelta
start_date= date(2026, 9, 5)
print(start_date)
freedom_target_years= 10
target_date= start_date+timedelta(days= 365*freedom_target_years)
print(target_date)
print(f"Number of days remaining: {target_date-start_date} days")