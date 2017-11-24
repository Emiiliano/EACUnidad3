#Emiliano Aguilar Cerna GITI9072
class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello"


class Adapter:
    """this changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add new dictionary item that establishes rhe mapping between the generic method name: speak() and the
        # concrete method For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)


# list to store speaker objects
objects = []

#Create a korean objetc
korean = Korean()

#Create a British objetc
british = British()

#Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))

