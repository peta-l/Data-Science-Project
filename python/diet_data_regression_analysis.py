import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Get the path to the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct the path to the CSV file
csv_file_path = os.path.join(script_dir, '..', 'data', 'dietdata.csv')

# Resolve the full absolute path
csv_file_path = os.path.abspath(csv_file_path)

# Load data into a DataFrame
data = pd.read_csv(csv_file_path)

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Convert categorical variables to binary
data['exercise'] = data['exercise'].apply(lambda x: 1 if x == 'Yes' else 0)
data['walk'] = data['walk'].apply(lambda x: 1 if x == 'Yes' else 0)
data['run'] = data['run'].apply(lambda x: 1 if x == 'Yes' else 0)

# Define independent variables and dependent variable
X = data[['calories', 'exercise', 'walk', 'run']]
y = data['weight_dif_in_g']

# Add constant to the model (intercept)
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Print the summary of the model
print(model.summary())

# Add model predictions to the DataFrame for plotting
data['predicted_weight_diff'] = model.predict(X)

# Plotting the actual vs predicted weight difference over time
plt.figure(figsize=(14, 8))

# Plot actual weight differences
plt.plot(data['Date'],
         data['weight_dif_in_g'],
         label='Actual Weight Difference',
         color='blue',
         marker='o')

# Plot predicted weight differences
plt.plot(data['Date'],
         data['predicted_weight_diff'],
         label='Predicted Weight Difference',
         color='red',
         linestyle='--')

plt.title('Actual vs Predicted Weight Difference Over Time')
plt.xlabel('Date')
plt.ylabel('Weight Difference (in g)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot with regression line for calories vs weight difference
plt.figure(figsize=(10, 6))
sns.regplot(x='calories',
            y='weight_dif_in_g',
            data=data,
            ci=None,
            line_kws={"color": "red"})
plt.title('Regression of Weight Difference on Calories')
plt.xlabel('Calories')
plt.ylabel('Weight Difference (in g)')
plt.show()
