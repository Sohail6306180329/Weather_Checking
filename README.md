# 🌤️ Real-Time Weather Forecast App using Flask & OpenWeatherMap:

This project is a beautiful and responsive weather dashboard built using **Flask** and **OpenWeatherMap API**, allowing users to fetch real-time weather information by city name.

---

## 🔍 Overview:

Using Flask and OpenWeatherMap’s RESTful API, the app fetches live weather data including temperature, humidity, wind speed, pressure, and description. The UI is styled using CSS with modern **glassmorphism** effects to give it a polished look.

---

## 📁 Project Structure :

```
weather-app/
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

   
---

## 🚀 How It Works:

1. User enters a city name in the search field.
2. On form submission, Flask sends a GET request to OpenWeatherMap API.
3. API responds with weather data in JSON format.
4. Flask processes this data and renders it on `index.html`.
5. Weather info is shown with icon, temperature, humidity, wind speed, and pressure.
6. If the city is invalid or request fails, a friendly error message is shown.

---

## ⚙️ How to Run : 

### 1️⃣ Clone the repository:


git clone https://github.com/9ariz1/Weather_Checking-.git

cd Weather_Checking

### 2️⃣ Install required packages:

pip install flask requests

### 3️⃣ Replace API Key:
Open app.py and replace the API key string:

API_KEY = "5a945612ae9abfaa000d54d3c0ed0940"

### 4️⃣ Run the app:

python app.py


### 5️⃣ Open in browser:

http://127.0.0.1:5001/


### 🧠 Skills You Showcase :
🔥 Flask (Routing, Rendering, Handling POST requests)

⚡ API Integration (OpenWeatherMap)

🧠 Python programming

🎨 Frontend Design (HTML5 + CSS3, Glassmorphism)

🚨 Error handling & clean user feedback


### 📸 Output:

<img width="937" height="848" alt="Screenshot 2025-08-03 182611" src="https://github.com/user-attachments/assets/4acccacf-2945-4df1-b90f-9dd562a1bdd6" />

### 🌟 Future Scope:
🗺️ Auto-location based weather (Geolocation API)

🕒 5-day or hourly forecast

🌙 Dark Mode toggle

📱 PWA (Progressive Web App) support

### 🙋‍♂️ Author:
Made with ❤️ by MO ARIZ
