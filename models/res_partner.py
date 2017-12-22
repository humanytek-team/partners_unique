# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, models
from openerp.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    _sql_constraints = [
        ('name_phone_email_key',
         'UNIQUE (name, phone, email)',
         _('This partner is already registered.'))
    ]
