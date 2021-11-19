# test if the object works good.


class MerveilleObject:
    """this class should be the base class of everything in Merveille. 
    Any object that has mass, should be considered under this class.
    """
    
    _object_list = []  # Question: how to quickly find certain object in this list?
    
    @classmethod
    def find(cls, by_id=None, by_function=None):
        pass
    
    def __init__(self, name) -> None:
        self._name = name  # Question: is there has to be a name on anonymous thing? would there be any anonymous thing?
        # self._mass = mass  # mass is not necessary because map object does not have mass.
        self._id = id(self)  # considering if I should take id as it is or made by hand.
        MerveilleObject._object_list.append(self)
    
    def describe(self):
        attrs = {
            'name': self._name,
            'id': self._id,
        }
        return attrs

