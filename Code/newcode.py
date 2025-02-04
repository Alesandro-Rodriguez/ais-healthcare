import pandas as pd
#Identifying high risk counties with the no of disaster count 
file_path = r"C:\Users\Christopher Sequeira\Documents\GitHub\ais-healthcare\Data\DisasterDeclarationsSummaries.csv"
df1 = pd.read_csv(file_path)
disaster_counts = df1['designatedArea'].value_counts().reset_index()
disaster_counts.columns = ['designatedArea', 'disaster_count']

# Filter counties with high disaster frequencies (top 10% for now)
threshold = disaster_counts['disaster_count'].quantile(0.9)
high_risk_counties = disaster_counts[disaster_counts['disaster_count'] >= threshold]

# Display the high-risk counties
print(high_risk_counties)