# -*- coding: utf-8 -*-

from openerp import fields, models


class GenericResourceSimpleCategory(models.Model):
    _name = 'generic.resource.simple.category'
    _inherit = [
        'mail.thread',
        'generic.mixin.parent.names',
    ]
    _description = 'Generic Resource Simple Category'

    _parent_name = 'parent_id'
    _parent_order = 'name'
    _parent_store = True

    name = fields.Char(index=True, required=True, translate=True)
    active = fields.Boolean(default=True, index=True)
    parent_id = fields.Many2one(
        'generic.resource.simple.category', 'Parent Category',
        index=True, ondelete='restrict')
    parent_left = fields.Integer('Left Parent', index=True)
    parent_right = fields.Integer('Right Parent', index=True)

    _sql_constraints = [
        ('category_unique', 'unique(parent_id, name)',
         'Category can not have subcategories with the same name!')]
