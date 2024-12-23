class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.projects = []

    def assign_to_project(self, project):
        if project.add_employee(self):
            self.projects.append(project)
            print(f"{self.name} successfully assigned to {project.title}")
        else:
            print(f"{self.name} could not be assigned to {project.title} (project may be full)")

    def view_assigned_projects(self):
        if not self.projects:
            print(f"{self.name} is not assigned to any projects.")
        else:
            print(f"{self.name} is assigned to the following projects:")
            for project in self.projects:
                print(f" - {project.title}")


class Project:
    def __init__(self, title, manager, max_employees):
        self.title = title
        self.manager = manager
        self.max_employees = max_employees
        self.employees = []

    def add_employee(self, employee):
        if len(self.employees) < self.max_employees:
            self.employees.append(employee)
            return True
        return False

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            employee.projects.remove(self)
            print(f"{employee.name} removed from {self.title}")
        else:
            print(f"{employee.name} is not assigned to {self.title}")

    def view_assigned_employees(self):
        if not self.employees:
            print(f"No employees are assigned to {self.title}.")
        else:
            print(f"The following employees are assigned to {self.title}:")
            for emp in self.employees:
                print(f" - {emp.name}")


# Sample Usage
employee1 = Employee("John Doe", 101)
employee2 = Employee("Jane Smith", 102)
employee3 = Employee("Alice Johnson", 103)

project1 = Project("Project A", "Manager X", 2)
project2 = Project("Project B", "Manager Y", 3)

employee1.assign_to_project(project1)
employee2.assign_to_project(project1)
employee3.assign_to_project(project1)  # This will fail because the project is full

employee1.view_assigned_projects()
employee3.view_assigned_projects()

project1.view_assigned_employees()
project2.view_assigned_employees()
