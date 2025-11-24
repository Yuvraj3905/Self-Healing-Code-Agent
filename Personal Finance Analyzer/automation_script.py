import pandas as pd
import glob
import os

# --- PART 1: The Cleaning Function ---
# We wrap our previous logic here. We can now apply this to ANY dataframe.
def clean_bank_data(df):
    # 1. Fix Dates
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 2. Standardize Descriptions
    df['Description'] = df['Description'].str.lower()
    
    # 3. Categorize (The logic we built earlier)
    def categorize(row):
        desc = row['Description']
        if pd.notna(row['Category']): 
            return row['Category']
        if 'starbucks' in desc: return 'Food & Drink'
        elif 'uber' in desc: return 'Transport'
        elif 'amazon' in desc: return 'Shopping'
        else: return 'Misc'

    df['Category'] = df.apply(categorize, axis=1)
    
    # 4. Fix Amounts (Make absolute)
    df['Amount'] = df['Amount'].abs()
    
    return df

# --- PART 2: The Automation Engine ---

# 1. Find all CSV files in the 'my_statements' folder
# The *.csv pattern means "anything ending in .csv"
files = glob.glob('my_statements/*.csv')

print(f"Found {len(files)} files to process.")

all_data_frames = []

# 2. Loop through every file found
for file in files:
    print(f"Processing: {file}")
    
    # Read the raw file
    raw_df = pd.read_csv(file)
    
    # Clean it using our function from Part 1
    cleaned_df = clean_bank_data(raw_df)
    
    # Add it to our list
    all_data_frames.append(cleaned_df)

# 3. Combine (Concatenate) all data into one Master DataFrame
if all_data_frames:
    master_df = pd.concat(all_data_frames, ignore_index=True)

    # --- CRITICAL STEP: Remove Duplicates ---
    # If you download statements that overlap (e.g., Jan 1-31, then Jan 15-Feb 15),
    # you will have duplicates. This fixes that.
    master_df = master_df.drop_duplicates()

    print("\n--- Processing Complete ---")
    print(f"Total Transactions: {len(master_df)}")
    
    # 4. Show the Summary
    print("\nTotal Spending by Category (All Files):")
    print(master_df.groupby('Category')['Amount'].sum())
    
    # Optional: Save the master report to a new file
    master_df.to_csv('Master_Financial_Report.csv', index=False)
    print("\nMaster report saved to 'Master_Financial_Report.csv'")

else:
    print("No CSV files found in the folder!")