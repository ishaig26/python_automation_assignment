import pandas as pd

# Step 1: Read the CSV file
# Make sure your file is named 'your_file.csv' or update the path accordingly
df = pd.read_csv("event_data.csv")

# Step 2: Remove duplicate rows based on email
df = df.drop_duplicates(subset='email')

# Step 3: Clean and convert 'has_joined_event' values from Yes/No → True/False
df['has_joined_event'] = df['has_joined_event'].str.strip().str.lower().map({'yes': True, 'no': False})

# Step 4: Mark rows where LinkedIn profile is missing or not starting with 'http'
df['linkedin_missing'] = df['What is your LinkedIn profile?'].isnull() | \
                         ~df['What is your LinkedIn profile?'].astype(str).str.startswith("http")

# Step 5: Mark rows where Job Title is missing or blank
df['job_title_missing'] = df['Job Title'].isnull() | (df['Job Title'].astype(str).str.strip() == '')

# Step 6: Save cleaned data into a new CSV file
df.to_csv("cleaned_output.csv", index=False)

print("✅ Cleaned data saved as 'cleaned_output.csv'")
