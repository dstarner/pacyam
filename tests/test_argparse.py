import os
import unittest

from pacyam.pacyam import parse_arguments


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def parse_arg_helper(cli_string):
        argv = cli_string.split(' ')
        return parse_arguments(argv)

class CLITestCase(unittest.TestCase):

    project_root = os.path.join(REPO_ROOT, 'tests', 'project')

    def test_directory(self):
        arguments = f'{self.project_root}'
        options = parse_arg_helper(arguments)
        self.assertEqual(options.directory, self.project_root)

    def test_config(self):
        config = 'hello'

        arguments = f'{self.project_root} --config {config}'
        options = parse_arg_helper(arguments)
        self.assertEqual(options.config_path, config)

        arguments = f'{self.project_root} -c {config}'
        options = parse_arg_helper(arguments)
        self.assertEqual(options.config_path, config)

    def test_load_global_variables(self):
        variables = 'hello=world'

        arguments = f'{self.project_root} -v {variables}'
        options = parse_arg_helper(arguments)
        self.assertEqual(options.vars, [variables])

        arguments = f'{self.project_root} -v {variables}'
        options = parse_arg_helper(arguments)
        self.assertEqual(options.vars, [variables])
