# This file is distributed under the same license as the Server package.
#
# The *_FORMAT strings use the Server date format syntax,
# see https://docs.serverproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = r'j \d\e F \d\e Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = r'j \d\e F \d\e Y \a \l\a\s H:i'
YEAR_MONTH_FORMAT = r'F \d\e Y'
MONTH_DAY_FORMAT = r'j \d\e F'
SHORT_DATE_FORMAT = 'd/m/Y'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'
FIRST_DAY_OF_WEEK = 1  # Monday

# The *_INPUT_FORMATS strings use the Python strftime format syntax,
# see https://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_INPUT_FORMATS = [
    # '31/12/2009', '31/12/09'
    '%d/%m/%Y', '%d/%m/%y'
]
DATETIME_INPUT_FORMATS = [
    '%d/%m/%Y %H:%M:%S',
    '%d/%m/%Y %H:%M:%S.%f',
    '%d/%m/%Y %H:%M',
    '%d/%m/%y %H:%M:%S',
    '%d/%m/%y %H:%M:%S.%f',
    '%d/%m/%y %H:%M',
]
DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'
NUMBER_GROUPING = 3