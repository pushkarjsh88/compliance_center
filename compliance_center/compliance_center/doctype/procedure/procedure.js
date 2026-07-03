// Copyright (c) 2026, pushkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Procedure", {
	onload(frm) {
		if (frm.is_new() && !frm.doc.company) {
			frm.set_value("company", frappe.defaults.get_default("company"));
		}
		if (frm.doc.classification) {
			fetch_classification_label(frm);
		}
	},
	refresh(frm) {
		update_version_from_control(frm);
		update_footer(frm);
	},
	company(frm) {
		update_footer(frm);
	},
	procedure(frm) {
		update_footer(frm);
	},
	department(frm) {
		update_footer(frm);
	},
	classification(frm) {
		fetch_classification_label(frm);
	},
	version(frm) {
		update_footer(frm);
	},
});

frappe.ui.form.on("Version Control", {
	version: function (frm) {
		update_version_from_control(frm);
	},
	version_control_add: function (frm) {
		update_version_from_control(frm);
	},
	version_control_remove: function (frm) {
		update_version_from_control(frm);
	},
});

function update_version_from_control(frm) {
	let latest_version = null;
	(frm.doc.version_control || []).forEach((row) => {
		if (row.version && (latest_version === null || row.version > latest_version)) {
			latest_version = row.version;
		}
	});
	frm.set_value("version", latest_version);
	update_footer(frm);
}

function fetch_classification_label(frm) {
	if (!frm.doc.classification) {
		frm._classification_label = null;
		update_footer(frm);
		return;
	}
	frappe.db.get_value("Document Classification", frm.doc.classification, "classification_type").then((r) => {
		frm._classification_label = (r.message && r.message.classification_type) || frm.doc.classification;
		update_footer(frm);
	});
}

function update_footer(frm) {
	let department_label = frm.doc.department ? frm.doc.department.split(" - ")[0].trim() : null;
	let left_parts = [frm.doc.company, frm.doc.procedure, department_label, frm.doc.version ? String(frm.doc.version) : null];
	let left = left_parts.filter(Boolean).join(" ");
	let classification_label = frm.doc.classification ? frm._classification_label || "" : "";
	let footer = `${left} | ${classification_label}`.trim().replace(/^\|\s*/, "").replace(/\s*\|$/, "");
	frm.set_value("footer", footer);
}
