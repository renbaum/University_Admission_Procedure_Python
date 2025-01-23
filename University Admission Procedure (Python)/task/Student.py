from enum import Enum
from unittest import case

import Division

class ResultsDepartment(Enum):
    Physics = 0
    Chemistry = 1
    Math = 2
    Computer_Science = 3



class Student:
    def __init__(self, first: str, last: str, score: list, divisions: list):
        self.score = {}
        self.first = first
        self.last = last
        for rs in ResultsDepartment:
            self.score[rs.name] = int(score[rs.value])
        self.divisions = divisions

    @property
    def name(self):
        return f"{self.first} {self.last}"

    def get_division(self) -> str:
        if len(self.divisions) > 0:
            return self.divisions[0]
        return Division.DepartmentNames.Rejected.value

    def reject(self):
        if len(self.divisions) > 0:
            self.divisions.pop(0)

    def is_rejected(self) -> bool:
        return len(self.divisions) == 0

    def get_score(self) -> float:
        match self.get_division():
            case Division.DepartmentNames.Engineering.value:
                return self.score[ResultsDepartment.Computer_Science.name]
            case Division.DepartmentNames.Mathematics.value:
                return self.score[ResultsDepartment.Math.name]
            case Division.DepartmentNames.Physics.value:
                return self.score[ResultsDepartment.Physics.name]
            case Division.DepartmentNames.Chemistry.value:
                return self.score[ResultsDepartment.Chemistry.name]
            case Division.DepartmentNames.Biotech.value:
                return self.score[ResultsDepartment.Chemistry.name]


        return self.score

    def is_primary(self) -> bool:
        return len(self.divisions) == 3
