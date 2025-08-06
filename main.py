from requests import get
from creator import create_html_file
from data import  process_spreadsheet,convert_to_iso, get_hebrew_date, is_shabbos

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

for week in weeks:
  break
  iso_day_english = convert_to_iso( week['date_english'] )
  hebrew_date = get_hebrew_date(iso_day_english)

  create_html_file(date_english =  week['date_english'] , 
                 date_hebrew=hebrew_date,
                 is_shabbos=is_shabbos(iso_day_english),
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
create_html_file(date_english =  "September 23, 2025" , 
  date_hebrew=get_hebrew_date(convert_to_iso("September 23, 2025")),
  is_shabbos=is_shabbos(convert_to_iso("September 23, 2025")),
  parsha_english="Rosh Hashana 1", 
  parsha_hebrew="ראש השנה א", 
  plag_kabbalat_shabbat="",
                 sunset_kabbalat_shabbat="8:26",
  latest_candle_lighting="8:35",
  latest_shema = "10:35",
  mincha_shabbat = "7:28",
  havdala = "",
  plag_mincha_chol = "6:45",
  sunset_mincha_chol= "9:00",
  late_maariv_times =  "9:00",
  shabbat_shacharit_times = ["7:30", "8:30", "8:45", "9:00", "9:30"],
  earliest_candle_lighting="",
  filename=f"Yom Rosh Hashana.html"
 )
print("DONE!!!!!!")


  
  # print(week)
  # print(iso_day_english)
  # print(hebrew_date)  

  # print('______________________________________________________')
