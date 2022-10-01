from odoo import models, fields


class Interface1(models.Model):
    _name = "test.generic.mixin.interface.1"
    _inherit = [
        'generic.mixin.delegation.interface',

    ]
    _description = 'Test Generic Mixin: Interface 1'
    _log_access = False

    _generic_mixin_implementation_model_field = 'interface_1_impl_model'
    _generic_mixin_implementation_id_field = 'interface_1_impl_id'

    interface_1_impl_model = fields.Char(required=True)
    interface_1_impl_id = fields.Integer(required=True)

    interface_1_test_field_1 = fields.Char()

    _sql_constraints = [
        ('unique_model', 'UNIQUE(interface_1_impl_model, interface_1_impl_id)',
         'Model instance must be unique')
    ]


class Interface2(models.Model):
    _name = "test.generic.mixin.interface.2"
    _inherit = [
        'generic.mixin.delegation.interface',
    ]
    _description = 'Test Generic Mixin: Interface 2'
    _log_access = False

    _generic_mixin_implementation_model_field = 'interface_2_impl_model'
    _generic_mixin_implementation_id_field = 'interface_2_impl_id'

    interface_2_impl_model = fields.Char(required=True)
    interface_2_impl_id = fields.Integer(required=True)

    interface_2_test_field_1 = fields.Char()

    _sql_constraints = [
        ('unique_model', 'UNIQUE(interface_2_impl_model, interface_2_impl_id)',
         'Model instance must be unique')
    ]


class ImplementationMixin1(models.AbstractModel):
    _name = 'test.generic.mixin.interface.1.impl.mixin'
    _description = 'Test Generic Mixin: Interface 1 Implementation Mixin'
    _inherit = [
        'generic.mixin.track.changes',
        'generic.mixin.delegation.implementation',
    ]

    interface_1_id = fields.Many2one(
        'test.generic.mixin.interface.1', index=True, auto_join=True,
        required=True, delegate=True, ondelete='restrict')

    _sql_constraints = [
        ('unique_interface_1_id', 'UNIQUE(interface_1_id)',
         'Interface must be unique')
    ]


class ImplementationMixin2(models.AbstractModel):
    _name = 'test.generic.mixin.interface.2.impl.mixin'
    _description = 'Test Generic Mixin: Interface 2 Implementation Mixin'
    _inherit = [
        'generic.mixin.track.changes',
        'generic.mixin.delegation.implementation',
    ]

    interface_2_id = fields.Many2one(
        'test.generic.mixin.interface.2', index=True, auto_join=True,
        required=True, delegate=True, ondelete='restrict')

    _sql_constraints = [
        ('unique_interface_2_id', 'UNIQUE(interface_2_id)',
         'Interface must be unique')
    ]


class TestDelegationMultiInterface(models.Model):
    _name = 'test.generic.mixin.multi.interface.impl'
    _inherit = [
        'test.generic.mixin.interface.1.impl.mixin',
        'test.generic.mixin.interface.2.impl.mixin',
        'generic.mixin.track.changes',
    ]

    name = fields.Char()