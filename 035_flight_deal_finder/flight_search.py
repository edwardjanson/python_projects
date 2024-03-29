from flight_data import FlightData
import requests
import os

FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/"
API_KEY = os.environ.get("API_KEY")


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {
            "apikey": API_KEY
        }

        parameters = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(
            f"{FLIGHT_ENDPOINT}/locations/query",
            params=parameters,
            headers=headers
        )

        data = response.json()["locations"]
        city_code = data[0]["code"]
        return city_code

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": API_KEY
        }

        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            f"{FLIGHT_ENDPOINT}v2/search",
            params=parameters,
            headers=headers
        )

        try:
            data = response.json()["data"][0]

        except IndexError:
            parameters["max_stopovers"] = 1
            response = requests.get(
                url=f"{FLIGHT_ENDPOINT}/v2/search",
                headers=headers,
                params=parameters,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
