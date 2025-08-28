import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM

# Load dataset
data = pd.read_excel('Measurement cow 1.xls')

# Preprocessing
data['Time (s)'] = pd.to_datetime(data['Time (s)'])
data['Acceleration Magnitude'] = np.sqrt(data['X (m/s^2)']**2 +
                                         data['Y (m/s^2)']**2 +
                                         data['Z (m/s^2)']**2)

features = ['X (m/s^2)', 'Y (m/s^2)', 'Z (m/s^2)', 'Acceleration Magnitude']
X_scaled = StandardScaler().fit_transform(data[features])

# Train One-Class SVM
model = OneClassSVM(nu=0.1, kernel='rbf', gamma='scale')
data['Anomaly'] = model.fit_predict(X_scaled)
data['Is Anomaly'] = data['Anomaly'].apply(lambda x: 'Yes' if x == -1 else 'No')

print(data.head())
