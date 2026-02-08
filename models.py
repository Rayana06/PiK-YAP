class Operator:
    def __init__(self, id_operator, name, salary, id_language=None):
        self.id_operator = id_operator
        self.name = name
        self.salary = salary
        self.id_language = id_language

    def __repr__(self):
        return f"Operator({self.name}, зарплата: {self.salary})"


class ProgrammingLanguage:
    def __init__(self, id_language, name):
        self.id_language = id_language
        self.name = name

    def __repr__(self):
        return f"Language({self.name})"


class OperatorLanguage:
    def __init__(self, id_operator, id_language):
        self.id_operator = id_operator
        self.id_language = id_language