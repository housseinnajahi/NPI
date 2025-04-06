def evaluate_npi(tokens: list[str]) -> float:
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            if len(stack) < 2:
                raise Exception(f"Not enough operands for operator '{token}'.")
            b = stack.pop()
            a = stack.pop()
            try:
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise Exception("Division by zero.")
                    stack.append(a / b)
            except Exception as e:
                raise Exception(f"Error during calculation: {str(e)}")
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise Exception(f"Invalid non-numeric value: '{token}'.")

    if len(stack) != 1:
        raise Exception("Malformed expression. Stack contains extra elements.")

    return stack.pop()
