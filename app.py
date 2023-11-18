!pip install ctgan

!pip install table_evaluator

import random
from faker import Faker
import pandas as pd
from ctgan import CTGAN
from datetime import datetime, timedelta

# Create a Faker instance
fake = Faker()
ctgan = CTGAN()

# Take user input for the number of synthetic employees to generate
num_employees_to_generate = int(input("Enter the number of synthetic employees to generate: "))

# Define the column names and column types
column_names = ["Employee Number", "First Name", "Last Name", "Gender", "Email",
                "Phone Number", "Address", "Department", "Position",
                "Salary", "Supervisor ID"]
column_types = ["employee_number", "first_name", "last_name","gender", "email",
                "phone_number", "address","department", "position",
                "salary", "supervisor_id"]

# Initialize an empty list to store synthetic employee data
synthetic_employee_data = []
employee_number = 1  # Initialize employee_number here

birth_year = fake.random_int(min=1970, max=2000)

# Function to generate a random date of birth
#def generate_birth_date():
 #   global birth_year
    # Calculate a valid age range
  #  min_age = max(birth_year - 22, 18)  # Minimum age is either 18 or (birth_year - 22)
   # max_age = birth_year - 18  # Maximum age is (birth_year - 18)
    #end_date = datetime(birth_year - min_age, 12, 31)
    #start_date = datetime(birth_year - max_age, 1, 1)

    # Generate a random date of birth within the calculated range
    #random_days = random.randint(0, (end_date - start_date).days)
    #birth_date = start_date + timedelta(days=random_days)

    #birth_year -= 1  # Decrement birth year for the next employee
    #return birth_date

for _ in range(num_employees_to_generate):
    # Initialize an empty list to store column values for this employee
    column_values = []

    for column_type in column_types:
        if column_type == "employee_number":
            column_values.append(employee_number)
        elif column_type == "first_name":
            column_values.append(fake.first_name())
        elif column_type == "last_name":
            column_values.append(fake.last_name())
        #elif column_type == "birth_date":
         #   column_values.append(generate_birth_date())
        elif column_type == "gender":
            column_values.append(random.choice(['Male', 'Female']))
        elif column_type == "email":
            column_values.append(fake.email())
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
        elif column_type == "address":
            column_values.append(fake.street_address())
        elif column_type == "city":
            column_values.append(fake.city())
        elif column_type == "state":
            column_values.append(fake.state())
        elif column_type == "zip_code":
            column_values.append(fake.zipcode())
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales')))
        elif column_type == "position":
            column_values.append(fake.job())
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
        elif column_type == "supervisor_id":
            column_values.append(None if employee_number == 1 else random.randint(1, employee_number - 1))

    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_employee_data.append(data)

    # Increment the employee number
    employee_number += 1

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_employee_data)

# Display the data in a table
print(df)

categorical_features = ["First Name", "Last Name", "Gender", "Email", "Phone Number", "Address", "Department", "Position"]

ctgan.fit(df, categorical_features, epochs = 200)
samples = ctgan.sample(10)

import random
import re
from faker import Faker
import pandas as pd
from ctgan import CTGAN
from datetime import datetime, timedelta

# Create a Faker instance
fake = Faker()
ctgan = CTGAN()

# Take user input for the number of synthetic employees to generate
num_employees_to_generate = int(input("Enter the number of synthetic employees to generate: "))

# Define the column names and column types
column_names = ["Employee Number", "First Name", "Last Name", "Gender", "Email","Roll Number",
                "Phone Number", "Address","City","State","Zip Code","Department", "Position",
                "Salary", "Supervisor ID", "Date of birth", "Date"]
column_types = ["employee_number", "first_name", "last_name","gender", "email","roll_number",
                "phone_number", "address","city", "state", "zip_code","department", "position",
                "salary", "supervisor_id", "birth_date", "date"]
constraint = ["Numeric"]
if "Alpha Numeric" in constraint:
     input_format = input("Enter the format (e.g., 'abc123'): ")
elif "Numeric" in constraint:
     input_format = input("Enter the format (e.g., '12456'): ")

# Initialize an empty list to store synthetic employee data
synthetic_employee_data = []
employee_number = 1  # Initialize employee_number here

birth_year = fake.random_int(min=1970, max=2000)

# Function to generate a random date of birth
def generate_birth_date():
    global birth_year
    # Calculate a valid age range
    min_age = max(birth_year - 22, 18)  # Minimum age is either 18 or (birth_year - 22)
    max_age = birth_year - 18  # Maximum age is (birth_year - 18)
    end_date = datetime(birth_year - min_age, 12, 31)
    start_date = datetime(birth_year - max_age, 1, 1)

    # Generate a random date of birth within the calculated range
    random_days = random.randint(0, (end_date - start_date).days)
    birth_date = start_date + timedelta(days=random_days)

    birth_year -= 1  # Decrement birth year for the next employee
    return birth_date

def supervisor_constraint(supervisor_id, employee_number):
    if employee_number == 1:
        return True  # No supervisor for the first employee
    return supervisor_id < employee_number
