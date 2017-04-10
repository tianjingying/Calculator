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

if __name__ == "__main__":
    print("main")
    # expression = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    expression = "-1 - 20*-(3+4)"
    expression = delete_space(expression)
    print("expression : %s"%expression)
    exp_list = init_action(expression)
    print("exp_list : %s"%exp_list)

