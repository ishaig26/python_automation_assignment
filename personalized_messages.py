import pandas as pd

# Step 1: Load the cleaned data
df = pd.read_csv("cleaned_output.csv")

# Step 2: Function to generate message
def create_message(row):
    name = row['first_name'] if pd.notna(row['first_name']) else row['name']
    joined = row['has_joined_event']
    job = row['Job Title'] if pd.notna(row['Job Title']) else "professional"
    linkedin = str(row.get('What is your LinkedIn profile?', '')).strip()

    if joined == True:
        message = f"Hey {name}, thanks for joining our session! As a {job}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        message = f"Hi {name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job}."

    # Add LinkedIn comment if missing
    if not linkedin or "http" not in linkedin:
        message += " (P.S. Looks like we couldn’t find your LinkedIn. Want to stay connected?)"

    return message

# Step 3: Apply function to each row
df['message'] = df.apply(create_message, axis=1)

# Step 4: Save email + message to new CSV
df[['email', 'message']].to_csv("personalized_messages.csv", index=False)

#  Done!
print("Messages saved to 'personalized_messages.csv'")
