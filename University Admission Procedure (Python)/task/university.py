
class Student:
    def __init__(self, first: str, last: str, score: float):
        self.first = first
        self.last = last
        self.score = score

    @property
    def name(self):
        return f"{self.first} {self.last}"

class Division:
    def __init__(self, name: str, number_of_applicants: int):
        self.applicants = []
        self.name = name
        self.number_of_applicants = number_of_applicants

    def add_applicant(self, applicant: Student) -> bool:
        if len(self.applicants) < self.number_of_applicants:
            self.applicants.append(applicant)
            return True
        return False

    def print_applicants(self):
        for applicant in self.applicants:
            print(f"{applicant.first} {applicant.last}")

if __name__ == "__main__":
    total_students = int(input())
    number_of_applicants = int(input())
    division = Division("First Division", number_of_applicants)
    lst = []
    for _ in range(total_students):
        first, last, score = input().split()
        lst.append(Student(first, last, float(score)))

    lst.sort(key=lambda x: (-x.score, x.name), reverse=False)
    for student in lst:
        division.add_applicant(student)

    print("Successful applicants:")
    division.print_applicants()