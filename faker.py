pip install Faker

pip install ctgan

pip install mimesis

from faker import Faker

import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

import random
from faker import Faker
import pandas as pd
import re

# Create a Faker instance
fake = Faker('en_IN')

# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ["Employee Number", "First Name", "Last Name", "Gender", "Email",
                "Phone Number", "Address", "Department", "Position",
                "Salary", "Supervisor ID","custom"]
column_types = ["number", "first_name", "last_name", "gender", "email",
                "phone_number", "address","department", "job",
                "salary", "Numeric_Relation","Alpha Numeric"]
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

##categorical_features = [ "Gender", "Department", "Position"]
from ctgan import CTGAN
from datetime import datetime, timedelta

ctgan = CTGAN()

ctgan.fit(df, column_names, epochs = 200)
samples = ctgan.sample(10)
samples

"""#### excess info"""

import random
from faker import Faker
import pandas as pd

# Create a Faker instance with the specified locale
fake = Faker('en_IN')

# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ["Employee Number", "First Name", "Last Name", "Date of Birth", "Gender", "Prefix",
                "Phone Number", "Address", "Department", "Position",
                "Salary", "Supervisor ID"]
column_types = ["number", "first_name", "last_name", "birth_date", "gender", "prefix",
                "phone_number", "address", "department", "position",
                "salary", "supervisor_id"]

# Initialize an empty list to store synthetic data
synthetic_data = []
number = 1  # Initialize number here
birth_year = fake.random_int(min=1970, max=2000)

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
    # Initialize an empty list to store column values for one row
    column_values = []

    for column_type in column_types:
        if column_type == "number":
            column_values.append(number)
        elif column_type == "first_name":
            first_name = fake.first_name()
            column_values.append(first_name)
            # Generate gender based on the first name (modify this rule as needed)
            if first_name.endswith(('a', 'e')):
                gender = "Female"
                prefix = fake.prefix_female()
            else:
                gender = "Male"
                prefix = fake.prefix_male()
        elif column_type == "gender":
            column_values.append(gender)  # Add gender to the column_values list
        elif column_type == "prefix":
            column_values.append(prefix)
        elif column_type == "last_name":
            column_values.append(fake.last_name())
        elif column_type == "birth_date":
            column_values.append(generate_birth_date())
        elif column_type == "email":
            column_values.append(fake.email())
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
        elif column_type == "address":
            column_values.append(fake.street_address())
        elif column_type == "department":
            column_values.append(fake.random_element(elements=('HR', 'IT', 'Finance', 'Sales')))
        elif column_type == "position":
            column_values.append(fake.job())
        elif column_type == "salary":
            column_values.append(fake.random_int(min=30000, max=100000))
        elif column_type == "supervisor_id":
            column_values.append(None if number == 1 else random.randint(1, number - 1))

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

import re

def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted

# Take user input for the desired format
input_format = input("Enter the format (e.g., 'abc123'): ")

# Convert the format
formatted_format = convert_format(input_format)

for _ in range(5):
    print(fake.bothify(text= formatted_format))

import re
from faker import Faker

# Function to convert a user-provided format into '?' and '#'
def convert_format(input_format):
    # Replace letters with '?'
    formatted = re.sub(r'[a-zA-Z]', '?', input_format)
    # Replace numbers with '#'
    formatted = re.sub(r'[0-9]', '#', formatted)
    return formatted

# Take user input for the desired format
input_format = input("Enter the format (e.g., 'abc123'): ")

# Convert the format
formatted_format = convert_format(input_format)

# Create a list of letters you want to use in 'letters'
letters = ['A', 'B']

# Initialize a Faker instance
fake = Faker()

for _ in range(5):
    # Concatenate the letters into a single string
    letters_string = ''.join(letters)
    # Use the specified 'letters_string' in the 'fake.bothify' call
    generated_text = fake.bothify(text=formatted_format, letters=letters_string)
    print(generated_text)

"""### Hospital CODE"""

import random
from faker import Faker
from datetime import datetime, timedelta
import pandas as pd
import re

# Create a Faker instance
fake = Faker('en_IN')

# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ['Patient ID', 'Patient Name', 'Gender','Age', 'Phone Number', 'Admission Date',
                'Doctor Name', 'Department', 'Diagnosis', 'Treatment', 'Bill Amount','Previous Records','Discharge Date','Address']
column_types = ['id','name','gender','age','phone_number','admission_date','name','department',
                'diagnosis','treatment','bill_amount','boolean','discharge_date','address']

# Initialize an empty list to store synthetic data
synthetic_data = []

Gender=random.choice(['Male', 'Female'])
null_value=""
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
            first_name = fake.first_name()
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
            column_values.append(random.choice(["Yes",null_value]))



    # Create the data dictionary dynamically based on the column names and values
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)


# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

from ctgan import CTGAN
from datetime import datetime, timedelta

ctgan = CTGAN()