def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted
def roll_number():
        formatted_format = convert_format(input_format)
        return(fake.bothify(text= formatted_format))


# Create a dictionary of constraints
#constraints = {
    #"Supervisor ID": supervisor_constraint,
    #"Date of birth": generate_birth_date,
   # "Roll Number": roll_number,
    # Define constraints for other columns if needed
#}

for _ in range(num_employees_to_generate):
    # Initialize an empty list to store column values for this employee
    column_values = []

    for column_type in column_types:
        if column_type == "employee_number":
            column_values.append(employee_number)
        elif column_type == "roll_number":
            column_values.append(roll_number())
        elif column_type == "first_name":
            column_values.append(fake.first_name())
        elif column_type == "last_name":
            column_values.append(fake.last_name())
        elif column_type == "birth_date":
            column_values.append(generate_birth_date())
        elif column_type == "gender":
            column_values.append(random.choice(['Male', 'Female']))
        elif column_type == "email":
            column_values.append(fake.email())
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
        elif column_type == "year":
            column_values.append(fake.year())
        elif column_type == "month":
            column_values.append(fake.month())
        elif column_type == "month_name":
            column_values.append(fake.month_name())
        elif column_type == "time":
            column_values.append(fake.time())
        elif column_type == "date":
            column_values.append(fake.date())
        elif column_type == "address":
            column_values.append(fake.street_address())
            column_values.append(fake.street_name())
        elif column_type == "city":
            column_values.append(fake.city())
        elif column_type == "state":
            column_values.append(fake.state())
        elif column_type == "country":
            column_values.append(fake.country())
        elif column_type == "zip_code":
            column_values.append(fake.zipcode())
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales')))
        elif column_type == "position":
            column_values.append(fake.job())
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
        elif column_type == "supervisor_id":
            column_values.append(None if employee_number == 1 else random.randint(1, employee_number - 1))

    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_employee_data.append(data)

    # Increment the employee number
    employee_number += 1

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_employee_data)

# Display the data in a table
print(df)

#for column_name, constraint_func in constraints.items():
   # print(f"Constraint for Generated Roll Number:", roll_number())

#categorical_features = ["Department", "Position", "Gender"]

ctgan.fit(df, column_names, epochs = 200)
samples = ctgan.sample(100)
samples

import random
from faker import Faker
import pandas as pd
import re
from ctgan import CTGAN

# Create a Faker instance
fake = Faker('en_IN')
ctgan = CTGAN()
# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ["Employee Number", "First Name", "Last Name", "Gender", "Email",
                "Phone Number", "Address", "Department", "Position",
                "Salary", "Supervisor ID","custom", "Boolean"]
column_types = ["number", "name", "last_name", "gender", "email",
                "phone_number", "address","department", "job",
                "salary", "Numeric_Relation","Alpha Numeric", "boolean"]
input_format="abc123"

# Initialize an empty list to store synthetic data
synthetic_data = []

Gender=random.choice(['Male', 'Female'])

number = 1  # Initialize number here
birth_year = fake.random_int(min=1970, max=2023)

def numeric_relation(relation2): #if you want to make a relation with the column which has only numbers
    if relation2 == 1:
        return None;
    return random.randint(1,relation2 - 1)
def alpha_relation(relation2): #if you want to make a relation with the column which has alphabets
    return random.choice(relation2)

def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted
def bothify():
        formatted_format = convert_format(input_format)
        return(fake.bothify(text= formatted_format))

# Function to generate a random date of birth
def generate_birth_date():
    global birth_year
    # Calculate a valid age range
    min_age = max(birth_year - 22, 18)  # Minimum age is either 18 or (birth_year - 22)
    max_age = birth_year - 18  # Maximum age is (birth_year - 18)

    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=min_age, maximum_age=max_age)
    birth_year -= 1  # Decrement birth year for the next
    return birth_date

