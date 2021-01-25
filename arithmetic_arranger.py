
def arithmetic_arranger(problems, with_answer = False):

    if len(problems) > 5 :
        return 'Error: Too many problems.'

    left_operands = ''
    right_operands = ''
    dashes = ''
    answers = ''

    for problem in problems :

        p = problem.split()

        result = 0
        try :
            if p[1] == '+' :
                result = int(p[0]) + int(p[2])
            elif p[1] == '-' :
                result = int(p[0]) - int(p[2])
            else :
                return 'Error: Operator must be \'+\' or \'-\'.'
        except ValueError :
            return 'Error: Numbers must only contain digits.'

        left_operand_size = len(p[0])
        right_operand_size = len(p[2])
        if left_operand_size > 4 or right_operand_size > 4 :
            return 'Error: Numbers cannot be more than four digits.'

        if left_operand_size < right_operand_size :
            left_operand = p[0].rjust(right_operand_size + 2)
            right_operand = p[1] + ' ' + p[2]
            answer = str(result).rjust(right_operand_size + 2)
        else :
            left_operand = '  ' + p[0]
            right_operand = p[1] + p[2].rjust(left_operand_size + 1)
            answer = str(result).rjust(left_operand_size + 2)

        left_operands += left_operand + '    '
        right_operands += right_operand + '    '
        dashes += get_dashes(len(right_operand)) + '    '
        answers += answer + '    '

    arranged_problems = left_operands.rstrip() + '\n' + right_operands.rstrip() + '\n' + dashes.rstrip()
    if with_answer :
        arranged_problems += '\n' + answers.rstrip()
    return arranged_problems

def get_dashes(nb):
    dashes = ''
    for i in range(nb):
        dashes += '-'
    return dashes
