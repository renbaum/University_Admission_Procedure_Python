import shutil
import os
from Division import DepartmentNames, Division
from Student import Student




class University:
    def __init__(self, name: str, number_of_applicants: int):
        self.divisions = {}
        for department in DepartmentNames:
            if department == DepartmentNames.Rejected: continue
            self.divisions[department.value] = Division(department.value, number_of_applicants)

        self.copy_file("applicants.txt", "applicants_copy.txt")
        self.students = self.load_applicants("applicants.txt")

        self.deploy_student()

    def deploy_student(self):
        while len(self.students) != 0:
            self.students.sort(key=lambda x: (x.get_division(), -x.get_score(), x.name), reverse=False)
            rejected_students = []
            for student in self.students:
                reject = self.place_applicant(student)
                if reject is not None and not reject.is_rejected():
                    rejected_students.append(reject)
            self.students = rejected_students

    def copy_file(self, source: str, destination: str):
        if os.path.exists(source):
            shutil.copyfile(source, destination)

    def load_applicants(self, filename: str) -> list:
        student_list = []
        
        with open(filename, "r") as file:
            for line in file:
                applicant = line.strip().split()
                student_list.append(Student(applicant[0], applicant[1], applicant[2:6], applicant[6:]))
        return student_list
    
    def place_applicant(self, applicant: Student) -> Student | None:
        if applicant.is_rejected(): return None
        return self.divisions[applicant.get_division()].add_applicant(applicant)

#        while not applicant.is_rejected():
#            next_applicant = self.divisions[applicant.get_division()].add_applicant(applicant)
#            if next_applicant is None:
#                break
#            applicant = next_applicant

    def print_applicants(self):
        for key, division in self.divisions.items():
            print(f"{division.name}:")
            division.print_applicants()
    
if __name__ == "__main__":
    number_of_applicants = int(input())
    university = University("University of Information Technology", number_of_applicants)

    university.print_applicants()
