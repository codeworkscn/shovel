# -*- coding: utf-8 -*-

from collections import OrderedDict
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
        res = self.es.cat.health()
        print("res=%s" % str(res))

    def order_by_field_name(self, dict):
        return OrderedDict(sorted(dict.items(), key=lambda t: t[0]))

    def search(self, index, indexType, body):
        res = self.es.search(index, indexType, body)
        hits = res["hits"]["hits"]
        return map(lambda doc: self.order_by_field_name(doc["_source"]), hits)

    def get_elasticsearch(self):
        return self.es
