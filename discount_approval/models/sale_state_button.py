from odoo import api, fields, models


class ServerAction(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(selection_add=[('to_approve', 'To Approve'), ('sent',)])

    def to_approve(self):
        self.write({
            'state': "approved"
        })

    def send_mail(self):
        for rec in self.order_line:
            minimum_amount = self.env['ir.config_parameter'].sudo().get_param('discount_approval.minimum_amount')
            discount_limit = self.env['ir.config_parameter'].sudo().get_param('discount_approval.discount_limit')
            discount = (rec.product_uom_qty * rec.price_unit) - rec.price_subtotal
            res = super(ServerAction, self).action_quotation_send()

            if (discount > float(minimum_amount)) and discount_limit:
                print(minimum_amount)
                print(discount)
                self.state = "to_approve"
            else:
                self.state = "sent"

                return res
