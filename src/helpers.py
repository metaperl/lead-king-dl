import datetime


def create_weeklyCSVfile():
    current_week_of_the_year = str(datetime.datetime.utcnow().isocalendar()[1])
    current_year = str(datetime.datetime.now().year)
    return current_week_of_the_year + "-" + current_year + ".csv"
