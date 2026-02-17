def calculate(expression: str) -> float:
    tokens = expression.replace(' ', '')
    nums = []
    ops = []
    
    i = 0
    while i < len(tokens):
        if tokens[i] in '+-*/':
            ops.append(tokens[i])
            i += 1
        else:
            j = i
            while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
                j += 1
            nums.append(float(tokens[i:j]))
            i = j

    # Handle * and /
    i = 0
    while i < len(ops):
        if ops[i] == '*':
            nums[i] = nums[i] * nums[i+1]
            nums.pop(i+1)
            ops.pop(i)
        elif ops[i] == '/':
            nums[i] = nums[i] / nums[i+1]
            nums.pop(i+1)
            ops.pop(i)
        else:
            i += 1

    # Handle + and -
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i+1]
        else:
            result -= nums[i+1]

    return round(result, 2)
