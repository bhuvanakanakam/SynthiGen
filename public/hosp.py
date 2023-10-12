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