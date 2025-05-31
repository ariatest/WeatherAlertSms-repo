# Weather Alert via SMS

This project provides weather alerts via SMS. It uses the OpenWeatherMap API to get weather forecasts and sends SMS notifications using the IPPanel API if certain weather conditions (like rain, snow, or thunderstorms) are expected.

## 🚀 Features:
- Retrieves weather data for the next 12 hours from OpenWeatherMap API.
- Translates weather conditions into Persian.
- Sends an SMS alert using the IPPanel API if any significant weather event (like rain or snow) is predicted.
- Easy to configure with `.env` for API keys.

## 📦 Setup

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/AriaAramesh/WeatherAlertSms-repo.git
    ```

2. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file to store your API keys. You can get the API keys from:
   - [OpenWeatherMap API key](https://home.openweathermap.org/api_keys)
   - [IPPanel API key](https://ippanel.com)
   
   Add the keys to your `.env` file:
    ```env
    OWM_API_KEY=your_openweathermap_api_key
    IPPANEL_API_KEY=your_ippanel_api_key
    RECIPIENT_NUMBER=your_phone_number
    ```

4. Run the script.
    ```bash
    python rain_alert.py
    ```

## 📲 SMS Sample:
<img src="preview.png" alt="Weather Alert Example" width="600"/>

## 🛡 License

This project is provided for **personal and educational use only**.  
Commercial use, redistribution, or publishing any part of the code without permission is **strictly prohibited**.

For other use cases, please contact the author.
