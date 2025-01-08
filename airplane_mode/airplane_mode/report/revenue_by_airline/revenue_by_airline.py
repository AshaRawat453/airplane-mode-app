# Copyright (c) 2024, asha rawat and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data
# import frappe

# def execute(filters=None):
#     # Define the columns for the report
#     columns = [{
#         "fieldname": "airline",
#         "label": "Airline",
#         "fieldtype": "Link",
#         "options": "Airline"  # Link to Airline DocType
#     }, {
#         "fieldname": "revenue",
#         "label": "Revenue",
#         "fieldtype": "Currency",
#         "options": "INR"
#     }]

#     # Fetch airplane tickets
#     tickets = frappe.get_all("Airplane Ticket", fields=["total_amount", "flight"], filters={})
    
#     # Initialize a dictionary to hold aggregated revenue by airline
#     aggregated_data = {}
#     airlines = frappe.get_all("Airline", fields=["name"])  # Fetch all airlines

#     for airline in airlines:
#         aggregated_data[airline['name']] = 0  # Initialize all airlines with 0 revenue

#     # Loop through the tickets and aggregate the revenue
#     for ticket in tickets:
#         flight = frappe.get_value("Airplane Flight", ticket.flight, "airplane")
#         if flight:
#             airline = frappe.get_value("Airplane", flight, "airline")
#             if airline:
#                 aggregated_data[airline] += ticket.total_amount  # Aggregate revenue

#     # Prepare final data for the report
#     final_data = [{"airline": airline, "revenue": revenue} for airline, revenue in aggregated_data.items()]

#     # Calculate total revenue
#     total_revenue = sum(item['revenue'] for item in final_data)

#     # Prepare donut chart data
#     chart = {
#         "data": {
#             "labels": [item["airline"] for item in final_data],
#             "datasets": [
#                 {
#                     "values": [item["revenue"] for item in final_data]
#                 }
#             ],
#         },
#         "type": "donut"  # Use 'donut' for the donut chart
#     }

#     return columns, final_data, f"Total Revenue: {total_revenue}", chart

import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "airline", "label": "Airline", "fieldtype": "Link", "options": "Airline"},
        {"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency", "options": "INR"}
    ]

    tickets = frappe.get_all("Airplane Ticket", fields=["total_amount", "flight"])
    airlines = frappe.get_all("Airline", fields=["name"])
    revenue_data = {airline['name']: 0 for airline in airlines}

    for ticket in tickets:
        airline = frappe.get_value("Airplane", frappe.get_value("Airplane Flight", ticket.flight, "airplane"), "airline")
        if airline:
            revenue_data[airline] += ticket.total_amount

    final_data = [{"airline": airline, "revenue": revenue} for airline, revenue in revenue_data.items()]
    total_revenue = sum([item['revenue'] for item in final_data])

    chart = {
        "data": {
            "labels": [item["airline"] for item in final_data],
            "datasets": [{"values": [item["revenue"] for item in final_data]}]
        },
        "type": "donut"
    }

    return columns, final_data, f"Total Revenue: {total_revenue}", chart
