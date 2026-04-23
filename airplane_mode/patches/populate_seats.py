import frappe
import random

def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name", "seat"])

    used_seats = set()

    # Step 1: collect existing seats
    for t in tickets:
        if t.get("seat"):
            used_seats.add(t["seat"])

    # Step 2: assign seats to empty ones
    for t in tickets:
        if t.get("seat"):
            continue

        doc = frappe.get_doc("Airplane Ticket", t["name"])

        # generate a unique seat
        while True:
            letter = random.choice("ABCDE")
            number = str(random.randint(1, 99))
            seat = number + letter

            if seat not in used_seats:
                used_seats.add(seat)
                break

        doc.seat = seat
        doc.save(ignore_permissions=True)

    frappe.db.commit()