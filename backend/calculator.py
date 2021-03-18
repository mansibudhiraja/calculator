def sum(operand1, operand2):
    return operand1 + operand2


def subtract(operand1, operand2):
    return operand1 - operand2


operator_to_func_map = {
    '+': sum,
    '-': subtract
}


def is_operator_supported(operator):
    return operator in ['+', '-']


def perform_operation(oper1, oper2, operator):
    if not is_operator_supported(operator):
        return -1
    return operator_to_func_map[operator](oper1, oper2)

