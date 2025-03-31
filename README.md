# Fortel
# **🌦 Weather Prediction System**  

A **Django-based** weather prediction system that uses **Machine Learning** to forecast **temperature** and **humidity** based on historical weather data. It also integrates real-time weather data using the **OpenWeather API**.  

---

## **🚀 Features**
✔ **Predicts** Maximum Temperature & Relative Humidity  
✔ **Uses Random Forest Regressor** for weather predictions  
✔ **Real-time weather forecasts** using OpenWeather API  
✔ **Django-based web application** with React frontend  
✔ **Interactive UI** for checking weather updates  

---

## **📂 Project Structure**
```
weather_predictor/
│── forecast/
│   │── migrations/
│   │── static/
│   │── templates/
│   │   └── weather.html
│   │── models.py
│   │── views.py  # Contains ML model & API integration
│   │── urls.py
│── weather_predictor/
│   │── settings.py
│   │── urls.py
│── FloodPrediction.csv  # Dataset for ML training
│── temp_model.pkl       # Trained ML model for temperature prediction
│── hum_model.pkl        # Trained ML model for humidity prediction
│── scaler.pkl           # StandardScaler for feature normalization
│── accuracy_scores.pkl  # Stores ML accuracy
│── manage.py
│── README.md
```

---

## **🔧 Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/weather-predictor.git
cd weather-predictor
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run Migrations**
```bash
python manage.py migrate
```

### **4️⃣ Start the Django Server**
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

---

## **🧠 Machine Learning Model**
The system trains two **Random Forest Regressor models** using the `FloodPrediction.csv` dataset:  
1️⃣ **Max Temperature Model**  
2️⃣ **Relative Humidity Model**  

✔ **Feature Scaling** is applied using `StandardScaler`.  
✔ **Random noise** is added to prevent overfitting.  
✔ Accuracy is **adjusted** if it exceeds 95% to prevent overconfidence.  



## **🌍 Real-Time Weather Forecast**
The system fetches real-time weather data from the **OpenWeather API**:
- **Max & Min Temperature**
- **Humidity**
- **Weather Description**
- **Wind Speed**
- **Rainfall Data**

### **🛠 API Integration**
```python
API_KEY = "your_openweather_api_key"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
weather_data = response.json()
```

---

## **📜 License**
This project is **open-source** and available under the **MIT License**.

---

## **🛠 Future Improvements**
- ✅ Add more weather parameters (Pressure, UV Index)  
- ✅ Improve **ML model accuracy** with hyperparameter tuning  
- ✅ Deploy using **Docker & AWS**  

---

