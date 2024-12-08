import os
import pandas as pd
from google.cloud import bigquery
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# Set your Google Cloud credentials if not already set
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/key.json'

# Your project ID
project_id = "vast-alcove-440701-e9"

# Initialize BigQuery client
client = bigquery.Client(project=project_id)

# Replace my_dataset and employee_table with the actual dataset and table names.
query = f"""
SELECT
  job_title,
  department,
  salary
FROM `{project_id}.my_dataset.employee_table`
WHERE salary IS NOT NULL
"""

df = client.query(query).to_dataframe()

# Prepare features and target
features = df[['job_title', 'department']]
target = df['salary'].astype(float)

X_train, X_test, y_train, y_test = train_test_split(features, target, 
                                                    test_size=0.2, 
                                                    random_state=42)

categorical_features = ['job_title', 'department']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)
    ]
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("R² Score:", r2)

# Predict on new data (example)
new_data = pd.DataFrame({
    'job_title': ['Engineer, petroleum'],
    'department': ['IT sales professional']
})

predicted_salary = model.predict(new_data)
print("Predicted Salary for new candidate:", predicted_salary[0])

# Writing predictions back to BigQuery (optional)
predictions_df = pd.DataFrame({
    'job_title': new_data['job_title'],
    'department': new_data['department'],
    'predicted_salary': predicted_salary
})

# Adjust dataset/table as needed
table_id = f"{project_id}.my_dataset.predictions"

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_APPEND"
)

load_job = client.load_table_from_dataframe(
    predictions_df, table_id, job_config=job_config
)
load_job.result()  # Wait for the job to complete.

print("Predictions uploaded to BigQuery table:", table_id)
