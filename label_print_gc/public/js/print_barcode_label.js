frappe.ui.form.on('Print Barcode Label', {

    refresh: function(frm) {
        console.log(11)
        if (frm.is_new()!=1 && frm.doc.item_barcode_print && frm.doc.item_barcode_print.length>0) {
            frm.add_custom_button("Label Print", function() {
                let url = `/api/method/label_print_gc.api.get_icecream_label_print_pdf`;
                let args = {
                    doctype: frm.doc.doctype,
                    docname: frm.doc.name,
                    print_type:'indirectpdf'
                };
                open_url_post(url, args, true);
            });       
        }
    }
});