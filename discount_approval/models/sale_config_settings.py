from odoo import api, models, fields


class ConfSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_limit = fields.Boolean(string="Discount Limit")
    minimum_amount = fields.Float(string="Maximum Amount")

    def set_values(self):
        super(ConfSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'discount_approval.minimum_amount', self.minimum_amount)
        self.env['ir.config_parameter'].set_param(
            'discount_approval.discount_limit', self.discount_limit)

    @api.model
    def get_values(self):
        res = super(ConfSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            minimum_amount=params.get_param('discount_approval.minimum_amount')
        )
        res.update(
            discount_limit=params.get_param('discount_approval.discount_limit')
        )
        # print(res)
        return res
