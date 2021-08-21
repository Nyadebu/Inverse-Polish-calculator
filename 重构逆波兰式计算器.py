class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(data, "开始插入了")

    def pop(self):
        if len(self.stack) > 0:
            t = self.stack.pop()
            print("从栈中弹出的为", t)
            return t

    def get_top(self):
        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def all(self):
        self.stack.reverse()
        return self.stack[:]

    def clear(self):
        self.stack.clear()


stack_num = Stack()
stack_op = Stack()
result = []
stack_result = Stack()


def get_number(num):
    if '0' <= num <= '9':
        return num, True
    else:
        return None, False


def get_operator(op):
    if op == "+" or op == "-" or op == "*" or op == "/" or op == "(" or op == ")":
        return op, True
    else:
        return None, False


def op_lv(_opp):
    if _opp == '(' or _opp == ')':
        return 0
    elif _opp == '+':
        return 1
    elif _opp == '-':
        return 1
    elif _opp == '*':
        return 2
    elif _opp == '/':
        return 2


def to_int(_int):
    try:
        _int = int(_int)
        return _int
    except TypeError as e:
        print(f"bad value: {e} {type(e)}")
    except Exception as e:
        print(f"error occurred: {e} {type(e)}")


def compare_op(op):
    if stack_op.is_empty():
        print('栈为空时 加入的运算符为', stack_op.push(op), op)
    elif op_lv(op) > op_lv(stack_op.get_top()) and op != '(':
        print('插入运算符比站内运算符大，直接存入', stack_op.push(op))
    elif op_lv(op) == op_lv(stack_op.get_top()) and op != '(':
        print('入栈运算符和栈顶运算符级别相同时弹出的', )
        result.append(stack_op.pop())
        stack_op.push(op)
    elif op_lv(op) <= op_lv(stack_op.get_top()) and op != '(':
        result.append(stack_op.get_top())
        stack_op.pop()
        while not stack_op.is_empty() and op_lv(op) <= op_lv(stack_op.get_top()):
            result.append(stack_op.get_top())
            stack_op.pop()
        print('入栈运算符小于栈顶运算符级别时弹出的', stack_op.push(op))
    elif op == '(':
        stack_op.push(op)


def expression(user_input_):
    char_num = []
    infix_expression = []
    for char in user_input_:
        number, is_number = get_number(char)
        op, is_op = get_operator(char)
        if len(infix_expression) == 0:
            if len(char_num) == 0 and char == '-':
                char_num.append(char)
                print('负号')
            elif char == '(':
                infix_expression.append(char)
                print('跨号')
            elif is_number:
                char_num.append(number)
                print('数字', number)
            else:
                get_num = "".join(char_num)
                print('-----空列表插入的数字为-----', get_num)
                infix_expression.append(get_num)
                char_num.clear()
                infix_expression.append(char)
                print('第一个符号', char)
        else:
            if infix_expression[-1] == '(' and char == '-':
                if len(char_num) == 0:
                    char_num.append(char)
                    print('非头部负号插入')
                elif char_num[0] == '-':
                    get_num = "".join(char_num)
                    infix_expression.append(get_num)
                    print('打印出char_num', char_num)
                    print('识别到符号', op, '合并数字', get_num)
                    char_num.clear()
                    infix_expression.append(op)
                    print('符号写入', op)
                else:
                    get_num = "".join(char_num)
                    infix_expression.append(get_num)
                    print('打印出char_num', char_num)
                    print('识别到符号', op, '合并数字', get_num)
                    char_num.clear()
                    infix_expression.append(op)
                    print('符号写入', op)
            elif infix_expression[-1] == '+' or infix_expression[-1] == '-' or infix_expression[-1] == '*' or \
                    infix_expression[-1] == '/':
                if char == '-' and len(char_num) == 0:
                    print('-以及char_num为空')
                    char_num.append(char)
                elif is_number:
                    print('符号后写入的数字', char)
                    char_num.append(char)
                else:
                    get_num = "".join(char_num)
                    infix_expression.append(get_num)
                    print('infix列表[-1]为符号')
                    print('打印出char_num', char_num)
                    print('识别到符号', op, '合并数字', get_num)
                    char_num.clear()
                    infix_expression.append(op)
                    print('符号写入', op)
            elif is_number:
                char_num.append(number)
                print('非头部数字插入char_num组', char)
            elif is_op:
                print('已进入符号判定')
                get_num = "".join(char_num)
                infix_expression.append(get_num)
                print('打印出char_num', char_num)
                print('识别到符号', op, '合并数字', get_num)
                char_num.clear()
                infix_expression.append(op)
                print('符号写入', op)
            else:
                print('Error')
    last_num = "".join(char_num)
    infix_expression.append(last_num)
    char_num.clear()
    ok_expression = [x.strip() for x in infix_expression if x.strip() != '']
    print('-------中缀表达式为-------', ok_expression)
    r_p_n(ok_expression)


def r_p_n(ok_expression):
    for char in ok_expression:
        num_, is_num_ = get_number(char)
        op_, is_op_ = get_operator(char)
        if is_num_:
            print('读取入栈的数字为', char)
            stack_num.push(char)
            result.append(char)
            stack_num.pop()
            continue
        elif not is_op_:
            print('读取入栈的负数为', char)
            stack_num.push(char)
            result.append(char)
            stack_num.pop()
            continue
        elif char != ')' and char != '(':
            compare_op(char)
        elif char == ')':
            while not stack_op.get_top() == '(':
                print('识别到右）')
                result.append(stack_op.get_top())
                print('处理右）吐出运算符', stack_op.pop())
            print('识别到左（抛弃的元素', stack_op.pop())
        else:
            compare_op(char)
    if stack_num.is_empty() and stack_op.is_empty() is not True:
        # result.append(stack_op.all())
        result.extend(stack_op.all())
        print('排空运算栈内符号', stack_op.all())
    print('r_p_n', result)
    _result(result)


def _result(_res):
    for res in _res:
        num_, is_num_ = get_number(res)
        op_, is_op_ = get_operator(res)
        if is_num_:
            stack_result.push(res)
        elif not is_op_:
            stack_result.push(res)
        if is_op_:
            num_a = to_int(stack_result.stack[-2])
            num_b = to_int(stack_result.stack[-1])
            stack_result.pop()
            stack_result.pop()
            if res == '+':
                cal_result = num_a + num_b
                stack_result.push(cal_result)
            elif res == '-':
                cal_result = num_a - num_b
                stack_result.push(cal_result)
            elif res == '*':
                cal_result = num_a * num_b
                stack_result.push(cal_result)
            elif res == '/':
                cal_result = num_a / num_b
                stack_result.push(cal_result)
    print('-------后缀式计算结果为-------', stack_result.pop())


user_input = input('请输入需要计算的公式：')
expression(user_input)
