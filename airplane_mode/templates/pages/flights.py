

import frappe

def format_duration(seconds):
    if not seconds:
        return "N/A"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"

def get_context(context):
    flights = frappe.get_all(
        "Airplane Flight",
        filters={"is_published": 1},          # Only show published flights
        fields=[
            "name",
            "route",                           # Used to build the detail page link
            "source_airport_code",
            "destination_airport_code",
            "date_of_departure",
            "time_of_departure",
            "duration",
            "status"
        ],
        order_by="date_of_departure asc"
    )

    for flight in flights:
        flight["duration"] = format_duration(flight["duration"])

    context.flights = flights
    context.title = "All Flights"