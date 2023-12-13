// frappe.ui.form.on('Item', {

//     refresh: function(frm) {
//         console.log(11)
//         if (frm.is_new()!=1 && frm.doc.barecode_lable) {
//             frm.add_custom_button("Label Print", function() {
//                 let url = `/api/method/label_print_gc.api.get_single_item_label_print_pdf`;
//                 let args = {
//                     doctype: frm.doc.doctype,
//                     docname: frm.doc.name,
//                     print_type:'indirectpdf'
//                 };
//                 open_url_post(url, args, true);
//             });       
//         }
//     }
// });


frappe.ui.form.on("Item", {
    refresh: function (frm) {
        if (frm.is_new()!=1 && frm.doc.barecode_lable) {
            frm.page.add_inner_button(__("Print Label"), () => {
                let url = "/api/method/label_print_gc.api.get_item_label", 
                  args = {
                    docname: frm.doc.name,
                  };
                open_url_post(url, args, true);
              });
        }

    },
  });
  