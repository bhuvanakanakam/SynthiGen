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
            start_date=fake.date_between(start_date='-5y', end_date='today') #constraint start date[-5y]
            column_values.append(start_date)                                   
        elif column_type == "end_date":
            end_date=fake.date_between(start_date, end_date='+2y') #constraint enter end[+2y]
            column_values.append(end_date)                                     
    
    data = {}
    for column_name, column_value in zip(column_names, column_values):
        data[column_name] = column_value

    synthetic_data.append(data)

df = pd.DataFrame(synthetic_data)

# Display the data in a table
print(df)