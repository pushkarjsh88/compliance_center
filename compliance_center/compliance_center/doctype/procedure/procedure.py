# Copyright (c) 2026, pushkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class Procedure(Document):
	def autoname(self):
		if self.department:
			department_code = self.department.split(" - ")[0].strip().upper().replace(" ", "-")
		else:
			department_code = "GENERAL"
		self.name = make_autoname(f"PROC-{department_code}-.#####")

	def onload(self):
		if not self.company:
			self.company = frappe.defaults.get_user_default("Company")

	def validate(self):
		if not self.company:
			self.company = frappe.defaults.get_user_default("Company")
		self.set_version_from_control()
		self.set_footer()

	def set_version_from_control(self):
		versions = [row.version for row in self.version_control if row.version]
		self.version = max(versions) if versions else None

	def set_footer(self):
		department_label = self.department.split(" - ")[0].strip() if self.department else None
		left_parts = [self.company, self.procedure, department_label, str(self.version) if self.version else None]
		left = " ".join(part for part in left_parts if part)
		classification_label = ""
		if self.classification:
			classification_label = (
				frappe.db.get_value("Document Classification", self.classification, "classification_type")
				or ""
			)
		self.footer = f"{left} | {classification_label}".strip(" |")
