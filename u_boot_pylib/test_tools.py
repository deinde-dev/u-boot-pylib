# SPDX-License-Identifier: GPL-2.0+
# Copyright 2026 Simon Glass <sjg@chromium.org>

"""Tests for the u_boot_pylib.tools module"""

import os
import shutil
import tempfile
import unittest
import unittest.mock

from u_boot_pylib import tools


class TestRunEnv(unittest.TestCase):
    """Tests for the environment used by tools.run()"""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix='test_tools.')

    def tearDown(self):
        shutil.rmtree(self.tmpdir)
        tools.set_tool_paths(None)

    def _run_env(self, **kwargs):
        """Run a tool which prints the value of two environment variables"""
        return tools.run('sh', '-c', 'echo "$TEST_VAR:$PATH"',
                         for_target=False, **kwargs).strip()

    def test_run_env(self):
        """Test that run() uses the environment it is given"""
        env = dict(os.environ, TEST_VAR='given')
        with unittest.mock.patch.dict(os.environ, {'TEST_VAR': 'parent'}):
            self.assertEqual(f"given:{os.environ['PATH']}",
                             self._run_env(env=env))
            self.assertEqual(f"parent:{os.environ['PATH']}", self._run_env())

    def test_run_env_tool_paths(self):
        """Test that run() puts the tool paths first in a given environment"""
        tools.set_tool_paths([self.tmpdir])
        env = dict(os.environ, TEST_VAR='given')
        self.assertEqual(f"given:{self.tmpdir}:{os.environ['PATH']}",
                         self._run_env(env=env))

    def test_get_env_with_path(self):
        """Test adding the tool paths to an environment"""
        self.assertIsNone(tools.get_env_with_path())
        env = {'PATH': '/bin'}
        self.assertIs(env, tools.get_env_with_path(env))

        tools.set_tool_paths([self.tmpdir])
        self.assertEqual({'PATH': f'{self.tmpdir}:/bin'},
                         tools.get_env_with_path(env))
        self.assertEqual({'PATH': '/bin'}, env)
        self.assertEqual({'PATH': f'{self.tmpdir}:'},
                         tools.get_env_with_path({}))
        self.assertEqual(f"{self.tmpdir}:{os.environ['PATH']}",
                         tools.get_env_with_path()['PATH'])

    def test_run_missing_tool(self):
        """Test the error for a missing tool with a given environment"""
        tools.set_tool_paths([self.tmpdir])
        with self.assertRaises(ValueError) as exc:
            tools.run('no-such-tool', env={'PATH': self.tmpdir})
        self.assertIn("Please install tool 'no-such-tool'", str(exc.exception))
