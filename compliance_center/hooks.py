app_name = "compliance_center"
app_title = "Compliance Center"
app_publisher = "pushkar"
app_description = "A centralized application for managing compliance procedures, policies, and documentation."
app_email = "pushkar@frappe.io"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "compliance_center",
# 		"logo": "/assets/compliance_center/logo.png",
# 		"title": "Compliance Center",
# 		"route": "/compliance_center",
# 		"has_permission": "compliance_center.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/compliance_center/css/compliance_center.css"
# app_include_js = "/assets/compliance_center/js/compliance_center.js"

# include js, css files in header of web template
# web_include_css = "/assets/compliance_center/css/compliance_center.css"
# web_include_js = "/assets/compliance_center/js/compliance_center.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "compliance_center/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "compliance_center/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "compliance_center.utils.jinja_methods",
# 	"filters": "compliance_center.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "compliance_center.install.before_install"
# after_install = "compliance_center.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "compliance_center.uninstall.before_uninstall"
# after_uninstall = "compliance_center.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "compliance_center.utils.before_app_install"
# after_app_install = "compliance_center.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "compliance_center.utils.before_app_uninstall"
# after_app_uninstall = "compliance_center.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "compliance_center.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "compliance_center.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"compliance_center.tasks.all"
# 	],
# 	"daily": [
# 		"compliance_center.tasks.daily"
# 	],
# 	"hourly": [
# 		"compliance_center.tasks.hourly"
# 	],
# 	"weekly": [
# 		"compliance_center.tasks.weekly"
# 	],
# 	"monthly": [
# 		"compliance_center.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "compliance_center.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "compliance_center.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "compliance_center.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "compliance_center.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["compliance_center.utils.before_request"]
# after_request = ["compliance_center.utils.after_request"]

# Job Events
# ----------
# before_job = ["compliance_center.utils.before_job"]
# after_job = ["compliance_center.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"compliance_center.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

