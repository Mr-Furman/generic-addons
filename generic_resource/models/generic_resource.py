import logging
from odoo import fields, models, api

from odoo.addons.generic_mixin import interface_proxy
from odoo.addons.generic_mixin.tools.generic_m2o import generic_m2o_get

_logger = logging.getLogger(__name__)


# resource_proxy decorator, that have to be used to mark methods that have
# to be added to resource implementation model.
# For backward compatibility we just do this assignment
resource_proxy = interface_proxy


class GenericResource(models.Model):
    _name = 'generic.resource'
    _inherit = [
        'generic.mixin.get.action',
        'generic.mixin.delegation.interface',
    ]
    _description = 'Generic Resource'
    _log_access = False

    _generic_mixin_implementation_model_field = 'res_model'
    _generic_mixin_implementation_id_field = 'res_id'

    active = fields.Boolean(default=True, index=True)
    res_type_id = fields.Many2one(
        'generic.resource.type', string="Resource Type",
        required=True, index=True, readonly=True, ondelete='cascade')
    res_model = fields.Char(
        related='res_type_id.model_id.model', readonly=True, store=True,
        string="Resource Model", compute_sudo=True, index=True)
    res_id = fields.Integer(
        string="Resource", required=True, index=True, readonly=True)
    resource_visibility = fields.Selection(
        [('internal', 'Visible only to internal users'),
         ('portal', 'Visible to internal users and portal users'),
         ('public', 'Visible for unregistered users')],
        default='internal', required=True, index=True,
        help="Resource visibility determines users that have read access for "
             "this resource.")

    _sql_constraints = [
        ('unique_model', 'UNIQUE(res_model, res_id)',
         'Model instance must be unique')
    ]

    @property
    def resource(self):
        """ Property to easily access implementation of this generic resource
        """
        return generic_m2o_get(
            self, field_res_model='res_model', field_res_id='res_id')

    @api.model
    def _get_resource_type_defaults(self, resource_type):
        """ Get default values for resource from resource type

            DEPRECATION: This method is deprecated.
                         Use generic.resource.type._get_resource_defaults
                         instead
        """
        # TODO: Remove this method in future in favor of
        #       generic.resource.type._get_resource_defaults
        return resource_type._get_resource_defaults()

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):  # noqa
        if name:
            resource_types = self.env['generic.resource.type'].search([])
            result = []
            for r_type in resource_types:
                res = self.env[r_type.model]._name_search(
                    name=name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)  # noqa
                result.extend(res)
            return result
        return super(GenericResource, self)._name_search(
            name=name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)  # noqa

    def _preprocess_resource_changes(self, changes):
        """ This method is called before write on resource implementation and
            receives dict with changes of tracked fields.

            This method may be overridden by other modules to add
            some postprocessing of resource changes.

            :param dict changes: keys are changed field names,
                                 values are tuples (old_value, new_value)
            :rtype: dict
            :return: values to update record with.
                     These values will be written just after write
        """
        return {}

    def _postprocess_resource_changes(self, changes):
        """ This method is called adter write on resource implementation and
            receives dict with changes of tracked fields.

            This method may be overridden by other modules to add
            some postprocessing of write.
            This method does not return any  value.

            :param dict changes: keys are changed field names,
                                 values are tuples (old_value, new_value)
            :return: None

        """

    @api.model
    def default_get(self, fields_list):
        res = super(GenericResource, self).default_get(fields_list)

        if 'generic_resource_type_model' in self.env.context:
            res_type = self.env['generic.resource.type'].get_resource_type(
                self.env.context['generic_resource_type_model'])
            res.update({
                k: v
                for k, v in res_type._get_resource_defaults().items()
                if k in fields_list
            })
        return res

    def on_resource_created(self):
        """ Hook to be called when resource creation completed
        """

    def action_open_resource_object(self):
        """ Open resource implementation object
        """
        if self.resource:
            return self.resource.get_formview_action()
        return None
