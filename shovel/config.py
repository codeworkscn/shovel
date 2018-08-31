import yaml

class ShovelConfig(object):

    config_dict = {}

    with open("shovel_config.yaml", 'r') as stream:
        try:
            config_dict = yaml.load(stream)     
            print("shovel config loaded")       
        except yaml.YAMLError as exc:
            print(exc)
        
    @staticmethod
    def get_config(section, key):
        return ShovelConfig.config_dict[section][key]

    @staticmethod
    def get_configs_by_section(section):
        return ShovelConfig.config_dict[section]
