# # Copyright (c) 2024, asha rawat and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# # class voterid(Document):
# # 	pass

# # from frappe.model.document import Document
# # import frappe  

# class voterid(Document):  
#     def validate(self):
#         if self.age < 18:  
#             frappe.throw("Person's age must be at least 18")

#     def after_insert(self):
#         frappe.sendmail(recipients=[self.email], message="Thank you for registering!")



import frappe
from frappe.model.document import Document

class voterid(Document):
    def validate(self):
        if self.age < 18:
            frappe.throw("Person's age must be at least 18")
        else:
            frappe.msgprint("succefully submited")

   