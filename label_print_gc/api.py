import frappe
from frappe import _
from frappe.utils.pdf import get_pdf


@frappe.whitelist()
def get_icecream_label_print_pdf(doctype,docname, print_type='indirectpdf'):
     doc = frappe.get_doc(doctype,docname).as_dict()
    
     doc.update({
          			"lang": "ar",
     })
     html = frappe.get_template("label_print_gc/print_format/multiple_col_item_barcode.html").render(doc=doc)
     options={
     #    "page-width": "210mm",
     #    "page-height": "297mm",          
        "margin-left":"0mm",
        "margin-right":"0mm",
        "page-size":"A4"
       
}
     if print_type=='indirectpdf':
          frappe.local.response.filename = "{name}.pdf".format(
          name=docname.replace(" ", "-").replace("/", "-")
     )
          frappe.local.response.filecontent = get_pdf(html,options)
          frappe.local.response.type = "pdf" 
   
