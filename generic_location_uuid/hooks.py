import logging

from odoo.tools.sql import (
    column_exists,
)
from odoo.addons.generic_mixin.tools.uuid import (
    auto_generate_uuids,
    create_uuid_field,
)

_logger = logging.getLogger(__name__)


def pre_init_hook(env):
    if column_exists(env.cr, 'generic_location', 'uuid'):
        _logger.info(
            "generic_location: uuid column already exists, "
            "no need to run pre-init hook")
        return

    create_uuid_field(env.cr, 'generic_location', 'uuid')

    auto_generate_uuids(env.cr, 'generic_location', 'uuid')
