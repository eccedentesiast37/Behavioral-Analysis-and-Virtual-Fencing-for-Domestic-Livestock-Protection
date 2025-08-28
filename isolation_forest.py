import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel('Measurement cow 1.xls')

# Preprocessing
data['Time (s)'] = pd.to_datetime(data['Time (s)'], unit='s')
data['Acceleration Magnitude'] = np.sqrt(data['X (m/s^2)']**2 +
                                         data['Y (m/s^2)']**2 +
                                         data['Z (m/s^2)']**2)

features = ['X (m/s^2)', 'Y (m/s^2)', 'Z (m/s^2)', 'Acceleration Magnitude']
X_scaled = StandardScaler().fit_transform(data[features])

# Train Isolation Forest
model = IsolationForest(n_estimators=200, contamination=0.1, random_state=42)
data['Anomaly'] = model.fit_predict(X_scaled)
data['Is Anomaly'] = data['Anomaly'].apply(lambda x: 'Yes' if x == -1 else 'No')

print(data.head())
