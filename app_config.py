
from json_parser import JSONReader

class AppConfig(object):

    def __init__(self, config_file):

        self.app_config = {}

        try:
            config = JSONReader(config_file)
            self.app_config = config.get_json()
        except Exception as e:
            print e

    def get_value(self,key, key2=None):
        try:
            if key2 == None:
                return self.app_config[key]
            else:
                return self.app_config[key][key2]
                
        except Exception as e:
            print e

        return None
