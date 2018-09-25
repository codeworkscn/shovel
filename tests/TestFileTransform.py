# -*- coding: utf-8 -*-
import os
import os.path
import shutil
import unittest

from context import shovel
from shovel import FileTransform


class TestFileTransform(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        output_directory = 'tests/output'
        shutil.rmtree(output_directory, ignore_errors=True)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    def test_json2csv(self):
        source_file_name = 'tests/resources/sample-source-ascii.json'
        target_file_name = 'tests/output/sample-target-ascii.csv'
        FileTransform.json2csv(source_file_name, target_file_name)
        self.assertTrue(os.path.isfile(target_file_name))

    def test_csv2json(self):
        source_file_name = 'tests/resources/sample-source-ascii.csv'
        target_file_name = 'tests/output/sample-target-ascii.json'
        FileTransform.csv2json(source_file_name, target_file_name)
        self.assertTrue(os.path.isfile(target_file_name))


if __name__ == '__main__':
    unittest.main()
