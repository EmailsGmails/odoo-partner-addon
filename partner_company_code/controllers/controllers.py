# -*- coding: utf-8 -*-
from odoo import http

class PartnerCompanyCode(http.Controller):
    @http.route('/partner_company_code/partner_company_code/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/partner_company_code/partner_company_code/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('partner_company_code.listing', {
            'root': '/partner_company_code/partner_company_code',
            'objects': http.request.env['partner_company_code.partner_company_code'].search([]),
        })

    @http.route('/partner_company_code/partner_company_code/objects/<model("partner_company_code.partner_company_code"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('partner_company_code.object', {
            'object': obj
        })