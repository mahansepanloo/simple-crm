import copy  

class Prototype:  
    def __init__(self, obj):  
        self.obj = obj  

    def clone(self, **kwargs):  
        cloned_obj = copy.deepcopy(self.obj) 
        cloned_obj.pk = None 
        cloned_obj.__dict__.update(kwargs)  
        return cloned_obj