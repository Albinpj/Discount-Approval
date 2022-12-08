from odoo import api, fields, models


class ServerAction(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(selection_add=[('approved', 'Approved'), ('sent',)])

    def send_by_mail(self):
        res = super(ServerAction, self).action_quotation_send()
        self.write({
            'state': "sent"
        })
        return res
