def arithmetic_arranger(problems, displayAnswer=False):
    max_problems = 5
    max_digits = 4
    if len(problems) > max_problems:
        return "Error: Too many problems."
    l, o, r = problems_to_elements(problems)

    for item in o:
        if item != "+" and item != "-":
            return "Error: Operator must be '+' or '-'."

    for item in l:
        if not item.isnumeric():
            return "Error: Numbers must only contain digits."
        if len(item) > max_digits:
            return "Error: Numbers cannot be more than four digits."
    for item in r:
        if not item.isnumeric():
            return "Error: Numbers must only contain digits."
        if len(item) > max_digits:
            return "Error: Numbers cannot be more than four digits."
    result = ""
    result += print_pr_first_line(problems)
    result += print_pr_second_line(problems)
    result += print_br_line(problems)
    if displayAnswer:
        result += "\n" + print_pr_answer_line(problems)
    return result

def print_pr_first_line(problems):
    result_str = ""
    gap = 4*" "
    l, o, r = problems_to_elements(problems)
    for index, item in enumerate(l):
        chunk_len = len(item) if len(item) > len(r[index]) else len(r[index])
        chunk_len += 2
        gap_for_num = (chunk_len - len(item))*" "
        result_str = result_str + gap_for_num + item + gap
    return result_str.rstrip() + "\n"

def print_pr_second_line(problems):
    result_str = ""
    gap = 4*" "
    l, o, r = problems_to_elements(problems)
    for index, item in enumerate(r):
        chunk_len = len(item) if len(item) > len(l[index]) else len(l[index])
        gap_for_num = (chunk_len - len(item) )*" "
        result_str = result_str + o[index] + " " + gap_for_num + item + gap
    return result_str.rstrip() + "\n"

def print_br_line(problems):
    result_str = ""
    gap = 4*" "
    l, o, r = problems_to_elements(problems)
    for index, item in enumerate(r):
        chunk_len = len(item) if len(item) > len(l[index]) else len(l[index])
        chunk_len += 2
        result_str = result_str + chunk_len*"-" + gap
    return result_str.rstrip()

def print_pr_answer_line(problems):
    result_str = ""
    gap = 4*" "
    l, o, r = problems_to_elements(problems)
    for index, item in enumerate(o):
        chunk_len = len(r[index]) if len(r[index]) > len(l[index]) else len(l[index])
        if item == "+":
           answer = int(l[index]) + int(r[index])
        elif item == "-":
           answer = int(l[index]) - int(r[index])
        else:
            print("Error")
        chunk_len = chunk_len + 2 - len(str(answer))
        result_str = result_str + chunk_len*" " + str(answer) + gap
    return result_str.rstrip()

def problems_to_elements(problems):
    pr_elements = []
    l_args = []
    operators = []
    r_args = []
    for problem in problems:
        s_problem = problem.split()
        l_args.append(s_problem[0])
        operators.append(s_problem[1])
        r_args.append(s_problem[2])

    pr_elements.append(l_args)
    pr_elements.append(operators)
    pr_elements.append(r_args)
    return pr_elements