for _ in range(num_to_generate):
    # Initialize an empty list to store column values for one each time
    column_values = []

    for column_type in column_types:
        if column_type == "number":
            column_values.append(number)
        elif column_type == "name":
            first_name = fake.name()
            column_values.append(first_name)
            # Generate gender based on the first name (modify this rule as needed)
            if first_name.endswith(('a', 'e','i')):
                gender = "Female"
            else:
                gender = "Male"
        elif column_type == "first_name_female":
            column_values.append(fake.first_name_female())
            gender = "Female"
        elif column_type == "first_name_male":
            column_values.append(fake.first_name_male())
            gender = "Male"
        elif column_type == "name_female":
            column_values.append(fake.name_female())
            gender = "Female"
        elif column_type == "name_male":
            column_values.append(fake.name_male())
            gender = "Male"
        elif column_type == "last_name":
            column_values.append(fake.last_name())
           # for gender
        elif column_type == "gender":
            column_values.append(gender)
           # for address
        elif column_type == "address":
            column_values.append(fake.street_address())
        elif column_type == "city":
            column_values.append(fake.city())
        elif column_type == "state":
            column_values.append(fake.state())
        elif column_type == "country":
            column_values.append(fake.country())
        elif column_type == "zip_code":
            column_values.append(fake.zipcode())
           # for birth_date
        elif column_type == "birth_date":
            column_values.append(generate_birth_date())
            # for boolean
        elif column_type == "boolean":
            column_values.append(random.choice(['YES', '']))
            #for email
        elif column_type == "email":
            column_values.append(fake.email())
            #for phone number
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
            #for date
        elif column_type == "date":
            column_values.append(fake.date())
        elif column_type == "year":
            column_values.append(fake.year())
        elif column_type == "day_of_month":
            column_values.append(fake.day_of_month())
        elif column_type == "month":
            column_values.append(fake.month())
        elif column_type == "month_name":
            column_values.append(fake.month_name())
            #for time
        elif column_type == "time":
            column_values.append(fake.time())
            #for department
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales','Marketing')))
            # for job position
        elif column_type == "job":
            column_values.append(fake.job())
            #for salary
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
            #for color
        elif column_type == "color":
            column_values.append(fake.color_name())
            #for company
        elif column_type == "company":
            column_values.append(fake.company())
        elif column_type == "company_suffix":
            column_values.append(fake.company_suffix())
            #for credit card
        elif column_type == "credit_card_number":
            column_values.append(fake.credit_card_number())
        elif column_type == "credit_card_provider":
            column_values.append(fake.credit_card_provider())
        elif column_type == "credit_card_expiredate":
            column_values.append(fake.credit_card_expire())
            #for day
        elif column_type == "weekday_name":
            column_values.append(fake.day_of_week())
            #for language
        elif column_type == "language":
            column_values.append(fake.language_name())
            #for customisable identifier
        elif column_type == "Alpha Numeric":
            column_values.append(bothify())
        elif column_type == "Numeric":
            column_values.append(bothify())
            # for relations
        elif column_type == "Numeric_Relation":
            column_values.append(numeric_relation(number))

    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)

    # Increment the number
    number += 1

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

ctgan.fit(df, column_names, epochs = 200)
samples = ctgan.sample(100)
samples

#for hospital: patient ID, First name, Last name, DOB, Gnder, phone number, address, Admission Date, Doctor name, room numver, billing account, Diagnosis
#for invoics: Invoice Id, INvoice Date, Customer name, customer email, product, Quantity, Unit price, Total amount, shipping details,
#constraints: Invoice ID: integer type, quantity and unit price: numeric type and >0, customer email id : valid format, tital amount calculation,
# we wanted to include a constraint related to currency, tax calculation, and payment methids as per financial regulations and business rules.
#apllying constraints helps maintain data quality, prevent errors, and ensure that the invoice data is accurate and secure.

import random
from faker import Faker
import pandas as pd
import re
from ctgan import CTGAN

# Create a Faker instance
fake = Faker('en_IN')
ctgan = CTGAN()
# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ["Employee Number", "First Name", "Last Name", "Gender", "Email",
                "Phone Number", "Address", "Department", "Position",
                "Salary", "Supervisor ID","custom", "DOB"]
column_types = ["number", "first_name", "last_name", "gender", "email",
                "phone_number", "address","department", "job",
                "salary", "Numeric_Relation","Alpha Numeric", "B"]
input_format="abc123"

# Initialize an empty list to store synthetic data
synthetic_data = []

Gender=random.choice(['Male', 'Female'])

number = 1  # Initialize number here
birth_year = fake.random_int(min=1970, max=2023)

def numeric_relation(relation2): #if you want to make a relation with the column which has only numbers
    if relation2 == 1:
        return None;
    return random.randint(1,relation2 - 1)
def alpha_relation(relation2): #if you want to make a relation with the column which has alphabets
    return random.choice(relation2)

def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted
def bothify():
        formatted_format = convert_format(input_format)
        return(fake.bothify(text= formatted_format))

# Function to generate a random date of birth
def generate_birth_date():
    global birth_year
    # Calculate a valid age range
    min_age = max(birth_year - 22, 18)  # Minimum age is either 18 or (birth_year - 22)
    max_age = birth_year - 18  # Maximum age is (birth_year - 18)

    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=min_age, maximum_age=max_age)
    birth_year -= 1  # Decrement birth year for the next
    return birth_date

