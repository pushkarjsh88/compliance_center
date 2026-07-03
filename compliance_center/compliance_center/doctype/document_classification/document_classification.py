# Copyright (c) 2026, pushkar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class DocumentClassification(Document):
	def validate(self):
		self.set_display_label()

	def set_display_label(self):
		self.display_label = self.classification_type or self.name
