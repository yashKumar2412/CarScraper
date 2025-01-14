import re
import pandas as pd
from scripts.config import VOLVO_TEXT, VOLVO_CSV, VOLVO_IMG

volvo_data = []

# Load the data from files
with open(VOLVO_TEXT, 'r') as text_file, open(VOLVO_IMG, 'r') as img_file:
    for text_line, img_line in zip(text_file, img_file):
        text_line = text_line.strip()
        img_line = img_line.strip()

        entry = {
            "data": text_line,
            "image": img_line
        }

        volvo_data.append(entry)

# Define a function to extract data
def extract_deals(data, brand):
    deals = []

    for entry in data:
        deal_text = entry["data"]
        image_url = entry["image"]

        deal_texts = re.split(r'Lease Offer', deal_text)[1:]

        for deal in deal_texts:
            deal_dict = {"Brand": brand, "Image_URL": image_url}
            
            # Extract model - only proceed if we find a valid model
            model_match = re.search(r"(\d{4}\s+Volvo\s+[A-Z0-9]+(?:\s+[A-Za-z0-9]+)?(?:\s+[A-Za-z0-9]+)?)", deal)
            if model_match:
                deal_dict["Model"] = model_match.group(1).strip()
                
                # Extract monthly payment
                payment_match = re.search(r"\$(\d+)\s+/month", deal)
                if payment_match:
                    deal_dict["Monthly_Payment"] = float(payment_match.group(1))
                    
                # Extract lease term
                term_match = re.search(r"/month\s+(\d+)\s+mos", deal)
                if term_match:
                    deal_dict["Lease_Term"] = int(term_match.group(1))
                    
                # Extract due at signing
                due_match = re.search(r"\$([0-9,]+)\s+cash due at signing", deal)
                if due_match:
                    deal_dict["Due_at_Signing"] = float(due_match.group(1).replace(",",""))
                    
                # Extract MSRP - handle both formats
                msrp_match = re.search(r"\$([0-9,]+)\s+MSRP|MSRP\s+\$([0-9,]+)", deal)
                if msrp_match:
                    msrp_value = msrp_match.group(1) or msrp_match.group(2)
                    deal_dict["MSRP"] = float(msrp_value.replace(",", ""))

                    
                # Extract miles per year and cost per mile
                miles_match = re.search(r"(\d+,\d+)\s+miles/year at \$([0-9.]+)\s*/\s*mile", deal)
                if miles_match:
                    deal_dict["Miles_per_Year"] = int(miles_match.group(1).replace(",",""))
                    deal_dict["Excess_Mile_Fee"] = float(miles_match.group(2))
                    
                # Extract expiry date
                expiry_match = re.search(r"Expires\s+(\d{2}/\d{2}/\d{4})", deal)
                if expiry_match:
                    deal_dict["Offer_Ends"] = expiry_match.group(1)
                    
                # Extract lease bonus
                bonus_match = re.search(r"application of \$([0-9,]+)\s+Lease Bonus", deal)
                if bonus_match:
                    deal_dict["Lease_Bonus"] = float(bonus_match.group(1).replace(",",""))
                    
                # Extract drivetrain info (AWD/FWD)
                if "AWD" in deal:
                    deal_dict["Drivetrain"] = "AWD"
                elif "FWD" in deal:
                    deal_dict["Drivetrain"] = "FWD"
                    
                # Extract trim level
                trim_patterns = ["R-Design", "Momentum", "Cross Country"]
                for trim in trim_patterns:
                    if trim in deal:
                        deal_dict["Trim"] = trim
                        break
                
                # Only append if we have more than just the brand
                if len(deal_dict) > 1:
                    deals.append(deal_dict)
    
    return deals

# Extract data for Volvo
volvo_deals = extract_deals(volvo_data, "Volvo")

# Convert to DataFrame
df = pd.DataFrame(volvo_deals)

# Save to CSV
df.to_csv(VOLVO_CSV, index=False)
print("Data extraction completed. Saved as volvo_deals.csv")