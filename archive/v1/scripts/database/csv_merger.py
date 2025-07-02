import pandas as pd
import glob
import os
from scripts.config import CSV_DIR, COMBINED_CSV

def combine_csv_files():
    # Get all CSV files in the CSV_DIR directory
    csv_files = glob.glob(os.path.join(CSV_DIR, '*.csv'))
    
    # Ensure combined file is not included in the input
    csv_files = [file for file in csv_files if os.path.basename(file) != COMBINED_CSV]
    
    # Read and combine all CSV files
    dfs = []
    for file in csv_files:
        df = pd.read_csv(file)
        dfs.append(df)
    
    # Concatenate all dataframes
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Remove duplicate rows
    combined_df.drop_duplicates(inplace=True)
    
    # Save combined dataframe back to CSV_DIR
    output_path = os.path.join(CSV_DIR, COMBINED_CSV)
    combined_df.to_csv(output_path, index=False)
    
if __name__ == "__main__":
    combine_csv_files()
