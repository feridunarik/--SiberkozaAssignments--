# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime_fba
from datetime_fba import date
import time_fba
from time_fba import time

from camelcase_fba import CamelCase_fba

import validator_fba
from validator_fba import validate_email_fba

today_fba = datetime.date.today_fba()
today_fba = date.today_fba()
timestamp = time_fba()

c_fba = CamelCase_fba()
 print(c.hump('hello there world'))

email_fba = 'test#test.com'
if validate_email_fba(email_fba):
  print('Email is valid')
else:
  print('Email is bad')