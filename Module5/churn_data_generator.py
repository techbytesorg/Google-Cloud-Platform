import pandas as pd
import random
import numpy as np
from faker import Faker

# Initialize Faker to create realistic fake data
fake = Faker()

def create_churn_data(num_rows):
    """Generates a DataFrame of synthetic customer churn data."""
    data = []
    
    # Define service options
    genders = ['Male', 'Female']
    yes_no = ['Yes', 'No']
    internet_services = ['DSL', 'Fiber optic', 'No']
    contracts = ['Month-to-month', 'One year', 'Two year']

    for _ in range(num_rows):
        # --- Basic Demographics ---
        gender = random.choice(genders)
        senior_citizen = random.choice([0, 1])
        partner = random.choice(yes_no)
        dependents = random.choice(yes_no)

        # --- Account Info ---
        tenure = random.randint(1, 72)
        contract = random.choice(contracts)

        # --- Service Info ---
        phone_service = random.choice(yes_no)
        internet_service = random.choice(internet_services)
        
        # --- Charges (correlated) ---
        # Base monthly charge
        if internet_service == 'Fiber optic':
            monthly_charges = random.uniform(70, 115)
        elif internet_service == 'DSL':
            monthly_charges = random.uniform(40, 70)
        else: # No internet
            monthly_charges = random.uniform(19, 25)
        
        # Add small charge for phone service
        if phone_service == 'Yes':
             monthly_charges += random.uniform(0, 10)
             
        # Total charges are correlated with tenure and monthly charges
        total_charges = (monthly_charges * tenure) + random.uniform(-50, 50)
        total_charges = round(max(monthly_charges, total_charges), 2) # Ensure total is at least monthly
        
        monthly_charges = round(monthly_charges, 2)

        # --- Target Variable (Churn) ---
        # We make churn more likely for certain groups to create patterns
        churn_prob = 0.26 # Base churn probability
        
        if contract == 'Month-to-month':
            churn_prob += 0.20
        if internet_service == 'Fiber optic':
            churn_prob += 0.10
        if tenure < 12:
            churn_prob += 0.15
        if tenure > 60:
            churn_prob -= 0.20
        
        # Ensure probability is between 0.05 and 0.95
        churn_prob = max(0.05, min(0.95, churn_prob))
        
        churn = 'Yes' if random.random() < churn_prob else 'No'
        
        # Add row to our data list
        data.append({
            'CustomerID': fake.unique.bothify(text='????-#####'),
            'Gender': gender,
            'SeniorCitizen': senior_citizen,
            'Partner': partner,
            'Dependents': dependents,
            'Tenure': tenure,
            'PhoneService': phone_service,
            'InternetService': internet_service,
            'Contract': contract,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges,
            'Churn': churn
        })

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

# --- How to Use the Script ---

# 1. Install required libraries (run this in your terminal or a notebook cell)
# pip install pandas faker

# 2. Generate the data (e.g., 1100 rows)
number_of_rows_to_generate = 1100
customer_data = create_churn_data(number_of_rows_to_generate)

# 3. Save to a CSV file to upload to Vertex AI
customer_data.to_csv('synthetic_churn_data.csv', index=False)

# 4. (Optional) Print the first 5 rows to check
print(f"Successfully generated {len(customer_data)} rows of data.")
print(customer_data.head())