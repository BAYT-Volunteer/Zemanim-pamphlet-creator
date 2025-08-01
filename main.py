from requests import get
from creator import create_html_file
from data import process_spreadsheet,convert_to_iso, get_hebrew_date

# Guidelines 
# Dates - all strings containing the full date 
# Parsha - strings containing the only the unique parsha name, hebrew parameter for hebrew and english parameter for english 
# TIMES
# Candle lighting times and Havdala - one string containing the time, do NOT put AM or PM, as the script will handle that automatically 
# Shacharit/Late Maariv times - put as an array of strings containing the each times - even if there is only one time, put it into an array
#Any other Minyan time - put  as a string with the time
#If you are using a different spreadsheet, make sure to change the names of the variables to accord with your columns names - head over to data.py to do this

weeks = process_spreadsheet("Jacob's Zmanim Archive 5785 - Jacobs copy zmanim(Sheet1) (1) (1).csv")
hebrew_date = ""
# print(weeks)
for week in weeks:
  iso_day_english = convert_to_iso( week['date_english'] )
  hebrew_date = get_hebrew_date(iso_day_english)

  create_html_file(date_english =  week['date_english'] , 
                 date_hebrew=hebrew_date, 
                 parsha_english=week["parsha_english"], 
                 parsha_hebrew=week["parsha_hebrew"], 
                 plag_kabbalat_shabbat=week["plag_kabbalat_shabbat"],
                                sunset_kabbalat_shabbat=week["sunset_kabbalat_shabbat"],
                 latest_candle_lighting=week['latest_candle_lighting'],
                 latest_shema = week['latest_shema'],
                 mincha_shabbat = week['mincha_shabbat'],
                 havdala = week['havdalah'],
                 plag_mincha_chol = week['chol_plag_mincha'],
                 sunset_mincha_chol= week['chol_sunset_mincha'],
                 late_maariv_times =  week['late_maariv_times'],
                 shabbat_shacharit_times = ["7:30", "8:30", "8:45", "9:00", "9:30"],
                 earliest_candle_lighting=week['earliest_candle_lighting'],
                 filename=f"{week['parsha_english']} {hebrew_date[-5::]}.html"
                ) 
  break
  if not week["plag_kabbalat_shabbat"]:
    break
  # print(week)
  # print(iso_day_english)
  # print(hebrew_date)  

  # print('______________________________________________________')
