import pandas as pd

# Load the original CSV file
df = pd.read_csv('Crash_Data.csv')

# Use the 'groupby' function to group the data by the 'state' column and count the occurrences
state_counts = df['state'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']

# Save the results to a new CSV file
state_counts.to_csv('state_counts.csv', index=False)