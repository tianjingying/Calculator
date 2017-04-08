def init_action(expression):
    """
    # 初始化表达式
    :param expression: "10+20"
    :return: res   ['10', '+', '20']
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
                res.append(char)
                char = ""
                res.append(i)
                tag = False
    if len(char) > 0:
        res.append(char)
    print("res: %s"%res)
    return res

if __name__ == "__main__":
    print("main")
    # expression = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    expression = "10+20"
    exp_list = init_action(expression)

