// Copyright (c) 2024, asha rawat and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field has a value
        if (frm.doc.website) {
            // Add a web link to the official airline website
            frm.add_web_link(__('Visit Website'), frm.doc.website);
        }
    }
});
