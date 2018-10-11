import os
import unittest

from pacyam.pacyam import Configuration, BuildException

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ConfigurationTestCase(unittest.TestCase):

    test_configs_root = os.path.join(REPO_ROOT, 'tests', 'test-configs')
    project_root = os.path.join(REPO_ROOT, 'tests', 'project')

    def test_invalid_root_dir(self):
        root = 'totes-invalid-dir'
        config_path = 'config.json'
        with self.assertRaises(BuildException):
            Configuration.load(
                root_directory=root,
                config_file_name=config_path,
            )

    def test_missing_config_path(self):
        root = self.test_configs_root
        config_path = 'not-available-config.json'
        with self.assertRaises(BuildException):
            Configuration.load(
                root_directory=root,
                config_file_name=config_path
            )

    def test_invalid_json_file(self):
        root = self.test_configs_root
        config_path = 'bad_json.json'
        with self.assertRaises(BuildException):
            Configuration.load(
                root_directory=root,
                config_file_name=config_path
            )

    def test_unique_config_path(self):
        root = self.test_configs_root
        config_path = 'some-unique-name.json'
        config = Configuration.load(
            root_directory=root,
            config_file_name=config_path
        )
        self.assertTrue(
            os.path.basename(config.config_file_path),
            config_path
        )
        self.assertEqual(config.root_directory, root)

    def test_invalid_config(self):
        root = self.test_configs_root
        config_path = 'config.json'
        with self.assertRaises(BuildException):
            Configuration.load(
                root_directory=root,
                config_file_name=config_path
            )

    def test_template_paths(self):
        root = self.project_root
        config_path = 'config.json'
        config = Configuration.load(
            root_directory=root,
            config_file_name=config_path
        )
        expected = [
            "builders/virtualbox.yaml",
            "builders/virtualbox.yaml",
            "post-processors/vagrant.yaml",
            "provisioners/core.yaml"
        ]
        self.assertEqual(config.template_paths, expected)

    def test_variable_paths(self):
        root = self.project_root
        config_path = 'config.json'
        config = Configuration.load(
            root_directory=root,
            config_file_name=config_path
        )
        expected = [
            "variables/default.yaml"
        ]
        self.assertEqual(config.variable_paths, expected)
