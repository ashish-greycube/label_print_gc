from . import __version__ as app_version

app_name = "label_print_gc"
app_title = "Label Print Gc"
app_publisher = "GreyCube Technologies"
app_description = "label"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/label_print_gc/css/label_print_gc.css"
# app_include_js = "/assets/label_print_gc/js/label_print_gc.js"

# include js, css files in header of web template
# web_include_css = "/assets/label_print_gc/css/label_print_gc.css"
# web_include_js = "/assets/label_print_gc/js/label_print_gc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "label_print_gc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Print Barcode Label" : "public/js/print_barcode_label.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "label_print_gc.install.before_install"
# after_install = "label_print_gc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "label_print_gc.uninstall.before_uninstall"
# after_uninstall = "label_print_gc.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "label_print_gc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"label_print_gc.tasks.all"
#	],
#	"daily": [
#		"label_print_gc.tasks.daily"
#	],
#	"hourly": [
#		"label_print_gc.tasks.hourly"
#	],
#	"weekly": [
#		"label_print_gc.tasks.weekly"
#	]
#	"monthly": [
#		"label_print_gc.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "label_print_gc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "label_print_gc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "label_print_gc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["label_print_gc.utils.before_request"]
# after_request = ["label_print_gc.utils.after_request"]

# Job Events
# ----------
# before_job = ["label_print_gc.utils.before_job"]
# after_job = ["label_print_gc.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"label_print_gc.auth.validate"
# ]