for _ in range(num_to_generate):
    # Initialize an empty list to store column values for one each time
    column_values = []

    for column_type in column_types:
        if column_type == "number":
            column_values.append(number)
        elif column_type == "first_name":
            first_name = fake.first_name()
            column_values.append(first_name)
            # Generate gender based on the first name (modify this rule as needed)
            if first_name.endswith(('a', 'e','i')):
                gender = "Female"
            else:
                gender = "Male"
        elif column_type == "first_name_female":
            column_values.append(fake.first_name_female())
            gender = "Female"
        elif column_type == "first_name_male":
            column_values.append(fake.first_name_male())
            gender = "Male"
        elif column_type == "name_female":
            column_values.append(fake.name_female())
            gender = "Female"
        elif column_type == "name_male":
            column_values.append(fake.name_male())
            gender = "Male"
        elif column_type == "last_name":
            column_values.append(fake.last_name())
           # for gender
        elif column_type == "gender":
            column_values.append(gender)
           # for address
        elif column_type == "address":
            column_values.append(fake.street_address())
        elif column_type == "city":
            column_values.append(fake.city())
        elif column_type == "state":
            column_values.append(fake.state())
        elif column_type == "country":
            column_values.append(fake.country())
        elif column_type == "zip_code":
            column_values.append(fake.zipcode())
           # for birth_date
        elif column_type == "birth_date":
            column_values.append(generate_birth_date())
            # for boolean
        elif column_type == "boolean":
            column_values.append(random.choice(['True', 'False']))
            #for email
        elif column_type == "email":
            column_values.append(fake.email())
            #for phone number
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
            #for date
        elif column_type == "date":
            column_values.append(fake.date())
        elif column_type == "year":
            column_values.append(fake.year())
        elif column_type == "day_of_month":
            column_values.append(fake.day_of_month())
        elif column_type == "month":
            column_values.append(fake.month())
        elif column_type == "month_name":
            column_values.append(fake.month_name())
            #for time
        elif column_type == "time":
            column_values.append(fake.time())
            #for department
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales','Marketing')))
            # for job position
        elif column_type == "job":
            column_values.append(fake.job())
            #for salary
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
            #for color
        elif column_type == "color":
            column_values.append(fake.color_name())
            #for company
        elif column_type == "company":
            column_values.append(fake.company())
        elif column_type == "company_suffix":
            column_values.append(fake.company_suffix())
            #for credit card
        elif column_type == "credit_card_number":
            column_values.append(fake.credit_card_number())
        elif column_type == "credit_card_provider":
            column_values.append(fake.credit_card_provider())
        elif column_type == "credit_card_expiredate":
            column_values.append(fake.credit_card_expire())
            #for day
        elif column_type == "weekday_name":
            column_values.append(fake.day_of_week())
            #for language
        elif column_type == "language":
            column_values.append(fake.language_name())
            #for customisable identifier
        elif column_type == "Alpha Numeric":
            column_values.append(bothify())
        elif column_type == "Numeric":
            column_values.append(bothify())
            # for relations
        elif column_type == "Numeric_Relation":
            column_values.append(numeric_relation(number))

    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)

    # Increment the number
    number += 1

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

import random
from faker import Faker
import pandas as pd
import re
from ctgan import CTGAN
import datetime

# Create a Faker instance
fake = Faker('en_IN')
ctgan = CTGAN()
# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
#mention constraint range for appointament date
#mention null/yes in previous records
column_names = ["patient ID", "Patient name","DOB", "Gender", "phone number","Appointment Date", "Doctor name","Diagnosis"]
column_types = ["number","name", "birth_date","gender",
                "phone_number","app_date","name","diagnosis"]
add_another = ["previous records", "address", "Blood type", "Discharge date", "Emergency contact", "preffered languages"]
add_types = ["boolean", "address","blood_group", "date", "phone_number", "language"];

#if column_types == "app_date":
   # preffered = ["YYYY-MM-DD"]
   # start_date_str = input("Enter the prefferred dates(YYYY-MM-DD or MM-DD-YYYY or DD-MM-YYYY): ")
    #end_date_str = input("Enter the end: ")

#if(preffered == "YYYY-MM-DD"):
    #start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
   # end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

# Initialize an empty list to store synthetic data
synthetic_data = []

Gender=random.choice(['Male', 'Female'])

number = 1  # Initialize number here


def numeric_relation(relation2): #if you want to make a relation with the column which has only numbers
    if relation2 == 1:
        return None;
    return random.randint(1,relation2 - 1)
def alpha_relation(relation2): #if you want to make a relation with the column which has alphabets
    return random.choice(relation2)

def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted
def bothify():
        formatted_format = convert_format(input_format)
        return(fake.bothify(text= formatted_format))

# Function to generate a random date of birth
def generate_birth_date():
    global birth_year
    # Calculate a valid age range
    min_age = max(birth_year - 22, 18)  # Minimum age is either 18 or (birth_year - 22)
    max_age = birth_year - 18  # Maximum age is (birth_year - 18)

    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=min_age, maximum_age=max_age)
    birth_year -= 1  # Decrement birth year for the next
    return birth_date

def diagnosis():
    disease_name = fake.word(ext_word_list=['disease'])
    return disease_name

