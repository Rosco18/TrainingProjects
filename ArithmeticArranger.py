def arithmetic_arranger(problems, result=True):

    # Empty List to hold each line of each problem
    line1 = ""          # To hold the first line of each of the problems
    line2 = ""          # To hold the second line of each of the problems
    line3 = ""          # The third line for underlining dashes
    line4 = ""          # The fourth line of each problem (the answer)
    # Create rule for first Error if more than 5 problems
    if len(problems) > 5:
        return("Error: Too many problems.")
    else:
        for problem in problems:
            #  Remove unwanted spaces
            problem = problem.replace(' ', '')
            # Check all problems have "+" or "-" only
            if "+" in problem:
                # Splitting characters in problem using "+" as the delimiter
                problem = problem.split("+")
                operator = "+"
            elif "-" in problem:
                # Splitting characters in problem using "-" as the delimiter
                problem = problem.split("-")
                operator = "-"
            else:
                # Second Error: Only "+" and "-" only
                return("Error: Operator must be a + or a -.")

            # Third Error: Check problems only contain intergers
            if not(problem[0].isnumeric() or problem[1].isnumeric()):
                return("Error: Numbers only contain digits.")
            # Fourth Error: Check problems only contain max 6 digits per number
            if len(problem[0]) > 4 or len(problem[1]) > 4:
                return("Error: Numbers can't be more than 4 digits.")

            # Getting number of digits contained in the promblem with the longest digits (adding 2 to it). This determines the number characters that a line can have in each arranged problem
            align = max([len(problem[0]), len(problem[1])]) + 2

            # Evaluating the concatenation of the problem and the operator with the 'eval' function
            if result:
                # Using eval to go from str to ing back to str to concatenate
                answer = str(eval(problem[0] + operator + problem[1]))
                # Concatenating the result of the expression with the contained digits rightly-just to the string [line4]
                line4 += answer.rjust(align) + "    "

            # Concatenating to string, first Operand, rightly-just
            line1 += problem[0].rjust(align) + "    "
            # Concatenating to string, operator and the second operand, rightly-just
            line2 += operator + problem[1].rjust(align - 1) + "    "
            # Concatenating to string, the underlining (bunch of dashes)
            line3 += "-" * (align) + "    "

        # Joining line 1 - 3 into a single string, separated by a newline character
        arranged_problems = "\n".join([line1, line2, line3])

        if result:
            line4 = line4.rstrip()    # Adding the fourth line with the result
            arranged_problems += "\n" + line4 + "\n" + line3 + "    "

        return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 + 49"]))
