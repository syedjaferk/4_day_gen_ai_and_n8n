from tools import (
    get_all_employees,
    get_employees_by_department,
    get_high_salary_employees,
)

TOOLS = [
    {"name": "get_all_employees", "description": "Get all employees", "parameters": {}},
    {
        "name": "get_employees_by_department",
        "description": "Get employees by department",
        "parameters": {"department": "string"},
    },
    {
        "name": "get_high_salary_employees",
        "description": "Get employees with salary greater than given amount",
        "parameters": {"min_salary": "integer"},
    },
]


FUNCTION_MAP = {
    "get_all_employees": get_all_employees,
    "get_employees_by_department": get_employees_by_department,
    "get_high_salary_employees": get_high_salary_employees,
}
