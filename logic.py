def get_languages_with_c(languages, operators):
    result = {}
    for lang in languages:
        if "C" in lang.name:
            ops = [op.name for op in operators if op.id_language == lang.id_language]
            result[lang.name] = ops
    return result


def get_average_salary_by_language(languages, operators):
    result = {}
    for lang in languages:
        lang_ops = [op.salary for op in operators if op.id_language == lang.id_language]
        if lang_ops:
            result[lang.name] = round(sum(lang_ops) / len(lang_ops), 2)
        else:
            result[lang.name] = None
    return result


def get_operators_starting_with_a(operators, languages, relations):
    result = {}
    for op in operators:
        if op.name.startswith("А"):
            langs = [
                lang.name
                for rel in relations
                for lang in languages
                if rel.id_operator == op.id_operator
                and rel.id_language == lang.id_language
            ]
            result[op.name] = langs
    return result