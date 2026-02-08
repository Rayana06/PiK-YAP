from data import languages, operators, operator_languages
from logic import *

if __name__ == "__main__":
    print("Запрос 1:")
    print(get_languages_with_c(languages, operators))

    print("\nЗапрос 2:")
    print(get_average_salary_by_language(languages, operators))

    print("\nЗапрос 3:")
    print(get_operators_starting_with_a(operators, languages, operator_languages))