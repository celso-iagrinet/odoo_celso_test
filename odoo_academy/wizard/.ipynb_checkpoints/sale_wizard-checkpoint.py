# -*- coding: utf-8 -*-

from odoo import models, fields, api



class SaleWizard(models.TransientModel):
    _name = 'academy.sale.wizard'
    _description = 'Wizard: Quick sale orders for sessions students'

    def _default_session(self):
        #regredsar la sesion actual en el contexto
        # del contexto actual obtiene el id activo en el navegador ..
        return self.env['academy.session'].browse(self._context.get('active_id'))
    
    session_id = fields.Many2one(comodel_name='academy.session', string='Session', required=True,
                                default=_default_session)
    
    session_student_ids = fields.Many2many(comodel_name='res.partner',
                                         string='Students en current session',
                                         related='session_id.student_ids',
                                         help='Estos son los estudiantes actualmente en la sesion')
    student_ids = fields.Many2many(comodel_name='res.partner',
                                  string='Students for Sales Order')
    
    def create_sale_orders(self):
        session_product_id = self.env['product.product'].search([('is_session_producto','=',True)], limit=1)
        if session_product_id:
            for student in self.student_ids:
                order_id = self.env['sale.order'].create({
                    'partner_id' : student.id,
                    'session_id' : self.session.id,
                    'order_line' : [(0,0,{'product_id': session_product_id.id, 'price_unit': self.session_id.total_price})]
                })
    