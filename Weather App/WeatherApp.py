import pip._vendor.requests
import calendar
API_KEY = #Retrieve from https://openweathermap.org/api 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ADD_URL = "http://api.openweathermap.org/data/2.5/forecast"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
request_url1 = f"{ADD_URL}?appid={API_KEY}&q={city}"
response = pip._vendor.requests.get(request_url)
response1 = pip._vendor.requests.get(request_url1)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    fahrenheit = round(temperature *1.80000 +32,2)

    print("Current Weather condition:", weather)
    print("Current Temperature:", temperature, "celsius", fahrenheit, "fahrenheit" )
if response1.status_code == 200:
    data1 = response1.json()
    location_data = {
        'city': data1['city']['name'],
        'country': data1['city']['country']
    }
    print('\n{city}, {country}'.format(**location_data))
    
    current_date = ''
    for item in data1['list']:
        # Time of the weather data received, partitioned into 3 hour blocks
        time = item['dt_txt']

        # Split the time into date and hour [2018-04-15 06:00:00]
        next_date, hour = time.split(' ')

        # Stores the current date and prints it once
        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('\n{m}/{d}/{y}'.format(**date))
        
        # Grabs the first 2 integers from our HH:MM:SS string to get the hours
        hour = int(hour[:2])

        # Sets the AM (ante meridiem) or PM (post meridiem) period
        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        # Prints the hours [HH:MM AM/PM]
        print('\n%i:00 %s' % (hour, meridiem))

        # Temperature is measured in Kelvin
        temperature = item['main']['temp']

        # Weather condition
        description = item['weather'][0]['description'],

        # Prints the description as well as the temperature in Celcius and Farenheit
        print('Weather condition: %s' % description)
        print('Celcius: {:.2f}'.format(temperature - 273.15))
        print('Farenheit: %.2f' % (temperature * 9/5 - 459.67))
        # Prints a calendar of the current month
    calendar = calendar.month(int(year), int(month))
    print('\n'+ calendar)

else:
    print("An error occurred. ErrorCode: ")+ str(response.status_code)
