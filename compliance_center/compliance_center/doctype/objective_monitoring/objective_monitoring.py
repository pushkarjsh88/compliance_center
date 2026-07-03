# Copyright (c) 2026, pushkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt


class ObjectiveMonitoring(Document):
	def autoname(self):
		if self.department:
			department_code = self.department.split(" - ")[0].strip().upper().replace(" ", "-")
		else:
			department_code = "GENERAL"
		period_code = (self.review_period or "").strip().upper().replace(" ", "-") or "PERIOD"
		self.name = f"{department_code}-{period_code}"

	def validate(self):
		self.set_results()

	def set_results(self):
		for row in self.objectives:
			if row.actual_result is None or row.target is None:
				row.result = None
				continue
			row.result = "Met" if flt(row.actual_result) >= flt(row.target) else "Not Met"


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_departments_with_objectives(doctype, txt, searchfield, start, page_len, filters):
	departments = frappe.get_all("Objective", pluck="department", distinct=True)
	if not departments:
		return []

	return frappe.get_all(
		"Department",
		limit_start=start,
		limit_page_length=page_len,
		filters=[
			["Department", "name", "in", departments],
			["Department", searchfield, "like", f"%{txt}%"],
		],
		as_list=True,
	)
