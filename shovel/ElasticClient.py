from datetime import datetime
from elasticsearch import Elasticsearch
from shovel.config import ShovelConfig


class ElasticClient(object):

    def __init__(self):
        esConfig = ShovelConfig.get_configs_by_section("ES")
        esNode = {'host': esConfig['host'], 'port': esConfig['port']}
        self.es = Elasticsearch([esNode])
        try:
            print("ES check connect start")
            self.health()
            print("ES check connect done")
        except Exception as e:
            print("Exception: " + str(e))

    def health(self):
        response = self.es.cat.health()
        print("response=%s" % str(response))
