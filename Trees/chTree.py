"""
    Company Hierarchy Tree

"""
class CompanyHierarchyTreeNode:
    def __init__(self, staff):
        self.name, self.position = staff
        self.below = []
        self.up = None

    def get_level(self):
        level = 0
        p = self.up
        while p:
            level += 1
            p = p.up

        return level 

    def add_staff(self,staff):
        staff.up = self
        self.below.append(staff)

    def print_hierarchy(self, cmd):
        spaces = " "*self.get_level()*3

        prefix = spaces +"|--" if self.up else ""
        if cmd == "name":
            print(prefix + self.name)
        elif cmd == "designation":
            print(prefix + self.position)
        elif cmd == "both":
            print(prefix + self.name +"("+self.position+")")
        else:
            print("Use can pass \"name, designation or both as a parameter\". ")

        for emp in self.below:
            emp.print_hierarchy(cmd)

def build_tree():
    ceo = CompanyHierarchyTreeNode(("Nilupul", "CEO"))

    cto = CompanyHierarchyTreeNode(("Chinmay", "CTO"))
    ih = CompanyHierarchyTreeNode(("Vishwa", "Infrastructure Head"))
    ih.add_staff(CompanyHierarchyTreeNode(("Dhaval", "Cloud Manager")))
    ih.add_staff(CompanyHierarchyTreeNode(("Abhijit", "App Manager")))

    cto.add_staff(ih)
    cto.add_staff(CompanyHierarchyTreeNode(("Aamir", "Application Head")))

    hr = CompanyHierarchyTreeNode(("Gels", "HR Head"))
    hr.add_staff(CompanyHierarchyTreeNode(("Peter", "Recruitment Manager")))
    hr.add_staff(CompanyHierarchyTreeNode(("Waqas", "Policy Manager")))    
    
    ceo.add_staff(cto)
    ceo.add_staff(hr)

    return ceo

if __name__ == "__main__":
    ct = build_tree()
    ct.print_hierarchy("designation")