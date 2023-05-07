from odoo import models, fields


class GenericLocationGeolocalizeMixin(models.AbstractModel):
    _name = 'generic.location.geolocalize.mixin'
    _inherit = 'generic.location.address.mixin'
    _description = 'Generic Location Geolocalize Mixin'

    longitude = fields.Float(related='location_id.longitude')
    latitude = fields.Float(related='location_id.latitude')

    def geo_localize(self):
        if self.location_id:
            return self.location_id.geo_localize()
        return False
