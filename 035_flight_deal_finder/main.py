from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "EDI"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in destinations:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination,
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destinations[destination]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from " \
                  f"{flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}"

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
               f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_emails(emails, message, link)
