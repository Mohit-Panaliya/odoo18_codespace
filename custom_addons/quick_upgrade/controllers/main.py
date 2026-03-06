# -*- coding: utf-8 -*-
import odoo.http as http
from odoo.http import request
import os


class QuickUpgradeController(http.Controller):
    """Controller for quick module upgrade functionality"""

    @http.route('/q', type='http', auth='user', methods=['GET', 'POST'])
    def quick_upgrade_page(self, module_id=None, upgrade_success=False, error_msg=False):
        """
        Render the quick upgrade page with dropdown selection
        """
        # Get custom modules from custom_addons folder
        custom_modules = self._get_custom_modules()

        # Get all installed modules
        installed_modules = self._get_installed_modules()

        # Handle upgrade action
        if module_id and request.httprequest.method == 'POST':
            success, message = self._upgrade_module(module_id)
            if success:
                return request.render('quick_upgrade.quick_upgrade_page', {
                    'custom_modules': custom_modules,
                    'installed_modules': installed_modules,
                    'upgrade_success': True,
                    'success_module': message,
                })
            else:
                return request.render('quick_upgrade.quick_upgrade_page', {
                    'custom_modules': custom_modules,
                    'installed_modules': installed_modules,
                    'error_msg': message,
                })

        return request.render('quick_upgrade.quick_upgrade_page', {
            'custom_modules': custom_modules,
            'installed_modules': installed_modules,
            'upgrade_success': upgrade_success,
            'error_msg': error_msg,
        })

    def _get_custom_modules(self):
        """Get modules from custom_addons folder"""
        # Get addons path from config
        addons_path = request.env['ir.config_parameter'].sudo().get_param('addons.path')
        if not addons_path:
            addons_path = '/workspaces/odoo17_codespace/custom_addons'

        custom_modules = []
        module_obj = request.env['ir.module.module'].sudo()

        try:
            if os.path.exists(addons_path):
                for folder in os.listdir(addons_path):
                    folder_path = os.path.join(addons_path, folder)
                    if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, '__manifest__.py')):
                        # Check if module is installed
                        module = module_obj.search([('name', '=', folder)], limit=1)
                        if module:
                            custom_modules.append({
                                'id': module.id,
                                'name': module.name,
                                'shortdesc': module.shortdesc or module.name,
                                'state': module.state,
                            })
        except Exception:
            pass

        return sorted(custom_modules, key=lambda x: x['name'])

    def _get_installed_modules(self):
        """Get all installed modules"""
        modules = request.env['ir.module.module'].sudo().search([
            ('state', '=', 'installed')
        ])
        return sorted([{
            'id': m.id,
            'name': m.name,
            'shortdesc': m.shortdesc or m.name,
        } for m in modules], key=lambda x: x['name'])

    def _upgrade_module(self, module_id):
        """Upgrade a module"""
        try:
            # Check admin access
            if not request.env.user.has_group('base.group_system'):
                return False, 'Permission denied. Admin access required.'

            # Get the module
            module = request.env['ir.module.module'].sudo().browse(int(module_id))

            if not module.exists():
                return False, 'Module not found'

            # Upgrade the module
            module.button_immediate_upgrade()

            return True, module.name

        except Exception as e:
            return False, str(e)
