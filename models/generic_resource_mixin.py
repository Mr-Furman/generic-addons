from odoo import fields, models, api
from .generic_resource import GenericResourceResID


import logging
_logger = logging.getLogger(__name__)


class GenericResourceMixin(models.AbstractModel):
    _name = 'generic.resource.mixin'

    resource_id = fields.Many2one(
        'generic.resource', index=True, auto_join=True,
        required=True, delegate=True, ondelete='restrict')

    _sql_constraints = [
        ('unique_resource_id', 'UNIQUE(resource_id)',
         'Resource must be unique')
    ]

    def _resource_mixin__protect_resource_id(self, vals):
        if vals.get('resource_id', None):
            _logger.warning(
                "Trying update / create object with 'resource_id' "
                "field specified. No need for this, resource will be created "
                "automatically")
            del vals['resource_id']
        return vals

    @api.multi
    def write(self, vals):
        vals = self._resource_mixin__protect_resource_id(vals)
        return super(GenericResourceMixin, self).write(vals)

    @api.model
    def create(self, vals):
        vals = self._resource_mixin__protect_resource_id(vals)

        values = self.env['generic.resource']._get_resource_type_defaults(
            self._get_resource_type())
        values.update(vals)

        # Add fake resource id to values. This is required to create
        # 'generic.resource' record, because 'res_id' field is required
        # This field will be updated after record creation
        values['res_id'] = GenericResourceResID(-1)

        # Create record
        # TODO: this create somehow triggers write on self. Review.
        rec = super(GenericResourceMixin, self).create(values)

        # Update res_id with created id
        rec.resource_id.write({'res_id': GenericResourceResID(rec.id)})
        return rec

    @api.multi
    def unlink(self):
        # Get resources
        resources = self.mapped('resource_id')

        # Delete records
        res = super(GenericResourceMixin, self).unlink()
        # Delete resources and return status
        resources.unlink()
        return res

    def _get_resource_type(self):
        return self.env['generic.resource.type'].search(
            [('model_id.model', '=', self._name)], limit=1)

    @api.multi
    def check_access_rule(self, operation):
        # Overriden to check access to generic resources also
        self.mapped('resource_id').check_access_rule(operation)
        return super(GenericResourceMixin, self).check_access_rule(operation)


class GenericResourceMixinInvNumber(models.AbstractModel):
    ''' generic_resource_mixin_inv_number model is meant to be inherited by
     any model that needs to have automatically generated field inv_number for
     inventory number.
     For use it you must create sequence in "ir.sequence" model in data
     directory.
     For example:
        <record id="id_for_your_sequence" model="ir.sequence">
            <field name="name">name_for_your_sequence</field>
            <field name="code">code_for_your_sequence</field>
            <field name="prefix">prefix_for_your_inv_number</field>
            <field name="padding">count_of_integer_in_your_inv_number</field>
        </record>

     And use it in model definition. For example:

     class YourModel(models.Model):
         _name = 'your.model'
         _inherit = 'generic.resource.mixin.inv.number'

         _inv_number_seq_code = 'your_addon.id_for_your_sequence'

     It's all!
     Field inv_number will be automatically added to your model.
     Values for it will be generated by sequence
      'your_addon.id_for_your_sequence'.
     '''
    _name = 'generic.resource.mixin.inv.number'
    _description = 'Generic Resource Mixin Inv Number'
    _inv_number_seq_code = None
    _inv_number_in_display_name = False

    inv_number = fields.Char(
        'Inventory Number', index=True, required=True,
        readonly=True, default='', copy=False)

    @api.model
    def create(self, vals):
        if self._inv_number_seq_code is not None and (
                not vals.get('inv_number')):
            vals['inv_number'] = self.env['ir.sequence'].next_by_code(
                self._inv_number_seq_code)
        result = super(GenericResourceMixinInvNumber, self).create(vals)
        return result

    @api.multi
    def name_get(self):
        result = super(GenericResourceMixinInvNumber, self).name_get()
        if not self._inv_number_in_display_name:
            return result

        name_map = dict(result)
        result = []
        for rec in self:
            result.append(
                (rec.id, "%s [%s]" % (name_map[rec.id], rec.inv_number))
            )
        return result