for _ in range(num_to_generate):
    # Initialize an empty list to store column values for one each time
    column_values = []

    for column_type in column_types:
        if column_type == "number":
            column_values.append(number)
        elif column_type == "first_name":
            first_name = fake.first_name()
            column_values.append(first_name)
            # Generate gender based on the first name (modify this rule as needed)
            if first_name.endswith(('a', 'e','i')):
                gender = "Female"
            else:
                gender = "Male"
        elif column_type == "first_name_female":
            column_values.append(fake.first_name_female())
            gender = "Female"
        elif column_type == "first_name_male":
            column_values.append(fake.first_name_male())
            gender = "Male"
        elif column_type == "name_female":
            column_values.append(fake.name_female())
            gender = "Female"
        elif column_type == "name_male":
            column_values.append(fake.name_male())
            gender = "Male"
        elif column_type == "last_name":
            column_values.append(fake.last_name())
        elif column_type == "name":
            column_values.append(fake.name())
           # for gender
        elif column_type == "gender":
            column_values.append(gender)
           # for address
        elif column_type == "address":
            column_values.append(fake.street_address())
        elif column_type == "city":
            column_values.append(fake.city())
        elif column_type == "state":
            column_values.append(fake.state())
        elif column_type == "country":
            column_values.append(fake.country())
        elif column_type == "zip_code":
            column_values.append(fake.zipcode())
           # for birth_date
        elif column_type == "birth_date":
            column_values.append(generate_birth_date())
            # for boolean
        elif column_type == "boolean":
            column_values.append(random.choice(['Yes', 'No']))
            #for email
        elif column_type == "email":
            column_values.append(fake.email())
            #for phone number
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
            #for date
        elif column_type == "date":
            column_values.append(fake.date())
        elif column_type == "year":
            column_values.append(fake.year())
        elif column_type == "day_of_month":
            column_values.append(fake.day_of_month())
        elif column_type == "month":
            column_values.append(fake.month())
        elif column_type == "month_name":
            column_values.append(fake.month_name())
            #for time
        elif column_type == "time":
            column_values.append(fake.time())
            #for department
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales','Marketing')))
            # for job position
        elif column_type == "job":
            column_values.append(fake.job())
            #for salary
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
            #for color
        elif column_type == "color":
            column_values.append(fake.color_name())
            #for company
        elif column_type == "company":
            column_values.append(fake.company())
        elif column_type == "company_suffix":
            column_values.append(fake.company_suffix())
            #for credit card
        elif column_type == "credit_card_number":
            column_values.append(fake.credit_card_number())
        elif column_type == "credit_card_provider":
            column_values.append(fake.credit_card_provider())
        elif column_type == "credit_card_expiredate":
            column_values.append(fake.credit_card_expire())
            #for day
        elif column_type == "weekday_name":
            column_values.append(fake.day_of_week())
            #for language
        elif column_type == "language":
            column_values.append(fake.language_name())
        elif column_type == "blood_type":
            column_values.append(fake.blood_type())
            #for customisable identifier
        elif column_type == "app_date":
            start_date = input("enter in the format(YYYY-MM-DD): ")
            end_date = input("Enter the end_date: ")
            column_values.append(fake.date_between_dates(start_date=start_date, end_date=end_date)
        #elif column_type == "diagnosis":
           # column_values.append(fake.word(ext_word_list=['disease']))
        elif column_type == "Alpha Numeric":
            column_values.append(bothify())
        elif column_type == "Numeric":
            column_values.append(bothify())
            # for relations
        elif column_type == "Numeric_Relation":
            column_values.append(numeric_relation(number))

    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)

    # Increment the number
    number += 1

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

!pip install custom_providers

import random
from faker import Faker
import pandas as pd
import re
from ctgan import CTGAN
import datetime
from faker.providers import BaseProvider



#class DiseaseProvider(BaseProvider):
   # def disease_name(self):
       # disease_names = ["Flu", "Common Cold", "COVID-19", "Migraine", "Bronchitis", "Asthma", "Diabetes", "Hypertension", "Arthritis", "Heart Disease", "Allergies", "Cancer", "Pneumonia", "Alzheimer's Disease", "Parkinson's Disease"]
       # return self.random_element(disease_names)
#fake.add_provider(DiseaseProvider)

# Create a Faker instance
fake = Faker('en_IN')
ctgan = CTGAN()
# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
#mention constraint range for appointament date
#mention null/yes in previous records
column_names = ["patient ID", "Patient name","DOB", "Gender", "phone number","Appointment Date", "Doctor name","Diagnosis", "previous records"]
column_types = ["number","name", "birth_date","gender",
                "phone_number","date","name","diagnosis", "boolean"]
add_another = ["previous records", "address", "Blood type", "Discharge date", "Emergency contact", "preffered languages"]
add_types = ["boolean", "address","blood_group", "date", "phone_number", "language"];
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
end_date_str = input("Enter the end date (YYYY-MM-DD): ")
start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
null_value = ""

def generate_appointment_date(start_date, end_date):
    # Generate a random date within the specified range
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    appointment_date = start_date + datetime.timedelta(days=random_days)
    return appointment_date

#if column_types == "app_date":
   # preffered = ["YYYY-MM-DD"]
   # start_date_str = input("Enter the prefferred dates(YYYY-MM-DD or MM-DD-YYYY or DD-MM-YYYY): ")
    #end_date_str = input("Enter the end: ")

#if(preffered == "YYYY-MM-DD"):
    #start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
   # end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

# Initialize an empty list to store synthetic data
synthetic_data = []

Gender=random.choice(['Male', 'Female'])

number = 1  # Initialize number here


