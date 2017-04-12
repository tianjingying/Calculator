import re

def init_action(expression):
    """
    # 初始化表达式
    :param expression: "-1-20*-3"
    :return: res   ['-1', '-', '20', '*', '-3']
    """
    res = []
    tag = False
    char = ""
    for i in expression:
        if i.isdigit():
            tag = True
            char += i
        else:
        # 不是数字，就是符号
            if tag:
                #遇到符号，且之前有数字
                if i == ".":
                    # 解决遇到小数的情况
                    char += i
                else:
                    res.append(char)
                    char = ""
                    res.append(i)
                    tag = False
            else:
                #遇到符号，之前没数字
                if i == "-":
                    char = i
                else:
                    res.append(i)
                pass
    if len(char) > 0:
        res.append(char)
    return res

def delete_space(expression):
    res = ""
    for i in expression:
        if i == " ":
            continue
        res += i
    pass
    return res

def priority(exp , opt_list):
    """
    判断优先级
    :param exp:  当前符号
    :param opt_list:   符号栈
    :return:">" 当前符号优先级大于栈顶元素优先级
            "<"  当前符号优先级小于栈顶元素优先级
             "=" : 当前符号优先级等于栈顶元素优先级
    """
    laval1 = ["+","-"]
    laval2 = ["*","/"]
    if exp in laval1:
        if opt_list[-1] in laval1:
            # 都是 + —  同一优先级
            return "="
        else:
            return "<"
    if exp in laval2:
        if opt_list[-1] in laval2 :
            return "="
        elif opt_list[-1] in laval1:
            return ">"


def compute(num1, opt, num2 ):
    """
    计算
    :param num1: 第一操作数
    :param opt: 运算符
    :param num2: 第二操作数
    :return:
    """
    if opt == "+":
        return num1 + num2
    elif opt == "-" :
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    elif opt == "/" :
        return num1 / num2
    else:
        return None

def calculate(exp_list):
    number_list = []
    opt_list = []
    symbol_list = ["+","-","*","/","(",")"]
    tag = False
    for exp in exp_list:
        if exp not in symbol_list:
            #是数字
            exp = float(exp)
            if not tag:
                number_list.append(exp)
            else:
                tag = False
                num2 = exp
                num1 = number_list.pop()
                opt = opt_list.pop()
                result = compute(num1, opt, num2)
                # print("result111  : %s"%result)
                # print("num1  : %s" % num1)
                # print("opt  : %s" % opt)
                # print("num2  : %s" % num2)
                number_list.append(result)
        else:
            # 是符号
            if len(opt_list) == 0 :
                opt_list.append(exp)
            else:
                if priority(exp , opt_list) == "=" or priority(exp , opt_list) == "<":
                    # 可以计算
                    num1 = 0
                    num2 = 0
                    opt = opt_list.pop()
                    if len(number_list) >= 2:
                        num2 = number_list.pop()
                        num1 = number_list.pop()
                        result = compute(num1, opt, num2 )
                        # print("result : %s"%result)
                        number_list.append(result)
                        opt_list.append(exp)
                    else:
                        print("输入的表达式有误，不能运算")
                        return None
                elif  priority(exp , opt_list) == ">":
                    tag = True
                    opt_list.append(exp)

    # print("number_list : %s"%number_list)
    # print("opt_list : %s" % opt_list)
    if len(number_list) == 2 and len(opt_list) == 1:
        pass
        num2 = number_list.pop()
        num1 = number_list.pop()
        opt = opt_list.pop()
        return compute(num1, opt, num2)
    else:
        print("输入的表达式有误，不能运算")
        return None

if __name__ == "__main__":
    # expression = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    # expression = "-1 + 2-3 + 4 + 5+8"
    # expression = "2*2+3*4-22*6+4"
    # expression = "2*2+(3*(4-22)*6)*2+(4+5)-4"
    while True:
        expression = input("请输入表达式： ").strip()
        expression = delete_space(expression)
        # print("expression : %s"%expression)
        while True:
            match = re.search(r'\([^()]+\)',expression)
            if not match:
                break
            else:
                exp = match.group()
                exp_list = init_action(exp[1:-1])
                # print("exp_list : %s"%exp_list)
                cal_result = calculate(exp_list)
                # print("cal_result:%s"%cal_result)
                tmp = expression.replace(exp,str(cal_result))
                expression = tmp
                # print("expression: %s"%expression)

        # print("expression--22  : %s"%expression)

        exp_list = init_action(expression)
        # print("exp_list : %s"%exp_list)
        cal_result = calculate(exp_list)
        print("计算结果:%s"%cal_result)





