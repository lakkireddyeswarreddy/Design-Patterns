
class ConfigurationManager:
    _instance = None
    
    def __new__(cls,app_config : dict):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        cls._instance.__dict__.update(app_config)
        return cls._instance
    
    
if __name__ == "__main__":
    config1_obj = ConfigurationManager({"id" : 1})
    print(config1_obj.__dict__)
    config2_obj = ConfigurationManager({"id" : 2})
    print(config1_obj is config2_obj)
    print(config1_obj.__dict__)
    print(config2_obj.__dict__)

    