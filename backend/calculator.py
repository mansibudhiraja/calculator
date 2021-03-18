def sum(operand1, operand2):
    return operand1 + operand2


def subtract(operand1, operand2):
    return operand1 - operand2

def multiplication(operator1, operator2):
    return operator1 * operator2

def division(operator1, operator2):
    if operator2 == 0:
        raise Exception("division by zero not allowed")
    else:
        return operator1 /operator2

operator_to_func_map = {
    '+': sum,
    '-': subtract,
    '*': multiplication,
    '/': division
}


def is_operator_supported(operator):
    return operator in ['+', '-', '*', '/']



def perform_operation(oper1, oper2, operator):
    if not is_operator_supported(operator):
        raise Exception ("Operator not supported")
    return operator_to_func_map[operator](oper1, oper2)