ctgan.fit(df, column_names, epochs = 200)
samples = ctgan.sample(100)
samples

"""### Insurance CODE"""

import random
from faker import Faker
from datetime import datetime, timedelta
from datetime import datetime
import pandas as pd

# Create a Faker instance
fake = Faker('en_IN')

# Take user input for the number of synthetic rows to generate
num_to_generate = int(input("Enter the number of rows to generate: "))

# Define the column names and column types
column_names = ['Policy ID', 'Policy Holder', 'Insurance Company', 'Coverage Type', 'Premium Amount',
                'Policy Start Date', 'Policy End Date', 'Claim Amount', 'Claim Date','DOB','Phone Number']
column_types = ['id', 'name', 'company', 'coverage_type', 'random_float','start_date','end_date',
                'claim_amount','claim_date','date_of_birth','phone_number']

# Initialize an empty list to store synthetic data
synthetic_data = []
has_claim = random.choice([True, False])


# Helper function to generate random claim information
def generate_claim_info(policy_start_date, policy_end_date):
    if has_claim:
        claim_date = fake.date_between(start_date=policy_start_date, end_date=policy_end_date)
        return claim_date
    else:
        return None


# Helper function to generate random claim information
def generate_claim_amount():
    if has_claim:
        claim_amount = round(random.uniform(100.0, 5000.0), 2)
        return  claim_amount
    else:
        return None

# List of Indian insurance companies
insurance_companies = [
    "Life Insurance Corporation of India (LIC)",
    "HDFC Ergo General Insurance",
    "ICICI Prudential Life Insurance",
    "Bajaj Allianz General Insurance",
    "SBI Life Insurance",
    "Tata AIG General Insurance",
    "Reliance General Insurance",
    "Max Life Insurance",
    "Birla Sun Life Insurance",
    "United India Insurance",
    "National Insurance Company",
    "Oriental Insurance",
    "Apollo Munich Health Insurance",
    "Star Health and Allied Insurance",
    "Future Generali India Insurance",
    "Kotak Mahindra Life Insurance",
    "L&T General Insurance",
    "Religare Health Insurance",
    "ICICI Lombard General Insurance",
    "DHFL Pramerica Life Insurance",
    "Aviva Life Insurance",
    "Royal Sundaram General Insurance",
    "Liberty General Insurance",
    "Edelweiss Tokio Life Insurance",
    "GoDigit General Insurance",
    "Kotak Mahindra General Insurance",
    "Raheja QBE General Insurance",
    "Universal Sompo General Insurance",
    "SBI General Insurance",
    "Tata AIA Life Insurance",
    "IDBI Federal Life Insurance",
    "Aviva Life Insurance",
    "Reliance Nippon Life Insurance",
    "IFFCO Tokio General Insurance",
    "Royal Sundaram General Insurance",
    "Universal Sompo General Insurance",
    "Star Union Dai-ichi Life Insurance",
    "Canara HSBC Oriental Bank of Commerce Life Insurance",
    "Cholamandalam MS General Insurance",
    "HDFC Ergo Health Insurance",
    "SBI General Insurance",
    "Cigna TTK Health Insurance",
]

# List of coverage types
coverage_types = [
    "Auto Insurance - Liability",
    "Auto Insurance - Comprehensive",
    "Health Insurance - Medical",
    "Health Insurance - Hospitalization",
    "Life Insurance - Term Life",
    "Life Insurance - Whole Life",
    "Property Insurance - Homeowners",
    "Property Insurance - Commercial",
    "Travel Insurance - Trip Cancellation",
    "Travel Insurance - Travel Medical",
    "Business Insurance - General Liability",
    "Business Insurance - Professional Liability"
]

for _ in range(num_to_generate):
    column_values = []

    for column_type in column_types:
        if column_type == "id":
            column_values.append(fake.unique.random_number(digits=6))
        elif column_type == "name":
            column_values.append(fake.name())
        elif column_type == "company":
            column_values.append(random.choice(insurance_companies))
        elif column_type == "coverage_type":
            column_values.append(random.choice(coverage_types))
        elif column_type == "date_of_birth":
            column_values.append(fake.date_of_birth(minimum_age=18, maximum_age=80))  # constraint enter min amd max age accordingly dob will be generated
        elif column_type == "phone_number":
            column_values.append(fake.phone_number())
        elif column_type == "random_float":
            column_values.append(round(random.uniform(500.0, 5000.0), 2)) #constraint enter min and max range
        elif column_type == "claim_date":
            column_values.append(generate_claim_info(start_date,end_date))
        elif column_type == "claim_amount":
            column_values.append(generate_claim_amount())
        elif column_type == "start_date":
            start_date=fake.date_between(start_date='-5y', end_date='today') #constraint enter start date[in the format'-5y']
            column_values.append(start_date)
        elif column_type == "end_date":
            end_date=fake.date_between(start_date, end_date='+2y') #constraint enter end date[in the format '+2y']
            column_values.append(end_date)

    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)

df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)

