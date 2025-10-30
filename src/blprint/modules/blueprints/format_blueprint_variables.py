import stringcase

letter_case_functions = {
    "snake_case": lambda x: stringcase.snakecase(x),
    "camel_case": lambda x: stringcase.camelcase(x),
    "pascal_case": lambda x: stringcase.pascalcase(x),
}


def format_blueprint_variables(
    blueprint_variable_codes: list[str], blueprint_variables: dict[str, str]
):
    formatted_blueprint_variables = {}

    for code in blueprint_variable_codes:
        splitted_code = code.split("__")
        name = splitted_code[0]

        if len(splitted_code) > 2 or len(splitted_code) == 0:
            raise (Exception(f"The code {code} is not a valid code"))

        if len(splitted_code) == 1:
            formatted_blueprint_variables[code] = blueprint_variables[name]
            continue

        letter_case = splitted_code[1]

        case_function = letter_case_functions.get(letter_case, None)

        if not case_function:
            raise (Exception(f"The code {code} is not a valid code"))

        formatted_blueprint_variables[code] = case_function(blueprint_variables[name])

    return formatted_blueprint_variables