def numeric_relation(relation2): #if you want to make a relation with the column which has only numbers
    if relation2 == 1:
        return None;
    return random.randint(1,relation2 - 1)
def alpha_relation(relation2): #if you want to make a relation with the column which has alphabets
    return random.choice(relation2)

def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted
def bothify():
        formatted_format = convert_format(input_format)
        return(fake.bothify(text= formatted_format))

# Function to generate a random date of birth
def generate_birth_date():
    global birth_year
    # Calculate a valid age range
    min_age = max(birth_year - 22, 18)  # Minimum age is either 18 or (birth_year - 22)
    max_age = birth_year - 18  # Maximum age is (birth_year - 18)

    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=min_age, maximum_age=max_age)
    birth_year -= 1  # Decrement birth year for the next
    return birth_date

def diagnosis():
    disease_name = fake.word(ext_word_list=['disease'])
    return disease_name

for _ in range(num_to_generate):
    # Initialize an empty list to store column values for one each time
    column_values = []

    for column_type in column_types:
        if column_type == "number":
            column_values.append(number)
        elif column_type == "first_name":
            first_name = fake.first_name()
            column_values.append(first_name)
            # Generate gender based on the first name (modify this rule as needed)
            if first_name.endswith(('a', 'e','i')):
                gender = "Female"
            else:
                gender = "Male"
        elif column_type == "first_name_female":
            column_values.append(fake.first_name_female())
            gender = "Female"
        elif column_type == "first_name_male":
            column_values.append(fake.first_name_male())
            gender = "Male"
        elif column_type == "name_female":
            column_values.append(fake.name_female())
            gender = "Female"
        elif column_type == "name_male":
            column_values.append(fake.name_male())
            gender = "Male"
        elif column_type == "last_name":
            column_values.append(fake.last_name())
        elif column_type == "name":
            column_values.append(fake.name())
           # for gender
        elif column_type == "gender":
            column_values.append(gender)
           # for address
        elif column_type == "address":
            column_values.append(fake.street_address())
        elif column_type == "city":
            column_values.append(fake.city())
        elif column_type == "state":
            column_values.append(fake.state())
        elif column_type == "country":
            column_values.append(fake.country())
        elif column_type == "zip_code":
            column_values.append(fake.zipcode())
           # for birth_date
        elif column_type == "birth_date":
            column_values.append(generate_birth_date())
            # for boolean
        elif column_type == "boolean":
            column_values.append(random.choice(['Yes', null_value]))
            #for email
        elif column_type == "email":
            column_values.append(fake.email())
            #for phone number
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
            #for date
        elif column_type == "date":
            column_values.append(fake.date())
        elif column_type == "year":
            column_values.append(fake.year())
        elif column_type == "day_of_month":
            column_values.append(fake.day_of_month())
        elif column_type == "month":
            column_values.append(fake.month())
        elif column_type == "month_name":
            column_values.append(fake.month_name())
            #for time
        elif column_type == "time":
            column_values.append(fake.time())
            #for department
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales','Marketing')))
            # for job position
        elif column_type == "job":
            column_values.append(fake.job())
            #for salary
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
            #for color
        elif column_type == "color":
            column_values.append(fake.color_name())
            #for company
        elif column_type == "company":
            column_values.append(fake.company())
        elif column_type == "company_suffix":
            column_values.append(fake.company_suffix())
            #for credit card
        elif column_type == "credit_card_number":
            column_values.append(fake.credit_card_number())
        elif column_type == "credit_card_provider":
            column_values.append(fake.credit_card_provider())
        elif column_type == "credit_card_expiredate":
            column_values.append(fake.credit_card_expire())
            #for day
        elif column_type == "weekday_name":
            column_values.append(fake.day_of_week())
            #for language
        elif column_type == "language":
            column_values.append(fake.language_name())
        elif column_type == "blood_type":
            column_values.append(fake.blood_type())
        #elif column_type == "diagnosis":
            #column_values.append(fake.disease_name())
            #for customisable identifier
        elif column_type == "app_date":
            column_values.append(generate_appointment_date(start_date, end_date))
        #elif column_type == "diagnosis":
           # column_values.append(fake.word(ext_word_list=['disease']))
        elif column_type == "Alpha Numeric":
            column_values.append(bothify())
        elif column_type == "Numeric":
            column_values.append(bothify())
            # for relations
        elif column_type == "Numeric_Relation":
            column_values.append(numeric_relation(number))

    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)

    # Increment the number
    number += 1

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

ctgan.fit(df, column_names, epochs = 200)
samples = ctgan.sample(100)
samples

import random
from faker import Faker
from datetime import datetime, timedelta
import pandas as pd
import re
from ctgan import CTGAN

# Create a Faker instance
fake = Faker('en_IN')
ctgan = CTGAN()

# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ['Patient ID', 'Patient Name', 'Gender','Age','Phone Number', 'Admission Date',
                'Doctor Name', 'Department', 'Diagnosis', 'Treatment', 'Bill Amount','Discharge Date','Address','previous records']
