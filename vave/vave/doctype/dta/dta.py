# -*- coding: utf-8 -*-
# Copyright (c) 2015, value added value engineering and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class dta(Document):
	pass


@frappe.whitelist()
def make_dta(source_name, target_doc=None):

doclist = get_mapped_doc("dta", source_name,		{
		"dta": {
			"doctype": "vave",
			
		},

return doclist
