import re
import pandas as pd
from scripts.config import AUDI_TEXT, AUDI_CSV, AUDI_IMG

audi_data = []

# Load the data from files
with open(AUDI_TEXT, 'r') as text_file, open(AUDI_IMG, 'r') as img_file:
    for text_line, img_line in zip(text_file, img_file):
        text_line = text_line.strip()
        img_line = img_line.strip()

        entry = {
            "data": text_line,
            "image": img_line
        }

        audi_data.append(entry)

# Define a function to extract data
def extract_deals(data, brand):
    deals = []
     
    for entry in data:
        deal_text = entry["data"]
        image_url = entry["image"]

        deal_texts = deal_text.split("Find Your Audi")[:-1]

        for deal in deal_texts:
            deal_dict = {"Brand": brand, "Image_URL": image_url}
            
            model_match = re.search(r"(\d{4}\s+Audi\s+[A-Z0-9]+.*?)(?:\s+Price|â€‹)", deal)
            if model_match:
                deal_dict["Model"] = model_match.group(1)
                
            # Extract MSRP
            msrp_match = re.search(r"MSRP\s+\$([0-9,]+)", deal)
            if msrp_match:
                deal_dict["MSRP"] = float(msrp_match.group(1).replace(",",""))
                
            # Extract monthly payment
            payment_match = re.search(r"\$(\d+,{0,1}\d*)\s+1\s*st\s+mo\.\s+pymt", deal)
            if payment_match:
                deal_dict["Monthly_Payment"] = float(payment_match.group(1).replace(",",""))
                
            # Extract due at signing
            due_match = re.search(r"\$([0-9,]+)\s+due at signing", deal)
            if due_match:
                deal_dict["Due_at_Signing"] = float(due_match.group(1).replace(",",""))
                
            # Extract down payment
            down_match = re.search(r"\$([0-9,]+)\s+down\s+pymt", deal)
            if down_match:
                deal_dict["Down_Payment"] = float(down_match.group(1).replace(",",""))
                
            # Extract bank fee
            bank_match = re.search(r"\$([0-9]+)\s+bank\s+fee", deal)
            if bank_match:
                deal_dict["Bank_Fee"] = float(bank_match.group(1))
                
            # Extract total payments
            total_match = re.search(r"Ttl\s+pmts/purch\s+option\s+\$([0-9,]+)", deal)
            if total_match:
                deal_dict["Total_Payments"] = float(total_match.group(1).replace(",",""))
                
            # Extract purchase option
            purchase_match = re.search(r"pmts/purch\s+option\s+\$[0-9,]+/+\${0,1}([0-9,]+)", deal)
            if purchase_match:
                deal_dict["Purchase_Option"] = float(purchase_match.group(1).replace(",",""))
                
            # Extract termination fee
            term_match = re.search(r"Lease\s+end\s+termination\s+fee,\s+\$([0-9]+)", deal)
            if term_match:
                deal_dict["Termination_Fee"] = float(term_match.group(1))
                
            # Extract excess mileage fee
            mile_fee_match = re.search(r"excess\s+miles\s+charged\s+\$([0-9.]+)\.", deal)
            if mile_fee_match:
                deal_dict["Excess_Mile_Fee"] = float(mile_fee_match.group(1))
                
            # Extract miles per year
            miles_match = re.search(r"Based on\s+([0-9,]+)\s+miles per year", deal)
            if miles_match:
                deal_dict["Miles_per_Year"] = int(miles_match.group(1).replace(",",""))
                
            # Extract expiry date
            expiry_match = re.search(r"Offer expires\s+(\d{1,2}/\d{1,2}/\d{2,4})", deal)
            if expiry_match:
                deal_dict["Expiry_Date"] = expiry_match.group(1)
                
            # Extract doc fee
            doc_match = re.search(r"\$([0-9]+)\s+doc\s+fee", deal)
            if doc_match:
                deal_dict["Doc_Fee"] = float(doc_match.group(1))
                
            deals.append(deal_dict)

    return deals

# Extract data for Audi
audi_deals = extract_deals(audi_data, "Audi")

# Convert to DataFrame
df = pd.DataFrame(audi_deals)

# Save to CSV
df.to_csv(AUDI_CSV, index=False)
print("Data extraction completed. Saved as audi_deals.csv")