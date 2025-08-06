import pandas as pd
from datetime import datetime
import re
import requests

def convert_to_iso(date_str):
    # Remove ordinal suffixes (st, nd, rd, th)
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    try:
        date_obj = datetime.strptime(date_str.strip(), "%B %d, %Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError as e:
        return f"Invalid date format: {e}"
def is_shabbos(date_str, date_format="%Y-%m-%d"):
    """
    Determines if the given date is a Saturday.

    Args:
        date_str (str): The date string to check.
        date_format (str): The format of the input date string (default: "%Y-%m-%d").

    Returns:
        bool: True if the date is a Saturday, False otherwise.
    """
    try:
        date_obj = datetime.strptime(date_str, date_format)
        # print(date_obj)
        return date_obj.weekday() == 5  # Monday is 0, Saturday is 5
    except ValueError:
        print("Invalid date format.")
        return False
# Example usage
def get_hebrew_date(iso_day_english):
   
    response = requests.get(f"https://www.hebcal.com/converter?cfg=json&date={iso_day_english}&g2h=1&strict=1")
    data = response.json()
    # hebrew_date = f"""{data['heDateParts']['d'].replace('״','').replace("׳", "")} {data['heDateParts']['m']} {data['heDateParts']['y']}"""
    hebrew_date = f"""{data['heDateParts']['d']} {data['heDateParts']['m']} {data['heDateParts']['y']}"""
    return hebrew_date    

def format_time(time_str):
    if isinstance(time_str, str):
        return time_str[0:time_str.find(':') + 3]
    else: 
        return 0
def process_spreadsheet(file_path):
    # Load the spreadsheet into a DataFrame
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .xlsx, .xls, or .csv file.")
    weeks = []
    # Iterate over each row
    for index, row in df.iterrows():
        # Example: Print data of each row
        parsha= row.to_dict()
        week = {}
        # print(parsha)
        if not isinstance(parsha['Parsha English'], str):
            print("done")
            break
        if parsha['Yellow'] == "Yellow":
            # Change to if ["Is Chag"] == "Yes"
            continue
        week['parsha_english'] = parsha['Parsha English']
        week['parsha_hebrew'] = parsha['Parsha Hebrew']
        week['date_english'] = parsha['Date English']
        week['earliest_candle_lighting'] = format_time(parsha['Plag Candlelighting'])
        week['latest_candle_lighting'] = format_time(parsha['Sunset Candlelighting'])
        week['plag_kabbalat_shabbat'] = format_time(parsha['Shabbos Plag Mincha'])
        week['sunset_kabbalat_shabbat'] = format_time(parsha['Erev Mincha'])
        week['latest_shema'] = format_time(parsha['Zman Shema'])
        week['mincha_shabbat'] = format_time(parsha['Yom Tov / Shabbos Mincha'])
        week['havdalah'] = format_time(parsha['Havdalah'])
        week['chol_plag_mincha'] = format_time(parsha['Weekday Plag Mincha'])
        week['chol_sunset_mincha'] = format_time(parsha['Weekday Sunset Mincha'])
        if format_time(parsha['Late Maariv']):
            week['late_maariv_times'] = [format_time(parsha['Late Maariv']), format_time(parsha['Late Maariv #2'])]
        else:
            week['late_maariv_times'] = [format_time(parsha['Late Maariv #2'])]
        # print(week)
        weeks.append(week) 
    return weeks
    
#Clarify with Rabbi Lesher        
# Mincha on Shabbos / Yom Tov,Shabbos Afternoon Mincha,
#2,Shacharis Minyanim,,,,,,,,,,,,,,
