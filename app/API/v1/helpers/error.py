
class ErrorModel(Exception):
    def __init__(self, name: str, code: int, success: bool = False):
        self.name = name
        self.code = code
        self.success = success
