frappe.provide("compliance_center");

compliance_center.show_module_doctypes_modal = function () {
	frappe.call({
		method: "frappe.client.get_list",
		args: {
			doctype: "DocType",
			filters: {
				module: "Compliance Center",
				istable: 0,
				custom: 0,
			},
			fields: ["name", "description"],
			order_by: "name asc",
			limit_page_length: 0,
		},
		callback: function (r) {
			let doctypes = r.message || [];
			compliance_center.render_doctypes_dialog(doctypes);
		},
	});
};

compliance_center.render_doctypes_dialog = function (doctypes) {
	let dialog = new frappe.ui.Dialog({
		title: __("Compliance Center"),
		fields: [
			{
				fieldtype: "HTML",
				fieldname: "doctype_list",
			},
		],
	});

	let $wrapper = $('<div class="compliance-center-doctype-list"></div>').appendTo(
		dialog.fields_dict.doctype_list.$wrapper
	);

	if (!doctypes.length) {
		$wrapper.append(`<div class="text-muted">${__("No doctypes found in this module.")}</div>`);
	} else {
		doctypes.forEach((dt) => {
			let $box = $(`
				<div class="compliance-center-doctype-box" style="
					display:flex; align-items:center; justify-content:space-between;
					padding:10px 14px; margin-bottom:8px; border:1px solid var(--border-color);
					border-radius:var(--border-radius); cursor:pointer;">
					<span>${frappe.utils.escape_html(dt.name)}</span>
					<span class="text-muted">→</span>
				</div>
			`).appendTo($wrapper);

			$box.on("click", () => {
				dialog.hide();
				frappe.set_route("List", dt.name);
			});
		});
	}

	dialog.show();
};

$(document).on("click", 'a.desktop-icon[data-id="Compliance Center"]', function (e) {
	if ($(e.target).closest(".hide-button").length) {
		return;
	}
	e.preventDefault();
	e.stopImmediatePropagation();
	compliance_center.show_module_doctypes_modal();
});
