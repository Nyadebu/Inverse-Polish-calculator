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


# stack_rec_op = Stack()
# stack_rec_num = Stack()


def get_operator(op):
    if op == "+" or op == "-" or op == "*" or op == "/" or op == "(" or op == ")":
        return op, True
    else:
        return None, False


def get_number(num):
    if '0' <= num <= '9':
        return num, True
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


def u_input(user):
    char_num = []
    infix_expression = []
    for user_input_ in user:
        number, is_number = get_number(user_input_)
        if is_number:
            char_num.append(number)
            # print(i)
            continue
        j, _j = get_operator(user_input_)
        if _j:
            # print(f'拼接后的数字为', "".join(char_num))
            _nu = "".join(char_num)
            # stack_num.push(_nu)
            infix_expression.append(_nu)
            # print(stack_num.pop())
            char_num.clear()
            infix_expression.append(j)
            # stack_op.push(j)
            # print(stack_op.pop())
            # r_p_n(j)
    # print(f'拼接后的最后一个数字为', "".join(char_num))
    last_num = "".join(char_num)
    # stack_num.push(last_num)
    # print(stack_num.pop())
    infix_expression.append(last_num)
    char_num.clear()
    # if stack_num.is_empty() and stack_op.is_empty() is not True:
    #     print('排空运算栈内符号', stack_op.all())
    ok_expression = [x.strip() for x in infix_expression if x.strip() != '']
    print('-------中缀表达式为-------', ok_expression)
    r_p_n(ok_expression)


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
        print('入栈运算符小于栈顶运算符级别时弹出的',  stack_op.push(op))
    elif op == '(':
        stack_op.push(op)
    # while not stack_op.is_empty() and op_lv(op) <= op_lv(stack_op.get_top()):
    #     result.append(stack_op.pop())
    # stack_op.push(op)


def r_p_n(ok_expression):
    for char in ok_expression:
        num_, is_num_ = get_number(char)
        if is_num_:
            print('读取入栈的数字为', char)
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
        if is_num_:
            stack_result.push(res)
        if not is_num_:
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
u_input(user_input)

# https://zhuanlan.zhihu.com/p/65110137
# https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95
