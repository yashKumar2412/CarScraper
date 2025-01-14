import re
import pandas as pd
from scripts.config import HONDA_TEXT, HONDA_IMG,HONDA_CSV

honda_data = []
# Load the data from the file
with open(HONDA_TEXT, 'r') as text_file, open(HONDA_IMG, 'r') as img_file:
    for text_line, img_line in zip(text_file, img_file):
        text_line = text_line.strip()
        img_line = img_line.strip()

        entry = {
            "data": text_line,
            "image": img_line
        }

        honda_data.append(entry)

# Define a function to extract structured data
def extract_honda_deals(data, brand="Honda"):
    deals = []

    for entry in data:
        deal_text = entry["data"]
        image_url = entry["image"]

        # Split deals using a robust delimiter
        deal_texts = re.split(r"\nNew \d{4} Honda", deal_text)

        for deal in deal_texts:
            deal_dict = {"Brand": brand, "Image_URL": image_url}

            # Extract model name with optional trim and drivetrain
            model_match = re.search(r"(New \d{4} Honda [A-Za-z0-9-]+(?: [A-Za-z0-9]+)*(?: AWD| FWD| Sedan)?)(?=\sOffer valid)", deal)
            if model_match:
                deal_dict["Model"] = model_match.group(1).strip()
            else:
                deal_dict["Model"] = "Unknown Model"

            # Extract offer period
            offer_period_match = re.search(r"Offer valid on ([\d/]+) through ([\d/]+)", deal)
            if offer_period_match:
                deal_dict["Offer_Starts"] = offer_period_match.group(1)
                deal_dict["Offer_Ends"] = offer_period_match.group(2)

            # Extract monthly payment
            payment_match = re.search(r"\$(\d+) a month for (\d+) months", deal)
            if payment_match:
                deal_dict["Monthly_Payment"] = float(payment_match.group(1))
                deal_dict["Lease_Term"] = int(payment_match.group(2))

            # Extract due at signing
            due_match = re.search(r"\$(\d{1,3}(?:,\d{3})*) due at signing", deal)
            if due_match:
                deal_dict["Due_at_Signing"] = float(due_match.group(1).replace(",", ""))

            # Extract MSRP
            msrp_match = re.search(r"MSRP \(vehicle\) .*?\$([\d,]+)", deal)
            if msrp_match:
                deal_dict["MSRP"] = float(msrp_match.group(1).replace(",", ""))

            # Extract purchase option
            purchase_match = re.search(r"Option to purchase at lease end \$(\d{1,3}(?:,\d{3})*)", deal)
            if purchase_match:
                deal_dict["Purchase_Option"] = float(purchase_match.group(1).replace(",", ""))

            # Extract excess mileage fee and miles per year
            mileage_match = re.search(r"up to (\d{1,3}(?:\.\d{1,2})?)\s*(?:Â¢|¢)/mi\.?\s+over\s+(\d{1,3}(?:,\d{3})*) miles/year", deal)
            if mileage_match:
                deal_dict["Excess_Mile_Fee"] = float(mileage_match.group(1)) / 100  # Convert cents to dollars
                deal_dict["Miles_per_Year"] = int(mileage_match.group(2).replace(",", ""))

            # Append only if meaningful data is extracted
            if len(deal_dict) > 2:  # Ensure we have more than just brand and image
                deals.append(deal_dict)

    return deals

# Extract deals
honda_deals = extract_honda_deals(honda_data)

# Convert to DataFrame
df = pd.DataFrame(honda_deals)

# # Remove duplicate rows
# df.drop_duplicates(subset=["Model", "Monthly_Payment", "Lease_Term"], inplace=True)

# # Validate missing models
# missing_models = df[df["Model"] == "Unknown Model"]
# if not missing_models.empty:
#     print("Warning: Some deals have missing models:")
#     print(missing_models)

# Save to CSV
df.to_csv(HONDA_CSV, index=False)
print(f"Data extraction completed. Saved as {HONDA_CSV}")