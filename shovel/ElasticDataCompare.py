#!/usr/bin/python2.7
import os
import sys
import getopt

from shovel import ElasticClient, ShovelConfig


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def usage():
    print '\n\nUsage: \n ' + sys.argv[0] + ' -j <job> | --job <job>'


def execute(leftIndex, rightIndex, queryStmt):
    esClient = ElasticClient()


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(
                argv[1:], "hl:r:q:", ["help", "leftIndex=", "rightIndex=", "queryStmt="])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            return 0
        elif o in ("-l", "--leftIndex"):
            leftIndex = a
        elif o in ("-r", "--rightIndex"):
            rightIndex = a
        elif o in ("-q", "--queryStmt"):
            queryStmt = a
        else:
            continue
    if not 'leftIndex' in locals():
        usage()
    elif not 'rightIndex' in locals():
        usage()
    elif not 'queryStmt' in locals():
        usage()
    else:
        execute(leftIndex, rightIndex, queryStmt)


if __name__ == "__main__":
    sys.exit(main())
