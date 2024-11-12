import frappe

def get_context(context):
    context.airports = frappe.get_all('Airport', fields=['name'])
    filters = get_filters()
    context.shops = frappe.get_all('shop', filters=filters, fields=['shop_name', 'area', 'shop_owner', 'shop_number'])
    context.selected_airport = frappe.form_dict.get('airport', '')
    return context

def get_filters():
    filters = {'availability_status': 'Available'}  # Only fetch shops with status "Available"
    airport = frappe.form_dict.get('airport')

    if airport:
        filters['airport'] = airport

    return filters
