
from P4 import P4, P4Exception
from shovel.config import ShovelConfig


class P4Client(object):

    def __init__(self):
        self.p4Config = ShovelConfig.get_configs_by_section("P4")
        self.integrateConfig = ShovelConfig.get_configs_by_section(
            "P4integrate")

        self.p4 = P4()
        p4 = self.p4

        p4Config = self.p4Config
        p4.port = p4Config["port"]
        p4.user = p4Config["user"]
        p4.password = p4Config["passwd"]
        p4.client = p4Config["client"]

        try:
            print("p4 connect start")
            p4.connect()
            print("p4 connect done")
        except P4Exception as e:
            print("P4Exception: " + str(e))
        except Exception as e:
            print("Exception: " + str(e))

    def __del__(self):
        try:
            self.p4.disconnect()
        except Exception as e:
            print("Exception: " + str(e))

    def get_p4(self):
        return self.p4

    def p4_describe_changelist(self, changeId):
        describe = self.p4.run("describe", changeId)
        print("describe : %s" % str(describe))
        return describe

    # return changelist id
    def p4_new_changelist(self, description=""):
        changespec = self.p4.fetch_change()
        if not description:
            description = "Merging changelist, auto created changelist by Shovel utils"

        changespec["Files"] = []
        changespec["Description"] = description
        result = self.p4.save_change(changespec)
        print("result : %s" % str(result))

        results = result[0].split()
        if results[0] == "Change" and results[2] == "created.":
            changeId = results[1]
        else:
            changeId = "0"
        print("new changelist created, changeId=%s" % changeId)
        return changeId

    def p4_list_changelist_by_job(self, jobName):
        assert jobName, "jobName is empty"
        argv = ["fixes"]
        argv.append("-j")
        argv.append(jobName)

        detailList = self.p4.run(argv)
        detailListCount = len(detailList)
        print("list changelist by job, found detailListCount=%d" %
              detailListCount)

        changelistList = []
        for detail in detailList:
            print("detail=%s" % str(detail))
            changelistList.append(detail["Change"])

        changelistList.reverse()
        return changelistList

    def p4_integrate_by_changelist(self, source, target, changelist, saveToChangeId=""):
        assert source, "source is empty"
        assert target, "target is empty"

        sourceScope = '{0}@{1},@{1}'.format(source, changelist)

        # print("integrate changelist start, changelist=%s" % changelist)
        # print("from: %s \n to:%s" % (sourceScope, target))

        argv = ["integrate"]
        if saveToChangeId:
            argv.append("-c")
            argv.append(saveToChangeId)
        argv.append(sourceScope)
        argv.append(target)

        try:
            result = self.p4.run(argv)
            print("integrate changelist done, changelist=%s" % changelist)
        except P4Exception as ex:
            exception_str = str(ex)
            if "already integrated" in exception_str or "no such file" in exception_str:
                print(
                    "integrate changelist skipped due already integrated, changelist=%s" % changelist)
                return ""
            else:
                print("integrate changelist failure, changelist=%s" % changelist)
                raise ex

        return result

    def p4_integrate_by_changelists(self, source, target, changelists, saveToChangeId=""):
        assert changelists, "changelists is empty"
        if not source:
            source = self.integrateConfig['source']
        if not target:
            target = self.integrateConfig['target']

        print("integrate_by_changelists start\n\tfrom: %s \n\tto:%s" %
              (source, target))

        for changelist in changelists:
            self.p4_integrate_by_changelist(
                source, target, changelist, saveToChangeId)

        print("integrate_by_changelists done, saveToChangeId=%s" % saveToChangeId)

    def p4_resolve_accept_merge_by_change(self, changeId):
        try:
            # result = self.p4.run("resolve", "-am", "-c", changeId)
            # result too large, avoid output
            self.p4.run("resolve", "-am", "-c", changeId)
            print("resolve by changeId done, changeId=%s" % changeId)
        except P4Exception as ex:
            print("resolve by changeId failure, changeId=%s, exceptionDetails=%s" % (
                changeId, str(ex)))
