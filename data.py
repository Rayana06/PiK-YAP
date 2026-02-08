from models import Operator, ProgrammingLanguage, OperatorLanguage

languages = [
    ProgrammingLanguage(1, "Python"),
    ProgrammingLanguage(2, "C++"),
    ProgrammingLanguage(3, "JavaScript"),
]

operators = [
    Operator(1, "Алиса", 85000, 1),
    Operator(2, "Борис", 90000, 2),
    Operator(3, "Андрей", 75000, 1),
    Operator(4, "Виктор", 95000, 3),
    Operator(5, "Алина", 88000, 2),
]

operator_languages = [
    OperatorLanguage(1, 1),
    OperatorLanguage(1, 2),
    OperatorLanguage(2, 2),
    OperatorLanguage(3, 1),
    OperatorLanguage(3, 3),
    OperatorLanguage(4, 3),
    OperatorLanguage(5, 1),
    OperatorLanguage(5, 2),
]