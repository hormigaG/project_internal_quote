# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api 
from openerp import tools


from openerp.tools.translate import _
import logging


_logger = logging.getLogger(__name__)



class project_internal_quote_category(models.Model):

    _name = 'project.internal.quote.category'
    _description = 'project internal quote'

    name = fields.Char()
    default_user_id = fields.Many2one('res.users')




class project_project(models.Model):

    _inherit = 'project.project'

    state = fields.Selection(selection_add=[('quoting', 'Presupuesto')])
    internal_quote_task_ids=fields.One2many('project.task','project_id')



class project_task_quote(models.Model):

    _name = 'project.task.quote'
    _description = 'task internal quote'

    task_id = fields.Many2one(
        comodel_name='project.task', string='Task', ondelete='cascade',
        required=True)

    product_id = fields.Many2one('product.product')
    product_uom = fields.Many2one(comodel_name='product.uom', string='Unit of Measure')
    quantity = fields.Float(string='Quantity')


class project_task(models.Model):

    _inherit = 'project.task'

    quote_task=fields.Boolean('quote task')
    quote_ids = fields.One2many(
        comodel_name='project.task.quote', inverse_name='task_id',
        string='Materials quoted')
