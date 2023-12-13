import frappe
import base64
import barcode
from frappe import _
from frappe.utils.pdf import get_pdf
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter
from werkzeug.wrappers import Response
from frappe.utils import flt, cint

@frappe.whitelist()
def get_single_item_label_print_pdf(doctype,docname, print_type='indirectpdf'):
     doc = frappe.get_doc(doctype,docname).as_dict()
    
     # doc.update({
     #      			"lang": "ar",
     # })
     print(doc)
     html = frappe.get_template("label_print_gc/print_format/single_item_barcode_label.html").render(doc=doc)
     # html = frappe.get_template("label_print_gc/print_format/try.html").render(doc=doc)
     options={
        "page-width": "45mm",
        "page-height": "12mm",          
        "margin-left":"0mm",
        "margin-right":"0mm",
     #    "page-size":"A4"
       
}
     if print_type=='indirectpdf':
          frappe.local.response.filename = "{name}.pdf".format(
          name=docname.replace(" ", "-").replace("/", "-")
     )
          frappe.local.response.filecontent = get_pdf(html,options)
          frappe.local.response.type = "pdf" 


# @frappe.whitelist()
# def get_icecream_label_print_pdf(doctype,docname, print_type='indirectpdf'):
#      doc = frappe.get_doc(doctype,docname).as_dict()
    
#      doc.update({
#           			"lang": "ar",
#      })
#      print(doc)
#      html = frappe.get_template("label_print_gc/print_format/multiple_col_item_barcode.html").render(doc=doc)
#      options={
#      #    "page-width": "210mm",
#      #    "page-height": "297mm",          
#         "margin-left":"0mm",
#         "margin-right":"0mm",
#         "page-size":"A4"
       
# }
#      if print_type=='indirectpdf':
#           frappe.local.response.filename = "{name}.pdf".format(
#           name=docname.replace(" ", "-").replace("/", "-")
#      )
#           frappe.local.response.filecontent = get_pdf(html,options)
#           frappe.local.response.type = "pdf" 
   

# def get_item_barcode(ewaybill):
#     stream = BytesIO()
#     Code128(str(ewaybill), writer=ImageWriter()).write(
#         stream,
#         {
#             "module_width": 0.5,
#             "text_distance": 2.9,
#           #   "font_size": 9,
#         },
#     )
#     barcode_base64 = base64.b64encode(stream.getbuffer()).decode()
#     stream.close()

#     return barcode_base64

# def get_item_barcode(ewaybill):
#     stream = BytesIO()
#     Code128(str(ewaybill), writer=ImageWriter()).write(
#         stream,
#         {
#             "module_width": 0.4,
#             "text_distance": 2,
#             "font_size": 20,
#         },
#     )
#     barcode_base64 = base64.b64encode(stream.getbuffer()).decode()
#     stream.close()

#     return barcode_base64

@frappe.whitelist()
def get_item_label(docname):
     pdf_options = {
     # set margins
     "margin-left": "0.1mm",
     "margin-right": "0.1mm",  # from 4
     "margin-top": "0.1mm",  # 3.1
     "margin-bottom": "0.1mm",
     # "orientation": "Portrait",
     "orientation": "Landscape",
     "page-height": "45mm",
     "page-width": "12mm",
     # "outline": True,
     "no-outline": None,
     }    
     doc = frappe.db.get_values(
        "Item",
        docname,
        ["item_name", "item_code","sales_price"],
        as_dict=True,
    )[0]
    
     barcodes=frappe.db.get_list('Item Barcode',filters={'parent': docname },fields=['barcode']) 
     if len(barcodes)>0:
        barcode_label=barcodes[0].barcode
        doc.update({'barcode_label':barcodes[0].get('barcode')})
        # doc.append()label_print_gc/label_print_gc/print_format/item_label.html
     print(doc,barcodes[0].get('barcode'))    
     html = frappe.render_template("label_print_gc/print_format/item_label.html", dict(doc=doc))
     frappe.local.response.filename = f"Item_{doc.item_code}_label.pdf"
     frappe.local.response.filecontent = get_pdf(html, pdf_options)
     frappe.local.response.type = "pdf"

@frappe.whitelist(allow_guest=True)
def get_barcode(
    barcode_text="",
    code="code128",
    margin=0,
    height=1,
    write_text=False,
    background="white",
    foreground="black",
    font_size=0,
):
    """
    Returns barcode.png for barcode_text
    Usage: <site_url>/api/method/dotted_path_to.get_barcode"""

    buf = BytesIO()
    out = barcode.get(code, barcode_text, writer=ImageWriter()).write(
        buf,
        {
            # barcode options
            # https://python-barcode.readthedocs.io/en/stable/writers/index.html
            # The width of one barcode module in mm as float. Defaults to 0.2.
            "module_width": 0.1,
            # The height of the barcode modules in mm as float. Defaults to 15.0...26.46
            "module_height": flt(height),
            # Distance on the left and on the right from the border to the first (last) barcode module in mm as float. Defaults to 6.5.
            "quiet_zone": flt(margin),
            "font_size": font_size,
            # Do not print text below image
            "write_text": cint(write_text),
            "foreground": foreground,
            "background": background,
            # "text_distance": Distance between the barcode and the text under it in mm as float
        },
    )
    

    response = Response()
    response.mimetype = "image/png"
    response.data = buf.getvalue()
    return response     