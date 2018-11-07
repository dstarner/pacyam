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
        arguments = self.project_root
        options = parse_arg_helper(arguments)
        self.assertEqual(options.directory, self.project_root)

    def test_config(self):
        config = 'hello'

        arguments = '%s --config %s' % (self.project_root, config)
        options = parse_arg_helper(arguments)
        self.assertEqual(options.config_path, config)

        arguments = '%s -c %s' % (self.project_root, config)
        options = parse_arg_helper(arguments)
        self.assertEqual(options.config_path, config)

    def test_load_global_variables(self):
        variables = 'hello=world'

        arguments = '%s -v %s' % (self.project_root, variables)
        options = parse_arg_helper(arguments)
        self.assertEqual(options.vars, [variables])
