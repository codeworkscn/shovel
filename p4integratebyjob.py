#!/usr/bin/python2.7
import os
import sys
import getopt

from shovel import P4Client, ShovelConfig

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def usage():
  print '\n\nUsage: \n ' + sys.argv[0] + ' -j <job> | --job <job>'

def execute(jobName):
  p4Client = P4Client()
  changelistsToMerge = p4Client.p4_list_changelist_by_job(jobName)
  print("changelistsToMerge=%s" % str(changelistsToMerge))

  saveToChangeId = p4Client.p4_new_changelist()
  print("saveToChangeId=%s" % saveToChangeId)

  integrateConfig = ShovelConfig.get_configs_by_section("P4integrate")
  source = integrateConfig["source"]
  target = integrateConfig["target"]

  p4Client.p4_integrate_by_changelists(source,target,changelistsToMerge,saveToChangeId)
  print("integrate done, jobName=%s, saveToChangeId=%s" % (jobName, saveToChangeId))

  p4Client.p4_resolve_accept_merge_by_change(saveToChangeId)

  print("\n\nauto resolve accept merge done, there may remain some conflict need manual check")
  print("please check pending changelist [%s], add comment, then submit your changes." % saveToChangeId)

def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "hvj:", ["help", "job="])
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
    elif o in ("-h", "--help"):
      usage()
      return 0         
    elif o in ("-j", "--job"):
      jobName = a            
    else:
      continue
  if not 'jobName' in locals():
    usage()
  else:    
    execute(jobName)

if __name__ == "__main__":
  sys.exit(main())
