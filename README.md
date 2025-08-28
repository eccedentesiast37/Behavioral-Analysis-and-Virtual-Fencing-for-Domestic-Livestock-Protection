# **1. Project Title**  
**Behavioral Analysis and Virtual Fencing for Domestic Livestock Protection**  

---

# **2. Overview**  
A comprehensive **IoT and ML-based livestock management system** that integrates:  
- GPS-based **virtual fencing**  
- IMU-based **behavioral monitoring**  
- **Anomaly detection** using ML models  
- Real-time **web dashboard** and **cloud integration (ThingSpeak)**  

---

# **3. System Architecture**  

- **Sensor Layer**: GPS module, MPU6050 IMU, buzzer  
- **Edge Computing Layer**: Raspberry Pi Pico W for data collection & Wi-Fi transmission  
- **Cloud/Application Layer**: WebSocket server, ThingSpeak cloud, browser-based dashboard with anomaly detection  

---

# **4. Core Components**  

- **Hardware (hardware/)**  
  - `pico_firmware/main.py` → Pico W firmware (GPS + IMU data collection)  
  - `sensor_data.py` → Reads MPU6050 + GPS data  
  - `websocket_server.py` → Data streaming to clients  

- **Software (software/anomaly_detection/)**  
  - `isolation_forest.py` → Isolation Forest anomaly detection  
  - `one_class_svm.py` → One-Class SVM model  
  - `autoencoder.py` → Autoencoder + Hybrid models  

- **Web Interface (web_interface/)**  
  - `index.html` → Real-time dashboard UI  
  - `map.js` → Leaflet.js map & geofencing  
  - `styles.css` → Dashboard styling  
  - `routes.py` → Flask WebSocket integration  

---

# **5. Key Features**  

- **Virtual Fencing**  
  - GPS-based geofence boundary detection  
  - Configurable radius (user input)  
  - Buzzer alerts on boundary crossing  

- **Behavioral Monitoring**  
  - Real-time IMU data (X, Y, Z accelerations)  
  - Preprocessing + feature extraction (acceleration magnitude)  

- **Machine Learning Models**  
  - Isolation Forest → Detects outliers in motion patterns  
  - One-Class SVM → Classifies abnormal behavior  
  - Autoencoder (Hybrid) → Deep learning-based anomaly detection  

- **Real-Time Dashboard**  
  - Leaflet.js map for tracking  
  - Interactive virtual fence setup  
  - Plotly.js sensor data visualization  

- **Cloud Integration**  
  - ThingSpeak cloud for long-term storage  
  - CSV export for offline analysis  

---

# **6. Technical Implementation**  

- **Backend Services**  
  - `sensor_data.py` → Collects IMU + GPS readings  
  - `websocket_server.py` → Broadcasts data to clients  

- **ML Pipeline**  
  - Preprocessing (scaling, normalization)  
  - Feature extraction (acceleration magnitude)  
  - Model inference (IF, OCSVM, Autoencoder)  
  - Anomaly labeling & visualization  

- **Web Dashboard**  
  - Real-time livestock tracking (Leaflet.js)  
  - User-defined geofencing  
  - WebSocket-driven live updates  

---

# **7. Data Flow**  

- **Data Collection**: IMU (X, Y, Z), GPS (Lat, Lng)  
- **Processing**: Normalization, feature extraction, ML inference  
- **Output**:  
  - WebSocket → Dashboard  
  - Buzzer → Alerts on geofence breach  
  - Cloud → ThingSpeak storage  

---

# **8. Security & Reliability**  

- Encrypted WebSocket communication (TLS-ready)  
- Data validation & error handling  
- Fault tolerance via periodic sampling  
- Logging for debugging and monitoring  

---

# **9. Testing & Validation**  

- **Geofencing**: GPS simulation tests  
- **Anomaly detection**: Validated with livestock accelerometer data  
- **Dashboard**: Stress-tested with real-time WebSocket updates  

**Performance Metrics:**  
- Sampling rate: 5 seconds  
- Detection latency: < 1 second  
- Battery runtime: ~10 hours (wearable collar)  

---

# **10. Future Enhancements**  

- 🛰 LoRaWAN integration for long-range communication  
- 📱 Mobile app for farmers (offline + online support)  
- 🌦 Weather-based predictive alerts  
- 🐑 Multi-species compatibility (sheep, goats, etc.)  
- ☁️ Cloud ML pipelines for scaling  

---

# **11. Installation & Setup**  

- **Prerequisites**  
  - Python 3.8+  
  - Raspberry Pi Pico W with MicroPython  
  - GPS NEO-6M, MPU6050, Buzzer  

- **Hardware**  
  ```bash
  cd hardware
  pip install -r requirements.txt
  python websocket_server.py

# **12. Contibuters**  

  - Daksh Mehta 
  - Chiraag Habbu 
  - Anish Adithya M A 
