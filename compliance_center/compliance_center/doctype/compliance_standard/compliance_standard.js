// Copyright (c) 2026, pushkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Compliance Standard", {
	refresh(frm) {
		if (frm.is_new()) return;

		frm.add_custom_button("New Audit", () => {
			const new_doc = frappe.model.get_new_doc("Audit");
			const row = frappe.model.add_child(new_doc, "Audit Compliance Standard", "compliance_standards");
			row.compliance_standard = frm.doc.name;
			frappe.set_route("Form", "Audit", new_doc.name);
		});
	},
});
