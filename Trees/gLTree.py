"""
    Global location tree
"""
from sre_parse import State


class GLTree:
    def __init__(self, location) -> None:
        self.location = location
        self.places = []
        self.parent = None

    def add_place(self, place):
        place.parent = self
        self.places.append(place)
    
    def get_level(self):
        level = 0
        p = self.parent

        while p != None:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):      
        if self.get_level() <= level:
            spaces = " "* self.get_level()*3
            prefix = spaces +" |--" if self.parent else " "
            print(prefix+self.location)

        for place in self.places:
            place.print_tree(level)


def build_tree():
    globe = GLTree("Global")
    # print("Globe Level: {}".format(globe.get_level()))

    india = GLTree("India")
    
    Gujarat = GLTree("Gujarat")
    Gujarat.add_place(GLTree("Ahmedabad"))
    Gujarat.add_place(GLTree("Baroda"))
    
    Karnataka = GLTree("Karnataka")
    Karnataka.add_place(GLTree("Bangluru"))
    Karnataka.add_place(GLTree("Mysore"))

    india.add_place(Gujarat)
    india.add_place(Karnataka)

    usa = GLTree("USA")
    New_Jersey = GLTree("New Jersey")
    New_Jersey.add_place(GLTree("Priceton"))
    New_Jersey.add_place(GLTree("Trenton"))

    California = GLTree("California")
    California.add_place(GLTree("San Francisco"))
    California.add_place(GLTree("Mountain View"))
    California.add_place(GLTree("Palo Alto"))

    usa.add_place(New_Jersey)
    usa.add_place(California)

    globe.add_place(india)
    globe.add_place(usa)
    # print("India Level: {}".format(india.get_level()))
    # print("Gujarat Level: {}". format(Gujarat.get_level()))

    # print("USA Level: {}".format(usa.get_level()))
    # print("New Jersey Level: {}". format(New_Jersey.get_level()))


    return globe

if __name__=="__main__":
    tree = build_tree()
    tree.print_tree(3)

    