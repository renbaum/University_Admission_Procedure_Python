from enum import Enum
import shutil
import os

class Student:
    def __init__(self, first: str, last: str, score: float, divisions: list):
        self.first = first
        self.last = last
        self.score = score
        self.divisions = divisions

    @property
    def name(self):
        return f"{self.first} {self.last}"
    
    def get_division(self) -> str:
        if len(self.divisions) > 0:
            return self.divisions[0]
        return DepartmentNames.Rejected.value
    
    def reject(self):
        if len(self.divisions) > 0:
            self.divisions.pop(0)
            
    def is_rejected(self) -> bool:
        return len(self.divisions) == 0
    
    def get_score(self) -> float:
        return self.score

    def is_primary(self) -> bool:
        return len(self.divisions) == 3
    
class Division:
    def __init__(self, name: str, number_of_applicants: int):
        self.applicants = []
        self.name = name
        self.number_of_applicants = number_of_applicants

    def add_applicant(self, applicant: Student) -> Student | None:
        if len(self.applicants) < self.number_of_applicants:
            self.applicants.append(applicant)
            return None

        applicant.reject()
        return applicant

    def print_applicants(self):
        self.applicants.sort(key=lambda x: (-x.score, x.name), reverse=False)
        for applicant in self.applicants:
            print(f"{applicant.first} {applicant.last} {applicant.get_score()}")
        print()

class DepartmentNames(Enum):
    Biotech = "Biotech"
    Chemistry = "Chemistry"
    Engineering = "Engineering"
    Mathematics = "Mathematics"
    Physics = "Physics"
    Rejected = "Rejected"


class University:
    def __init__(self, name: str, number_of_applicants: int):
        self.divisions = {}
        for department in DepartmentNames:
            if department == DepartmentNames.Rejected: continue
            self.divisions[department.value] = Division(department.value, number_of_applicants)

        self.copy_file("applicants.txt", "applicants_copy.txt")
        self.students = self.load_applicants("applicants.txt")
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
                student_list.append(Student(applicant[0], applicant[1], float(applicant[2]), applicant[3:]))
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
