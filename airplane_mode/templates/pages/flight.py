# <your_app>/templates/pages/flight.py

import frappe
from frappe import _

def format_duration(seconds):
    if not seconds:
        return "N/A"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"

def get_context(context):
    # Frappe resolves the document via the route field automatically
    # context.doc is set by Frappe when route matches
    flight_name = frappe.local.request.path.split("/")[-1]
    print(flight_name)

    try:
        flight = frappe.get_doc("Airplane Flight", flight_name)
    except frappe.DoesNotExistError:
        frappe.throw(_("Flight not found."), frappe.DoesNotExistError)

    # Only allow access to published flights
    if not flight.is_published:
        frappe.throw(_("This flight is not published."), frappe.PermissionError)

    flight.duration = format_duration(flight.duration)

    context.flight = flight
    context.title = f"Flight {flight.name}"

# def get_context(context):
    flight_name = frappe.local.request.path.split("/")[-1]

    try:
        flight = frappe.get_doc("Airplane Flight", flight_name)  # query by name directly
    except frappe.DoesNotExistError:
        frappe.throw(_("Flight not found."), frappe.DoesNotExistError)

    if not flight.is_published:
        frappe.throw(_("This flight is not published."), frappe.PermissionError)

    flight.duration = format_duration(flight.duration)

    context.flight = flight
    context.title = f"Flight {flight.name}"