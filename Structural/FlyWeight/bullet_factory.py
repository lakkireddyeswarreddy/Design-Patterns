from bullet_type import BulletType

class BulletFactory:
    _models = dict()
    
    @classmethod
    def get_bullet_type(cls, type, color):
        key = (type,color)
        if key not in cls._models:
            cls._models[key] = BulletType(type,color)
            print(f"Creating new bullet type : {type}, {color}")
        else:
            print(f"Reusing the existing bullet type : {type}, {color}")
        return cls._models[key]