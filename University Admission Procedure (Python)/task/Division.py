from enum import Enum
from Student import Student

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
        self.applicants.sort(key=lambda x: (-x.get_score(), x.name), reverse=False)
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