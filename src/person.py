class Person:
    def __init__(self,first_name=None,last_name=None):
        if not first_name or not last_name:
            raise ValueError("First and last names must have values")
        
        self._first_name = first_name
        self._last_name = last_name
    
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"