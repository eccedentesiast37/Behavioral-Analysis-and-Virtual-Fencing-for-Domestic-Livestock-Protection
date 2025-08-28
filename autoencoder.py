import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load dataset
data = pd.read_excel("Cowwwww2 2025-05-12 21-25-35.xls")

# Preprocessing
data['Acceleration Magnitude'] = np.sqrt(data['X (m/s^2)']**2 +
                                         data['Y (m/s^2)']**2 +
                                         data['Z (m/s^2)']**2)
features = ['X (m/s^2)', 'Y (m/s^2)', 'Z (m/s^2)', 'Acceleration Magnitude']
X_scaled = StandardScaler().fit_transform(data[features])

# Train Isolation Forest + OCSVM
iso_forest = IsolationForest(n_estimators=200, contamination=0.1, random_state=42)
data['Anomaly_IF'] = iso_forest.fit_predict(X_scaled)

ocsvm = OneClassSVM(nu=0.05, kernel='rbf', gamma='scale')
data['Anomaly_OCSVM'] = ocsvm.fit_predict(X_scaled)

# Define Autoencoder
def build_autoencoder(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_dim,)),
        Dense(32, activation='relu'),
        Dense(64, activation='relu'),
        Dense(input_dim, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# Train Autoencoder on IF-cleaned data
normal_if = X_scaled[data['Anomaly_IF'] == 1]
autoencoder_if = build_autoencoder(X_scaled.shape[1])
autoencoder_if.fit(normal_if, normal_if, epochs=12, batch_size=64, validation_split=0.1)

# Train Autoencoder on OCSVM-cleaned data
normal_ocsvm = X_scaled[data['Anomaly_OCSVM'] == 1]
autoencoder_ocsvm = build_autoencoder(X_scaled.shape[1])
autoencoder_ocsvm.fit(normal_ocsvm, normal_ocsvm, epochs=12, batch_size=64, validation_split=0.1)

print("Autoencoder training completed.")
