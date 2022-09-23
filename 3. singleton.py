class Director:
    _instance = None
    value = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls.value = [items for items in args]
        return cls._instance, cls.value

    # def set_value(self, dir_name):
    #     self.value = dir_name
    #     return self.value



d1 = Director("Директор Петр")
d2 = Director("Директор Серж")

print(d1, d2)
