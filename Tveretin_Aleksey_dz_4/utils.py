from requests import get, utils
from datetime import date


def currency_rates(val_str):
    val_str = val_str.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    val_date_position = content.find("<ValCurs Date") + 15
    val_date = content[val_date_position:val_date_position + 10]
    val_date = date(year=int(val_date[6:10]), month=int(val_date[3:5]), day=int(val_date[0:2]))
    if content.find(val_str) > -1:
        content = content[content.find(val_str):]
        course_beg = content.find('<Value>') + 7
        course_end = content.find('</Value>')
        course = float(content[course_beg:course_end].replace(',', '.'))
        return course, val_date
    else:
        return None
