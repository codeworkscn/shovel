#!/usr/bin/python2.7
import os
import sys
import getopt
import pprint
from shovel import ElasticClient, StringUtils

pp = pprint.PrettyPrinter(indent=2)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def usage():
    print '\n\nUsage: \n ' + \
        sys.argv[0] + '--leftIndex <leftIndex> --rightIndex <rightIndex> --queryStmtFile <queryStmtFile> --keyFields <keyFields> '


def key_from_doc(doc, key_fields):
    key = ""
    for field in key_fields:
        key += doc[field]
        key += "."
    return key


def transform_list_to_map(docs, key_fields):
    return {key_from_doc(doc, key_fields): doc for doc in docs}


def compare_dictionaries(leftDict, rightDict, verbose=False):
    same = set()
    different = set()
    leftKeySet = set(leftDict.keys())
    rightKeySet = set(rightDict.keys())

    leftMissKeySet = rightKeySet - leftKeySet
    rightMissKeySet = leftKeySet - rightKeySet
    if leftMissKeySet:
        print("find left missed keys, count=%d, keys:" % len(leftMissKeySet))
        pp.pprint(leftMissKeySet)
    if rightMissKeySet:
        print("find right missed keys, count=%d, keys:" % len(rightMissKeySet))
        pp.pprint(rightMissKeySet)

    sameKeySet = leftKeySet & rightKeySet
    for key in sameKeySet:
        if leftDict[key] == rightDict[key]:
            same.add(key)
            continue
        if key not in different:
            different.add(key)
            leftJson = StringUtils.obj_to_json(leftDict[key])
            rightJson = StringUtils.obj_to_json(rightDict[key])
            if verbose:
                print("find diffrent docs, key=%s, leftJson=%s, rightJson=%s" %
                      (key, leftJson, rightJson))
    same_key_count = len(sameKeySet)
    same_count = len(same)
    diffrent_count = len(different)
    print("same_key_count=%d, same_count=%d, diffrent_count=%d" %
          (same_key_count, same_count, diffrent_count))
    return diffrent_count


def execute(leftIndex, rightIndex, queryStmtFile, key_fields, verbose=False):
    queryStmt = StringUtils.load_json_from_file(queryStmtFile)
    if queryStmt == None:
        print >>sys.stderr, "load query stmt from file failure"
        return

    esClient = ElasticClient()

    docsLeft = esClient.search(leftIndex, "default", queryStmt)
    doc_count_left = len(docsLeft)

    docsRight = esClient.search(rightIndex, "default", queryStmt)
    doc_count_right = len(docsRight)

    print("doc_count_left=%d, doc_count_right=%d" %
          (doc_count_left, doc_count_right))

    keyToDocMapLeft = transform_list_to_map(docsLeft, key_fields)
    keyToDocMapRight = transform_list_to_map(docsRight, key_fields)

    unmatched_item_count = compare_dictionaries(
        keyToDocMapLeft, keyToDocMapRight, verbose)
    print("unmatched_item_count=%d" % (unmatched_item_count))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(
                argv[1:],
                "hvl:r:q:k:",
                ["help",
                 "leftIndex=",
                 "rightIndex=",
                 "queryStmtFile=",
                 "keyFields="])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
            print("verbose mode")
        if o in ("-h", "--help"):
            usage()
            return 0
        elif o in ("-l", "--leftIndex"):
            leftIndex = a
        elif o in ("-r", "--rightIndex"):
            rightIndex = a
        elif o in ("-q", "--queryStmtFile"):
            queryStmtFile = a
        elif o in ("-k", "--keyFields"):
            keyFields = a
        else:
            continue
    if not 'leftIndex' in locals():
        usage()
    elif not 'rightIndex' in locals():
        usage()
    elif not 'queryStmtFile' in locals():
        usage()
    elif not 'keyFields' in locals():
        usage()
    else:
        execute(leftIndex, rightIndex, queryStmtFile,
                keyFields.split(","), verbose)


if __name__ == "__main__":
    sys.exit(main())
