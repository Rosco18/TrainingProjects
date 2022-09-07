def arithmetic_arranger(problems, result=True):

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    # Create rule for Error if more than 5 problems
    if len(problems) > 6:
        return("Error: Too many problems.")
    else:
        for problem in problems:
            #  Remove unwanted spaces
            problem = problem.replace(' ', '')
            # Check all problems have "+" or "-" only.
            if "+" in problem:
                problem = problem.split("+")
                operator = "+"
            elif "-" in problem:
                problem = problem.split("-")
                operator = "-"
            else:
                return("Error: Operator must be a + or a -.")

            # Check problems only contain intergers.
            if not(problem[0].isnumeric() or problem[1].isnumeric()):
                return("Error: Numbers only contain digits.")
            # Check problems only contain max 4 digits per number.
            if len(problem[0]) > 6 or len(problem[1]) > 6:
                return("Error: Numbers can't be more than 4 digits.")

            align = min([len(problem[0]), len(problem[1])]) + 2

            if result:
                answer = str(eval(problem[0] + operator + problem[1]))
                line4 += answer.center(align) + "    "

            line1 += problem[0].center(align) + "    "
            line2 += operator + problem[1].center(align - 1) + "    "
            line3 += "-" * (align) + "    "

        arranged_problems = "\n".join([line1, line2, line3])

        if result:
            line4 = line4.rstrip()
            arranged_problems += "\n" + line4 + "\n" + line3 + "    "

        return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "12356 + 94965"]))
