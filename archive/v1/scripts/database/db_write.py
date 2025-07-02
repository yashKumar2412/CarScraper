import psycopg2
import pandas as pd
from scripts.config import COMBINED_CSV

# Database connection details
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'carscraper'
DB_USER = 'postgres'
DB_PASSWORD = 'nextmeal123'

# Read the CSV file into a DataFrame
data = pd.read_csv(COMBINED_CSV)

# Function to insert data into the database
def insert_data_to_db():
    try:
        # Establish connection
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        
        # Prepare the insert query
        insert_query = """
        INSERT INTO car_deals (
            Brand, Image_URL, Model, MSRP, Monthly_Payment, Due_at_Signing, Down_Payment,
            Bank_Fee, Total_Payments, Purchase_Option, Termination_Fee, 
            Excess_Mile_Fee, Miles_per_Year, Doc_Fee, Offer_Starts, Offer_Ends, 
            Lease_Term, Lease_Bonus, Drivetrain, Trim
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
        """
        
        # Iterate through the DataFrame and insert rows
        for _, row in data.iterrows():
            # Convert NaN to None for database insertion
            row = row.where(pd.notnull(row), None)
            cursor.execute(insert_query, (
                row['Brand'], row['Image_URL'], row['Model'], row['MSRP'], row['Monthly_Payment'],
                row['Due_at_Signing'], row['Down_Payment'], row['Bank_Fee'], 
                row['Total_Payments'], row['Purchase_Option'], row['Termination_Fee'],
                row['Excess_Mile_Fee'], row['Miles_per_Year'], row['Doc_Fee'], row['Offer_Starts'], row['Offer_Ends'], 
                row['Lease_Term'], row['Lease_Bonus'], row['Drivetrain'], row['Trim']
            ))
        
        # Commit the transaction
        conn.commit()
        print("Data inserted successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Execute the function
if __name__ == "__main__":
    insert_data_to_db()