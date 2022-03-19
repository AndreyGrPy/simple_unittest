#this is simple calculator function
def calculator(expression):
    allowed = "+-/*"
    if not any(sing in expression for sing in allowed):
        raise ValueError(f"Expression must contain at least one character({allowed})")
    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                if sing == "+":
                    return left + right
                elif sing == "-":
                    return left - right
                elif sing == "/":
                    return left / right
                elif sing == "*":
                    return left * right
            except (ValueError, TypeError):
                raise ValueError("Expression must contain 2 int numbers and 1 sing")


if __name__ == "__main__":
    print(calculator("2+2"))