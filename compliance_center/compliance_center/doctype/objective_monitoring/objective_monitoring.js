// Copyright (c) 2026, pushkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Objective Monitoring", {
	onload(frm) {
		frm.set_query("department", () => ({
			query:
				"compliance_center.compliance_center.doctype.objective_monitoring.objective_monitoring.get_departments_with_objectives",
		}));
	},
	department(frm) {
		fetch_active_objectives(frm);
	},
});

frappe.ui.form.on("Objective Monitoring Item", {
	actual_result(frm, cdt, cdn) {
		compute_result(frm, cdt, cdn);
	},
});

function fetch_active_objectives(frm) {
	frm.clear_table("objectives");

	if (!frm.doc.department) {
		frm.refresh_field("objectives");
		return;
	}

	frappe.db
		.get_list("Objective", {
			filters: { department: frm.doc.department, status: "Active" },
			fields: ["name", "target"],
			limit: 1000,
		})
		.then((objectives) => {
			objectives.forEach((objective) => {
				let row = frm.add_child("objectives");
				row.objective = objective.name;
				row.target = objective.target;
			});
			frm.refresh_field("objectives");

			if (!objectives.length) {
				frappe.show_alert({
					message: __("No Active objectives found for this Department"),
					indicator: "orange",
				});
			}
		});
}

function compute_result(frm, cdt, cdn) {
	let row = frappe.get_doc(cdt, cdn);
	let result = "";
	if (row.target !== null && row.target !== undefined && row.actual_result !== null && row.actual_result !== undefined) {
		result = flt(row.actual_result) >= flt(row.target) ? "Met" : "Not Met";
	}
	frappe.model.set_value(cdt, cdn, "result", result);
}