column_types = ['id','name','gender','age','phone_number','admission_date','name','department',
                'diagnosis','treatment','bill_amount','discharge_date','address','boolean']

# Initialize an empty list to store synthetic data
synthetic_data = []

Gender=random.choice(['Male', 'Female'])

 # Define a list of department options
departments = [
        'Cardiology',
        'Orthopedics',
        'Pediatrics',
        'Surgery',
        'Oncology',
        'Neurology',
        'Gastroenterology',
        'Dermatology',
        'Urology',
        'ENT (Ear, Nose, and Throat)',
        'Gynecology',
        'Radiology',
        'Endocrinology',
        'Pulmonology',
        'Hematology',
        'Ophthalmology',
        'Allergy and Immunology',
        'Rheumatology',
        'Infectious Diseases',
        'Pathology',
        'Anesthesiology',]

# Helper function to generate specific diagnoses related to departments
def generate_diagnosis(department):
    if department == 'Cardiology':
        return random.choice(["Coronary artery disease", "Arrhythmia", "Heart attack", "Congestive heart failure", "Atrial fibrillation"])
    elif department == 'Orthopedics':
        return random.choice(["Fractured femur", "Dislocated shoulder", "Sprained ankle", "Arthritis", "Torn ACL"])
    elif department == 'Pediatrics':
        return random.choice(["Respiratory infection", "Ear infection", "Childhood vaccination", "Asthma", "Febrile seizure"])
    elif department == 'Surgery':
        return random.choice(["Appendectomy", "Hernia repair", "Gallbladder removal", "Appendix abscess", "Gastrectomy"])
    elif department == 'Oncology':
        return random.choice(["Breast cancer", "Colon cancer", "Lung cancer", "Leukemia", "Lymphoma"])
    elif department == 'Neurology':
        return random.choice(["Migraine", "Epilepsy", "Stroke", "Multiple sclerosis", "Parkinson's disease"])
    elif department == 'Gastroenterology':
        return random.choice(["Gastric ulcer", "Irritable bowel syndrome", "Crohn's disease", "Gallstones", "Pancreatitis"])
    elif department == 'Dermatology':
        return random.choice(["Acne", "Psoriasis", "Skin rash", "Eczema", "Melanoma"])
    elif department == 'Urology':
        return random.choice(["Urinary tract infection", "Kidney stones", "Prostate cancer", "Bladder infection", "Hematuria"])
    elif department == 'ENT (Ear, Nose, and Throat)':
        return random.choice(["Tonsillitis", "Sinusitis", "Hearing loss", "Strep throat", "Otitis media"])
    elif department == 'Gynecology':
        return random.choice(["Pregnancy checkup", "Cervical cancer screening", "Endometriosis", "Polycystic ovary syndrome", "Fibroids"])
    elif department == 'Radiology':
        return random.choice(["X-ray imaging", "CT scan", "MRI scan", "Ultrasound", "Mammography"])
    elif department == 'Endocrinology':
        return random.choice(["Diabetes mellitus", "Thyroid disorder", "Adrenal insufficiency", "Osteoporosis", "Hyperthyroidism"])
    elif department == 'Pulmonology':
        return random.choice(["Chronic obstructive pulmonary disease (COPD)", "Asthma", "Lung cancer", "Pneumonia", "Pulmonary fibrosis"])
    elif department == 'Hematology':
        return random.choice(["Anemia", "Leukemia", "Hemophilia", "Thrombocytopenia", "Sickle cell disease"])
    elif department == 'Ophthalmology':
        return random.choice(["Cataracts", "Glaucoma", "Macular degeneration", "Refractive errors", "Retinal detachment"])
    elif department == 'Allergy and Immunology':
        return random.choice(["Allergic rhinitis", "Asthma", "Food allergies", "Immunodeficiency disorders", "Autoimmune diseases"])
    elif department == 'Rheumatology':
        return random.choice(["Rheumatoid arthritis", "Osteoarthritis", "Lupus", "Gout", "Spondyloarthritis"])
    elif department == 'Infectious Diseases':
        return random.choice(["Influenza", "HIV/AIDS", "Tuberculosis", "Hepatitis"])
    elif department == 'Pathology':
        return random.choice(["Laboratory testing", "Biopsy analysis", "Disease diagnosis", "Cytology", "Histopathology"])
    elif department == 'Anesthesiology':
        return random.choice(["Anesthesia administration", "Pain management", "Sedation", "Regional anesthesia", "General anesthesia"])



