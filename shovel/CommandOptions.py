import argparse
import sys


class CommandOptions(object):

    def __init__(self, prog=sys.argv[0]):
        parser = argparse.ArgumentParser(prog)
        parser.add_argument('--source', help='source file name')
        parser.add_argument('--target', help='target file name')

        self.parser = parser

    def get_parse(self):
        return self.parser

    def parse_args(self):
        return self.parser.parse_args()

    def print_usage(self):
        self.parser.print_usage()
