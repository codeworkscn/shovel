#!/usr/bin/python2.7
import os
import sys
import getopt

from shovel import ElasticClient, StringUtils


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


def compare_dictionaries(leftDict, rightDict):
    same = set()
    different = set()
    sameKeySet = set(leftDict.keys()) & set(rightDict.keys())
    for key in sameKeySet:
        if leftDict[key] == rightDict[key]:
            same.add(key)
        else:
            if key not in different:
                different.add(key)
                leftJson = StringUtils.obj_to_json(leftDict[key])
                rightJson = StringUtils.obj_to_json(rightDict[key])
                print("key=%s, leftJson=%s, rightJson=%s" %
                      (key, leftJson, rightJson))
    same_key_count = len(sameKeySet)
    same_count = len(same)
    diffrent_count = len(different)
    print("same_key_count=%d, same_count=%d, diffrent_count=%d" %
          (same_key_count, same_count, diffrent_count))
    return diffrent_count


def execute(leftIndex, rightIndex, queryStmtFile, key_fields):
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

    # print(keyToDocMapLeft)
    # print(keyToDocMapRight)

    unmatched_item_count = compare_dictionaries(
        keyToDocMapLeft, keyToDocMapRight)
    print("unmatched_item_count=%d" % (unmatched_item_count))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(
                argv[1:],
                "hl:r:q:k:",
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

    for o, a in opts:
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
        execute(leftIndex, rightIndex, queryStmtFile, keyFields.split(","))


if __name__ == "__main__":
    sys.exit(main())
