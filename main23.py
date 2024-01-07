import requests

url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

# 修改查询参数为齐河县的信息
querystring = {"city": "Qihexian", "state": "Shandong", "country": "China"}

headers = {
    "X-RapidAPI-Key": "a917603d83msh07d39ae029b390ep17aa0cjsn9cb51c96fd2e",
    "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

weather_data = response.json()

# 从字典中提取信息
cloud_percentage = weather_data.get('cloud_pct', 'N/A')
temperature = weather_data.get('temp', 'N/A')
feels_like = weather_data.get('feels_like', 'N/A')
humidity = weather_data.get('humidity', 'N/A')
min_temperature = weather_data.get('min_temp', 'N/A')
max_temperature = weather_data.get('max_temp', 'N/A')
wind_speed = weather_data.get('wind_speed', 'N/A')
wind_degrees = weather_data.get('wind_degrees', 'N/A')
sunrise_timestamp = weather_data.get('sunrise', 'N/A')
sunset_timestamp = weather_data.get('sunset', 'N/A')

# 打印提取的信息
print(f"云覆盖百分比：{cloud_percentage}%")
print(f"温度：{temperature}°C")
print(f"体感温度：{feels_like}°C")
print(f"湿度：{humidity}%")
print(f"最低温度：{min_temperature}°C")
print(f"最高温度：{max_temperature}°C")
print(f"风速：{wind_speed} m/s")
print(f"风向：{wind_degrees}°")
print(f"日出时间：{sunrise_timestamp}")
print(f"日落时间：{sunset_timestamp}")
