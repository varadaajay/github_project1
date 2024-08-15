import pandas as pd
# Load the data from the given URL
data_url = "https://raw.githubusercontent.com/arora123/Data/master/emp-data.csv"
df = pd.read_csv(data_url)

# 1. How many Males/Females are there in the entire organization?
gender_count = df['Gender'].value_counts()

# 2. How many Males/Females are there in each department or for each location?
gender_department_count = df.groupby(['Department', 'Gender'])['Gender'].count()
gender_location_count = df.groupby(['Location', 'Gender'])['Gender'].count()

# 3. For which department is the average Pay highest?
department_avg_salary = df.groupby('Department')['Salary'].mean()
highest_avg_salary_department = department_avg_salary.idxmax()

# 4. For which location is the average Pay highest?
location_avg_salary = df.groupby('Location')['Salary'].mean()
highest_avg_salary_location = location_avg_salary.idxmax()

# 5. What percentage of employees received good & very good rating? What about poor & very poor rating? and average rating?
rating_counts = df['Ratings'].value_counts()
total_employees = len(df)
good_and_very_good_percentage = (rating_counts[['Good', 'Very Good']].sum() / total_employees) * 100
poor_and_very_poor_percentage = (rating_counts[['Poor', 'Very Poor']].sum() / total_employees) * 100
average_rating = df['Ratings'].map({'Poor': 1, 'Very Poor': 1, 'Average': 2, 'Good': 3, 'Very Good': 3}).mean()

# 6. Compute gender pay gap for each department. Interpret
gender_pay_gap_department = df.groupby(['Department', 'Gender'])['Salary'].mean().unstack()
gender_pay_gap_department['Gender Pay Gap'] = gender_pay_gap_department['Male'] - gender_pay_gap_department['Female']

# 7. Compute gender pay gap for each location. Interpret
gender_pay_gap_location = df.groupby(['Location', 'Gender'])['Salary'].mean().unstack()
gender_pay_gap_location['Gender Pay Gap'] = gender_pay_gap_location['Male'] - gender_pay_gap_location['Female']

# Print the results
print("1. Gender distribution in the entire organization:")
print(gender_count)

print("\n2. Gender distribution by Department:")
print(gender_department_count)

print("\nGender distribution by Location:")
print(gender_location_count)

print("\n3. Department with the highest average salary:", highest_avg_salary_department)

print("\n4. Location with the highest average salary:", highest_avg_salary_location)

print("\n5. Percentage of employees with Good & Very Good ratings:", good_and_very_good_percentage)
print("Percentage of employees with Poor & Very Poor ratings:", poor_and_very_poor_percentage)
print("Average Rating:", average_rating)

print("\n6. Gender pay gap by Department:")
print(gender_pay_gap_department)

print("\n7. Gender pay gap by Location:")
print(gender_pay_gap_location)
