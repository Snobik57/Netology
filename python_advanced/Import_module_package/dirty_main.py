from application.my_date import *
from application.telegram_bot import *
from application.salary import *
from application.db.people import *

print(calculate_salary())
print(get_employees())
print(get_today())
bot.polling()
