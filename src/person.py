class Person:
    def __init__(self,first_name=None,last_name=None):
        self._first_name = first_name
        self._last_name = last_name
    
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"