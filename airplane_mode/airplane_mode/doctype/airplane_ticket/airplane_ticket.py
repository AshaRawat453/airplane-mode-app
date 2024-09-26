# Copyright (c) 2024, asha rawat and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    def before_insert(self):
        number = random.randint(10, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{number}{letter}"

    def validate(self):
        addon_items = []
        for addon in self.add_ons:
            if addon.item in addon_items:
                frappe.throw("Duplicate Add-ons are not allowed")
            addon_items.append(addon.item)

        addon_total = 0
        for addon in self.add_ons:
            addon_total += addon.amount
        self.total_amount = self.flight_price + addon_total
        
    # def on_submit(self):
    def on_submit(self):
        frappe.db.set_value('Airplane Flight', self.flight, 'status', 'Completed')

        
	