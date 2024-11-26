def format_linter_error(error: dict) -> dict:

    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors": [format_linter_error(element) for element in errors
                   if element != {}],
        "path": file_path,
        "status": "passed" if len([format_linter_error(element)
                                   for element in errors
                                   if element != {}]) == 0 else "failed"
    }


def format_linter_report(linter_report: dict) -> list:

    return [format_single_linter_file(key, item)
            for key, item in linter_report.items()]
