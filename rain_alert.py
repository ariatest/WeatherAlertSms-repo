import requests
from ippanel import Client
import os
from dotenv import load_dotenv
load_dotenv()

# ========== API KEYS ==========
owm_api_key = os.environ.get("OWM_API_KEY")
sms_api_key = os.environ.get("IPPANEL_API_KEY")
recipient_number = os.environ.get("RECIPIENT_NUMBER")
url = "https://api.openweathermap.org/data/2.5/forecast"

# اعتبارسنجی کلیدها
if not owm_api_key or not sms_api_key:
    raise ValueError("🔒 کلیدهای API پیدا نشدند. لطفاً فایل .env را بررسی کنید.")
if not recipient_number:
    raise ValueError("📱 شماره گیرنده پیامک تعریف نشده. لطفاً متغیر RECIPIENT_NUMBER را در فایل .env اضافه کنید.")

# ========== موقعیت جغرافیایی تهران ==========
weather_params = {
    "lat": 35.689198,
    "lon": 51.388973,
    "appid": owm_api_key,
    #get data every 12 hour (3*4)
    "cnt": 4,
}

# ========== وضعیت‌های آب‌وهوا به فارسی ==========
weather_conditions_fa = {
    "thunderstorm": "طوفانی",
    "drizzle": "نم‌نم باران",
    "rain": "بارانی",
    "snow": "برفی",
    "atmosphere": "مه‌آلود یا گردوغبار",
    "clear": "صاف و آفتابی",
    "clouds": "ابری",
    "unknown": "نامشخص",
}
def get_weather_status(code):
    if 200 <= code < 300:
        return weather_conditions_fa["thunderstorm"]
    elif 300 <= code < 400:
        return weather_conditions_fa["drizzle"]
    elif 500 <= code < 600:
        return weather_conditions_fa["rain"]
    elif 600 <= code < 700:
        return weather_conditions_fa["snow"]
    elif 700 <= code < 800:
        return weather_conditions_fa["atmosphere"]
    elif code == 800:
        return weather_conditions_fa["clear"]
    elif 801 <= code <= 804:
        return weather_conditions_fa["clouds"]
    else:
        return weather_conditions_fa["unknown"]

# ========== گرفتن اطلاعات هوا ==========
response = requests.get(url,weather_params)
response.raise_for_status()

weather_data = response.json()
# print(response.json())

# ========== تحلیل وضعیت ==========
forecast_conditions = []
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

        forecast_conditions.append(get_weather_status(int(condition_code)))

forecast_conditions = list(set(forecast_conditions))  # حذف تکراری‌ها

# ========== ارسال پیام فقط در صورت نیاز ==========

if forecast_conditions:
    message = (
        "☁ هشدار هواشناسی:\n"
        f"در ساعات آینده، وضعیت هوا به صورت «{'، '.join(forecast_conditions)}» پیش‌بینی شده است.\n"
        "لطفاً برای خروج از منزل احتیاط کنید."
    )
    try:
        client = Client(sms_api_key)

        message_id = client.send(
            "+983000505",  # originator
            [recipient_number],  # recipients
            message,  # message
            "وضعیت آب و هوا"
        )
        print(f"✅ پیامک با موفقیت ارسال شد. ID: {message_id}")
    except Exception as e:
        print("❌ خطا در ارسال پیامک:", e)
else:
    print("✅ وضعیت هوا پایدار است، نیازی به ارسال پیام نیست.")