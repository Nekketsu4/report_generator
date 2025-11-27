from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: List[str]
    team: str
    experience_years: int
