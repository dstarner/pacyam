import os
import unittest

from pacyam.pacyam import VariableManager


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class VariableManagerTestCase(unittest.TestCase):

    project_root = os.path.join(REPO_ROOT, 'tests', 'test-configs')

    def test_basic_variables(self):
        variable_files = [
            'variables/basic.yaml'
        ]
        expected = {
            'disk_device': '/dev/sda',
            'preseed_location': 'preseed-vb.cfg',
            'version': 0.1
        }

        manager = VariableManager(
            variable_files,
            self.project_root
        )
        variables = manager.variables
        self.assertEqual(variables, expected)

    def test_templated_variables(self):
        variable_files = [
            'variables/templated.yaml'
        ]
        expected = {
            'disk_device': '/dev/sda',
            'headless': True,
            'iso_checksum': 'a5b0ea5918f850124f3d72ef4b85bda82f0fcd02ec721be19c1a6952791c8ee8',
            'os': 'ubuntu-18.04.1-server-amd64',
            'iso_checksum_type': 'sha256',
            'iso_url': 'iso/ubuntu-18.04.1-server-amd64.iso',
            'preseed_location': 'preseed-vb.cfg',
            'ssh_password': 'vagrant',
            'ssh_username': 'vagrant',
            'version': 0.1,
            'vm_name': 'ubuntu-18.04.1-server-amd64'
        }

        manager = VariableManager(
            variable_files,
            self.project_root
        )
        variables = manager.variables
        self.assertEqual(variables, expected)

    def test_list_variables(self):
        variable_files = [
            'variables/list.yaml'
        ]
        expected = {'not_list': 'hello', 'some_list': ['val1', 'val2']}

        manager = VariableManager(
            variable_files,
            self.project_root
        )
        variables = manager.variables
        self.assertEqual(variables, expected)

    def test_global_variables(self):
        variable_files = [
            'variables/list.yaml'
        ]
        expected = {'not_list': 'world', 'some_list': ['val1', 'val2']}

        manager = VariableManager(
            variable_files,
            self.project_root,
            global_variables=['not_list=world']
        )
        variables = manager.variables
        self.assertEqual(variables, expected)
