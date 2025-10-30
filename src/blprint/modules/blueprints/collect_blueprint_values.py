def collect_blueprint_variables(variable_names: list[str]):
    variables = {}

    for variable_name in variable_names:
        value = input(f"Value for '{variable_name}': ")
        variables[variable_name] = value

    return variables
