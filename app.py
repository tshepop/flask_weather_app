from flask import Flask, render_template
import arrow

app = Flask(__name__)

API_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&cnt=5&appid={}"

capitals = [
    "Ascension and Tristan da Cunha", "Abu Dhabi", "Abuja", "Accra",
    "Adamstown", "Addis Ababa", "Algiers", "Alofi", "Amman", "Amsterdam",
    "Andorra la Vella", "Ankara", "Antananarivo", "Apia", "Ashgabat", "Asmara", "Asunción", "Athens", "Avarua", "Baghdad", "Baku", "Bamako", "Bandar Seri Begawan", "Bangkok", "Bangui", "Banjul", "Basse-Terre", "Basseterre", "Beijing", "Beirut", "Belgrade", "Belmopan", "Berlin", "Bern", "Bishkek", "Bissau", "Bogotá", "Brades", "Brasília", "Bratislava", "Brazzaville", "Bridgetown", "Brussels", "Bucharest", "Budapest", "Buenos Aires", "Bujumbura", "Cairo", "Canberra", "Caracas", "Castries", "Cayenne", "Charlotte Amalie", "Chisinau", "Città del Vaticano", "Cockburn Town", "Colombo", "Conakry", "Concelho de Macau", "Copenhagen", "Dakar", "Damascus", "Dhaka", "Dili", "Djibouti", "Dodoma", "Doha", "Douglas", "Dublin", "Dushanbe", "El Aaiún or Laâyoune ", "Flying Fish Cove", "Fort-de-France", "Freetown", "Funafuti", "Gaborone", "George Town", "Georgetown", "Gibraltar", "Guatemala City", "Gustavia", "Hagåtña", "Hamilton", "Hanoi", "Harare", "Havana", "Helsinki", "Hong Kong", "Honiara", "Islamabad", "Jakarta", "Jerusalem", "Juba", "Kabul", "Kampala", "Kathmandu", "Khartoum", "Kiev", "Kigali", "King Edward Point", "Kingston", "Kingston", "Kingstown", "Kinshasa", "Kuala Lumpur", "Kuwait City", "Libreville", "Lilongwe", "Lima", "Lisbon", "Ljubljana", "Lomé", "London", "Longyearbyen", "Luanda", "Lusaka", "Luxembourg", "Madrid", "Majuro", "Malabo", "Malé", "Mamoudzou", "Managua", "Manama", "Manila", "Maputo", "Mariehamn", "Marigot", "Maseru", "Mata-Utu", "Mbabane", "Mexico City", "Minsk", "Mogadishu", "Monaco", "Monrovia", "Montevideo", "Moroni", "Moscow", "Muscat", "Nairobi", "Nassau", "Nay Pyi Taw", "New Delhi", "Niamey", "Nicosia", "Nouakchott", "Nouméa", "Nuku'alofa", "Nursultan", "Nuuk", "N'Djamena", "Oranjestad", "Oslo", "Ottawa", "Ouagadougou", "Pago Pago", "Panama City", "Papeete", "Paramaribo", "Paris", "Philipsburg", "Phnom Penh", "Podgorica", "Port Louis", "Port Moresby", "Port-Vila", "Port-au-Prince", "Port-of-Spain", "Porto-Novo", "Prague", "Praia", "Pretoria", "Pristina", "Pyongyang", "Quito", "Rabat", "Ramallah", "Reykjavík", "Riga", "Riyadh", "Road Town", "Rome", "Roseau", "Saint George's", "Saint Helier", "Saint John's", "Saint Peter Port", "Saint-Denis", "Saint-Pierre", "Saipan", "San José", "San Juan", "San Marino", "San Salvador", "Sanaa", "Santiago", "Santo Domingo", "Sarajevo", "Seoul", "Singapore", "Skopje", "Sofia", "Stanley", "Stockholm", "Sucre", "Suva", "São Tomé", "Taipei", "Tallinn", "Tarawa", "Tashkent", "Tbilisi", "Tegucigalpa", "Tehran", "The Valley", "Thimphu", "Tirana", "Tokyo", "Tripoli", "Tunis", "Tórshavn", "Ulaanbaatar", "Vaduz", "Valletta", "Victoria", "Vienna", "Vientiane", "Vilnius", "Warsaw", "Washington", "Wellington", "West Island", "Willemstad", "Windhoek", "Yamoussoukro", "Yaoundé", "Yaren", "Yerevan", "Zagreb"
]


@app.route("/")
def home():
    return render_template("index.html",
                           capital_city=capitals)
