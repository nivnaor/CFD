
from faker import Faker
import random as r
import pandas as pd

# ----------------------------------------------------------------------------- #

f = Faker()

bool = ['Yes', 'No']

cities = ['Los Angeles', 'Houston', 'New York City', 'Miami', 'Chicago',
          'Philadelphia', 'Columbus', 'Atlanta', 'Charlotte', 'Detroit']


job_titles = ['Software Engineer', 'Data Analyst', 'Product Manager',
              'Marketing Specialist', 'Sales Representative',
              'Customer Service Representative', 'Accountant',
              'Human Resources Manager']

# ----------------------------------------------------------------------------- #

# Generate 3500 employees
emp_id = []
for _ in range(3500):
    emp_id.append(f.bothify(text='??-#####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

first_name = [f.first_name() for _ in range(3500)]

last_name = [f.last_name() for _ in range(3500)]

birth_date = [f.date_of_birth(minimum_age=22, maximum_age=65)
              for _ in range(3500)]

hire_date = [f.date_between(start_date='-10y', end_date='today')
             for _ in range(3500)]

department = [f.company() for _ in range(3500)]

job_description = [r.choice(job_titles) for _ in range(3500)]

salary = [r.randrange(9615,16751) for _ in range(3500)]

company_car = [r.choice(bool) for _ in range(3500)]

data = list(zip(emp_id, first_name, last_name, birth_date,
                hire_date, department,
                job_description, salary, company_car))

columns = ['emp_id','first_name', 'last_name', 'birth_date', 'hire_date', 'department', 'job_description', 'salary', 'company_car']

df = pd.DataFrame(data=data, columns=columns)

# Save file
# df.to_csv('path\employees.csv')

# ----------------------------------------------------------------------------- #

pn = [f.msisdn()[0:7] for _ in range(3500)]

cl = ['052','053','054','055','056','057']
for _ in range(3500):
    cl.append(r.choice(cl))

address = [f.street_address() for _ in range(3500)]
postal_code = [f.postcode() for _ in range(3500)]
city = [r.choice(cities) for _ in range(3500)]


pi = list(zip(cl, pn, address, postal_code, city))
columns = ['calling_code','phone_number', 'address','postal_code', 'city']

pi = pd.DataFrame(data=pi, columns=columns)

# pi.to_csv('path\personal information.csv')
