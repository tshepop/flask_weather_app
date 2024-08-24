from flask import Flask, flash, render_template, request, redirect, url_for
import requests
import pprint

import arrow

import config

app = Flask(__name__)
app.secret_key = config.APP_SECRET

API_KEY = config.API_KEY
# use string interpolation for url
API_URL = "https://api.openweathermap.org/data/2.5/forecast?q={0}&units=metric&appid={1}"


capitals = [
    "Ascension and Tristan da Cunha", "Abu Dhabi", "Abuja", "Accra",
    "Adamstown", "Addis Ababa", "Algiers", "Alofi", "Amman", "Amsterdam",
    "Andorra la Vella", "Ankara", "Antananarivo", "Apia", "Ashgabat", "Asmara", "Asunción", "Athens", "Avarua", "Baghdad", "Baku", "Bamako", "Bandar Seri Begawan", "Bangkok", "Bangui", "Banjul", "Basse-Terre", "Basseterre", "Beijing", "Beirut", "Belgrade", "Belmopan", "Berlin", "Bern", "Bishkek", "Bissau", "Bogotá", "Brades", "Brasília", "Bratislava", "Brazzaville", "Bridgetown", "Brussels", "Bucharest", "Budapest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Caracas", "Castries", "Cayenne", "Charlotte Amalie", "Chisinau", "Città del Vaticano", "Cockburn Town", "Colombo", "Conakry", "Concelho de Macau", "Copenhagen", "Dakar", "Damascus", "Dhaka", "Dili", "Djibouti", "Dodoma", "Doha", "Douglas", "Dublin", "Dushanbe", "El Aaiún or Laâyoune ", "Flying Fish Cove", "Fort-de-France", "Freetown", "Funafuti", "Gaborone", "George Town", "Georgetown", "Gibraltar", "Guatemala City", "Gustavia", "Hagåtña", "Hamilton", "Hanoi", "Harare", "Havana", "Helsinki", "Hong Kong", "Honiara", "Islamabad", "Jakarta", "Jerusalem", "Juba", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "King Edward Point", "Kingston", "Kingstown", "Kinshasa", "Kuala Lumpur", "Kuwait City", "Libreville", "Lilongwe", "Lima", "Lisbon", "Ljubljana", "Lomé", "London", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg", "Madrid", "Majuro", "Malabo", "Malé", "Mamoudzou", "Managua", "Manama", "Manila", "Maputo", "Mariehamn", "Marigot", "Maseru", "Mata-Utu", "Mbabane", "Mexico City", "Minsk", "Mogadishu", "Monaco", "Monrovia", "Montevideo", "Moroni", "Moscow", "Muscat", "Nairobi", "Nassau", "Nay Pyi Taw", "New Delhi", "Niamey", "Nicosia", "Nouakchott", "Nouméa", "Nuku'alofa", "Nursultan", "Nuuk", "N'Djamena", "Oranjestad", "Oslo", "Ottawa", "Ouagadougou", "Pago Pago", "Panama City", "Papeete", "Paramaribo", "Paris", "Philipsburg", "Phnom Penh", "Podgorica", "Port Louis", "Port Moresby", "Port-Vila", "Port-au-Prince", "Port-of-Spain", "Porto-Novo", "Prague", "Praia", "Pretoria", "Pristina", "Pyongyang", "Quito", "Rabat", "Ramallah", "Reykjavík", "Riga", "Riyadh", "Road Town", "Rome", "Roseau", "Saint George's", "Saint Helier", "Saint John's", "Saint Peter Port", "Saint-Denis", "Saint-Pierre", "Saipan", "San José", "San Juan", "San Marino", "San Salvador", "Sanaa", "Santiago", "Santo Domingo", "Sarajevo", "Seoul", "Singapore", "Skopje", "Sofia", "Stanley", "Stockholm", "Sucre", "Suva", "São Tomé", "Taipei", "Tallinn", "Tarawa", "Tashkent", "Tbilisi", "Tegucigalpa", "Tehran", "The Valley", "Thimphu", "Tirana", "Tokyo", "Tripoli", "Tunis", "Tórshavn", "Ulaanbaatar", "Vaduz", "Valletta", "Victoria", "Vienna", "Vientiane", "Vilnius", "Warsaw", "Washington", "Wellington", "West Island", "Willemstad", "Windhoek", "Yamoussoukro", "Yaoundé", "Yaren", "Yerevan", "Zagreb"
]


@app.route("/")
def home():
    """
   This function handles HTTP requests to the root URL ("/") of the web application.

   It returns an HTML template named "index.html" with a variable named "capital_city"
   that is populated with a list of capital cities.

   Parameters:
   None

   Returns:
   A rendered HTML template
   """
    return render_template("index.html",
                           capital_city=capitals)


@app.route("/weather", methods=("GET", "POST"))
def get_weather():
    """
    Handles HTTP requests to the "/get_weather" URL of the web application.

    If the request method is a POST, it retrieves the city name from the
    form input and submits a GET request to the OpenWeatherMap API.

    The API response is printed to the console using the pprint module.

    The function then renders the "weather.html" template and passes the API
    response as a variable named "results".

    Parameters:
        None

    Returns:
        A rendered HTML template
    """

    if request.method == "POST":
        # Get the city name from the form input
        city = request.form.get("city_name")

        if not city:
            flash("Please make a valid selection!")
            return redirect(url_for("home"))

        try:
            # Submit a GET request to the OpenWeatherMap API
            data = requests.get(API_URL.format(city, API_KEY))
            print(data.status_code)
            data.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            flash("Error fetching weather data")
            return redirect(url_for("home"))

        # Get the API response in JSON format
        response = data.json()

        # extract timezone
        timezone_offset = response["city"]["timezone"]
        # print(timezone_offset)

        # get utc
        utc_now = arrow.utcnow()
        # print(utc_now)

        # calculate the time for each chosen city
        # there are 3600 seconds in 1 hour
        offset_hours = timezone_offset / 3600
        # selected capital city local time
        local_time = utc_now.shift(hours=offset_hours)

        # test if correct time format is displayed
        if offset_hours > 0:
            offset_description = f"{int(offset_hours)} hours ahead of UTC"
        else:
            offset_description = f"{abs(int(offset_hours))} hours behind UTC"

        print(f"Local Time: {local_time.format('YYYY-MM-DD hh:mm:ss A')}")
        print(f"Timezone offset: {offset_description}\n")

        # format the time and year, before sending to template
        current_time = local_time.format('hh:mm A')
        current_date = local_time.format('YYYY-MM-DD')

        # Print the API response to the console
        # pprint.pprint(response)
        # print(type(response))

        # use arrow.get() to get dt from response,
        # get only midday temps for different days

        for d_time in response['list']:
            dt_time = d_time['dt']
            get_dt = arrow.get(dt_time)
            sliced_time = str(get_dt).split("T")[1]
            if sliced_time.startswith("12"):
                # print(d_time['main']['temp'])
                midday_temp = d_time['main']['temp']

    # Render the "weather.html" template with the API response as a variable
    return render_template("weather.html",
                           current_time=current_time,
                           current_date=current_date,
                           results=response,
                           local_time=local_time,
                           midday_temp=midday_temp)
