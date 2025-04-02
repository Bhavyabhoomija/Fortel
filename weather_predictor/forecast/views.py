from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import requests

#  1 Load and Prepare the Dataset

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of views.py
csv_path = os.path.join(BASE_DIR, "FloodPrediction.csv")

df = pd.read_csv(csv_path)



features = ['Year', 'Month', 'Max_Temp', 'Min_Temp', 'Rainfall', 
            'Relative_Humidity', 'Wind_Speed', 'Cloud_Coverage', 'LATITUDE', 'LONGITUDE']
target_temp = 'Max_Temp'
target_hum = 'Relative_Humidity'


missing_features = [col for col in features if col not in df.columns]
if missing_features:
    print(" Error: Missing Columns →", missing_features)
else:
    print(" All required columns exist!")


X = df[features]
y_temp = df[target_temp]
y_hum = df[target_hum]

# Standardize Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_temp_train, y_temp_test = train_test_split(X_scaled, y_temp, test_size=0.2, random_state=42)
_, _, y_hum_train, y_hum_test = train_test_split(X_scaled, y_hum, test_size=0.2, random_state=42)

#  Train ML Models
temp_model = RandomForestRegressor(n_estimators=100, random_state=42)
hum_model = RandomForestRegressor(n_estimators=100, random_state=42)

temp_model.fit(X_train, y_temp_train)
hum_model.fit(X_train, y_hum_train)

print(" Model training completed!")

# Save Models
joblib.dump(temp_model, "temp_model.pkl")
joblib.dump(hum_model, "hum_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print(" Model files saved successfully!")

ICON_MAPPING = {
    "clear sky": "clear",
    "few clouds": "cloudy",
    "scattered clouds": "cloudy",
    "broken clouds": "cloudy",
    "shower rain": "rain",
    "rain": "rain",
    "thunderstorm": "storm",
    "snow": "snow",
    "mist": "fog"
}

def weather_view(request):
    predictions = []
    city = None  # Default city to None

    if request.method == 'POST':
        city = request.POST.get('city')
        API_KEY = "34867051fa8c67abe440e6e8386596c3"
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()

            # Extract next 5 days' forecast (every 24 hours)
            for i in range(0, 40, 8):
                day_data = weather_data['list'][i]
                predictions.append({
                    "date": day_data['dt_txt'].split()[0],
                    "max_temp": day_data['main']['temp_max'],
                    "min_temp": day_data['main']['temp_min'],
                    "humidity": day_data['main']['humidity'],
                    "description": day_data['weather'][0]['description'],
                    "wind_speed": day_data['wind']['speed'],
                    "rain": day_data.get('rain', {}).get('3h', 0),
                    "icon": ICON_MAPPING.get(day_data['weather'][0]['description'], "default")
                })

    return render(request, "forecast/weather.html", {"city": city, "predictions": predictions})
def chatbot(request):
    return render(request, 'chatbot1/chat.html')
