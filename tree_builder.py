class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name 
        self.left = None 
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None
    
    def insert(self, manager_name, employee_name, side, current_node=None):
        if current_node is None:
            current_node = self.root
        
        if current_node and current_node.name == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                print(f"{employee_name} added to the left of {manager_name}.")
            elif side == "right" and current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                print(f"{employee_name} added to the right of {manager_name}.")
            else:
                print(f" The {side} side has already been filled or side is invalid.")
        elif current_node is not None:
            if current_node.left:
                self.insert(manager_name, employee_name, side, current_node.left)
            if current_node.right:
                self.insert(manager_name, employee_name, side, current_node.right)
        else:
            print(f"Manager {manager_name} could not be found.")

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return
        print(" " * (level * 2) + f" - {node.name}")

        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

    
    












def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")   
#design memo should be around 249 words
#In my code the recursive insertion worked by traversing the tree, during this traverail it was searching for the target manager where the new employee specified should be placed. To further break it down during the course of the search if the current node was already none it would stop the recursion as it would have reached a leaf node that could not go further. When inserting an employee depending if the side that is desired by the user is free, a new employee node would be created and would be added to that side. If the current node was not the target it will search by calling insert on both the left and right subtrees, this will ensure that no matter where the manager is in the tree the method will continue searching the entire tree until the manager is found. The biggest challenges I faced when trying to find the right spot for the new employee where running into various complications such as a side being occupied or a manager not being found, and lastly if the tree were to continue to grow it will become increasingly difficult to run it efficiently cases may arise where there are too many employees on one side compared to the other. The best scenarios where trees would be useful in real examples would be in file systems, indexing a database, even in some basic games such as tic-tac-toe as the tree could represent possible moves for an AI to do. 
