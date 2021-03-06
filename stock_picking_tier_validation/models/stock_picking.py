# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Picking(models.Model):
    _name = "stock.picking"
    _inherit = ['stock.picking', 'tier.validation']
    _state_from = ['draft']
    _state_to = ['waiting', 'confirmed', 'assigned', 'done']