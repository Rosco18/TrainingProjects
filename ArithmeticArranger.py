def arithmetic_arranger(problems):
    # Create rule for Error if more than 5 problems
    if len(problems) > 5:
        return("Error: Too many problems.")
    else:
        for problem in problems:
            #  Remove unwanted spaces
            problem = problem.replace(' ', '')
            # Check all problems have + or -.
            if "+" in problem:
                problem = problem.split("+")
            elif "-" in problem:
                problem = problem.split("-")
            else:
                return("Error: Operator must be a + or a -.")

            # Check problems only contain intergers.
            if not(problem[0].isnumeric() or problem[1].isnumeric()):
                return("Error: Numbers only contain digits.")
            # Check problems only contain max 4 digits per number.
            if len(problem[0]) > 4 or len(problem[1]) > 4:
                return("Error: Numbers can't be more than 4 digits.")


# return arranged_problems
print(arithmetic_arranger(["32 + 698", "32365 + 698", "32 - 698", "32 + 698", "82 + 698"]))
