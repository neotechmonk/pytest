class Person:
    def __init__(self,first_name=None,last_name=None, age=0):
        if not first_name or not last_name:
            raise ValueError("First and last names must have values")
        
        if not age or 100 > age < 0:
            raise ValueError("Age must be between 0 and 100")
        

        self._first_name = first_name
        self._last_name = last_name
    
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
    
 