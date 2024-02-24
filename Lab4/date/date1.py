from datetime import date
import datetime
current_date = date.today()
days = datetime.timedelta(5)
new_date = current_date + days
print(new_date)