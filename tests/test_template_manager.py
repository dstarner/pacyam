import os
import unittest

from pacyam.pacyam import TemplateManager, VariableManager


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_variable_manager(root, variable_strings=None):
    return VariableManager([], root, variable_strings)

class TemplateManagerTestCase(unittest.TestCase):

    project_root = os.path.join(REPO_ROOT, 'tests', 'test-configs')

    def test_static_template(self):
        template_files = [
            'templates/static.yaml'
        ]
        expected = {
            'builders': [
                {'type': 'qemu', 'vm_name': 'ubuntu-1804'}
            ]
        }

        variable_manager = create_variable_manager(self.project_root)

        manager = TemplateManager(
            variable_manager,
            template_files,
            self.project_root
        )
        data = manager.merge_template_data()
        self.assertEqual(data, expected)

    def test_templated_template(self):
        template_files = [
            'templates/templated.yaml'
        ]
        expected = {
            'builders': [
                {'type': 'qemu', 'vm_name': 'ubuntu-1804'}
            ]
        }

        variable_manager = create_variable_manager(self.project_root, ['type=qemu'])

        manager = TemplateManager(
            variable_manager,
            template_files,
            self.project_root
        )
        data = manager.merge_template_data()
        self.assertEqual(data, expected)
