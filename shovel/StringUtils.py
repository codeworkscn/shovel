import json


class StringUtils(object):

    @staticmethod
    def load_json_from_file(file_name):
        with open(file_name) as f:
            data = json.load(f, "UTF-8")
            return data
        return None

    @staticmethod
    def obj_to_json(obj):
        return json.dumps(obj)
