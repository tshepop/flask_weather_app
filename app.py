from flask import Flask, render_template, request, redirect, url_for
import requests
import pprint

import config

app = Flask(__name__)

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


@app.route("/get_weather", methods=("GET", "POST"))
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
        city = request.form["city_name"]

        # Submit a GET request to the OpenWeatherMap API
        data = requests.get(API_URL.format(city, API_KEY))

        # Get the API response in JSON format
        resp = data.json()

        # Print the API response to the console
        pprint.pprint(resp)

    # Render the "weather.html" template with the API response as a variable
    return render_template("weather.html",
                           results=resp)
