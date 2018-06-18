# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Adds to the res.partner data model an extra field "company_code"
# that allows for up to 3 partners (or contacts) to use the same company code.
class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    company_code = fields.Char("Company Code")

    @api.constrains('company_code')
    def _check_company_code_uses(self):
        same_code_records = self.search_read([('company_code', '=', self.company_code)], ['company_code'])
        limit = 3
        print(same_code_records)
        if len(same_code_records) > limit:
            raise ValidationError("Too many companies use this code!")
