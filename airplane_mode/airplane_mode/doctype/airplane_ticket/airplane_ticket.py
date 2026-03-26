# Copyright (c) 2026, simon  and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		addons =[]
		obs=set()
		totalz=0
		for i in self.add_ons:
			if i.item not in obs:
				obs.add(i.item)
				addons.append(i)
		self.set("add_ons", addons)
		
		for x in addons:
			totalz+=x.amount

		self.total_amount=self.flight_price+totalz

		seat_char = random.choice("ABCDE")
		seat_num = str(random.randint(1, 99))

		seat_number=seat_num+seat_char
		self.seat=seat_number

	def before_submit(self):
		if self.status!="Boarded":
			frappe.throw("Please make the ticket Boarded")
		else:
			pass