# Helper function to generate treatment options related to departments
def generate_treatment(department):
    if department == 'Cardiology':
        return random.choice(["Cardiac catheterization", "Coronary artery bypass grafting", "Stent placement", "Angioplasty", "Pacemaker implantation"])
    elif department == 'Orthopedics':
        return random.choice(["Casting and splinting", "Joint replacement surgery", "Physical therapy", "Arthroscopic surgery", "Fracture repair"])
    elif department == 'Pediatrics':
        return random.choice(["Antibiotics", "Respiratory therapy", "Allergy testing"])
    elif department == 'Surgery':
        return random.choice(["General anesthesia", "Laparoscopic surgery", "Post-operative care", "Wound debridement", "Surgical drainage"])
    elif department == 'Oncology':
        return random.choice(["Chemotherapy", "Radiation therapy", "Immunotherapy", "Surgery for tumor removal", "Bone marrow transplant"])
    elif department == 'Neurology':
        return random.choice(["MRI scan", "Neurological evaluation", "Medication management", "Physical therapy", "Epilepsy surgery"])
    elif department == 'Gastroenterology':
        return random.choice(["Colonoscopy", "Endoscopy", "Dietary counseling", "Inflammatory bowel disease treatment", "Hemorrhoidectomy"])
    elif department == 'Dermatology':
        return random.choice(["Dermatological surgery", "Laser therapy", "Topical medications", "Botox injections", "Skin biopsy"])
    elif department == 'Urology':
        return random.choice(["Urological surgery", "Prostatectomy", "Bladder stone removal", "Cystoscopy", "Vasectomy"])
    elif department == 'ENT (Ear, Nose, and Throat)':
        return random.choice(["Tonsillectomy", "Rhinoplasty", "Hearing aid fitting", "Sinus surgery", "Laryngoscopy"])
    elif department == 'Gynecology':
        return random.choice(["Prenatal care", "Hysterectomy", "Pelvic floor therapy", "Fertility treatments", "Cesarean section"])
    elif department == 'Radiology':
        return random.choice(["Radiography", "Fluoroscopy", "Mammography", "Nuclear medicine imaging", "Interventional radiology"])
    elif department == 'Endocrinology':
        return random.choice(["Diabetes management", "Thyroid hormone therapy", "Osteoporosis treatment", "Hormone replacement therapy", "Adrenal insufficiency management"])
    elif department == 'Pulmonology':
        return random.choice(["Pulmonary function tests", "Asthma management", "Chronic obstructive pulmonary disease (COPD) treatment", "Lung cancer therapy", "Bronchoscopy"])
    elif department == 'Hematology':
        return random.choice(["Blood transfusion", "Chemotherapy for blood disorders", "Anemia treatment", "Bleeding disorder management", "Hemophilia care"])
    elif department == 'Ophthalmology':
        return random.choice(["Cataract surgery", "Glaucoma treatment", "Retinal detachment repair", "Laser eye surgery", "Eye infection management"])
    elif department == 'Allergy and Immunology':
        return random.choice(["Allergy testing", "Immunotherapy", "Asthma management", "Autoimmune disease treatment", "Food allergy management"])
    elif department == 'Rheumatology':
        return random.choice(["Rheumatoid arthritis treatment", "Osteoarthritis management", "Lupus therapy", "Gout treatment", "Spondyloarthritis care"])
    elif department == 'Infectious Diseases':
        return random.choice(["Infectious disease diagnosis", "Antiviral treatment", "Antibiotic therapy", "Vaccination", "Travel medicine consultation"])
    elif department == 'Pathology':
        return random.choice(["Laboratory testing", "Biopsy analysis", "Disease diagnosis", "Cytology", "Histopathology"])
    elif department == 'Anesthesiology':
        return random.choice(["Anesthesia administration", "Pain management", "Sedation", "Regional anesthesia", "General anesthesia"])




for _ in range(num_to_generate):
    column_values = []

    for column_type in column_types:
        if column_type == "id":
            column_values.append(fake.unique.random_number(digits=6)) #constraint: mention the length of the id
        elif column_type == "name":
            first_name = fake.name()
            column_values.append(first_name)
            if first_name.endswith(('a', 'e','i')):
                gender = "Female"
            else:
                gender = "Male"

        elif column_type == "gender":
            column_values.append(gender)

        elif column_type == "address":
            column_values.append(fake.address())
        elif column_type == "age":
            column_values.append(fake.random_int(min=40, max=100)) # constraint min and max

        elif column_type == "admission_date":
            admission_date=fake.date_between(start_date='-1y', end_date='today')  #constraint start_date[-1y]
            column_values.append(admission_date)
        elif column_type == "discharge_date":
            column_values.append(fake.date_between(start_date=admission_date, end_date=admission_date + timedelta(days=30)))
                                                                                # constraint no.of days=30

        elif column_type == "phone_number":
            column_values.append(fake.phone_number())

        elif column_type == "department":
            department=fake.random_element(elements=departments)
            column_values.append(department)


        elif column_type == "bill_amount":
            column_values.append(round(random.uniform(1000.0, 10000.0), 2)) #constarint min and max
        elif column_type == "diagnosis":
            column_values.append(generate_diagnosis(department))
        elif column_type == "treatment":
            column_values.append(generate_treatment(department))
        elif column_type == "boolean":
            column_values.append(random.choice(["Yes",""]))



    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)


# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

ctgan.fit(df, column_names, epochs = 300)#ask epochs
samples = ctgan.sample(1000)
samples

from table_evaluator import load_data, TableEvaluator
table_evaluator = TableEvaluator(df, samples)
table_evaluator.evaluate(target_col='previous records')

table_evaluator.visual_evaluation()
