def calculate_solution_weights(molecular_weights: dict[str, float], solutions_needed: list[str]) -> list[str]:
    """
    :param molecular_weights: A dictionary whose keys are the chemical formula of the solution and whose values are the corresponding molecular weights in grams per mole
    :param solutions_needed: A list whose elements are strings that contain the chemical formula and molarity of the desired solution 
    :return: A list whose elements are strings that contain the chemical formula, molarity, and solute mass of the desired solution
    """
    
    def parse_molarity_and_chemical_formula(solution: str) -> tuple[float, str]:
        """
        A helper function used to parse the molarity and chemical formula from the solutions_needed
        :param solution: A string that contains the chemical formula and molarity of the desired solution 
        :return: A tuple whose first element is the molarity and second element is the chemical formula 
        """
        solution_split = solution.split("-")
        molarity = float(solution_split[1].split("M")[0])
        chemical_formula = solution_split[0]
        return molarity, chemical_formula
    
    def get_whole_output(solution: str) -> str:
        """
        A helper function that computes the solute mass, constructs the final output, and handles the case where the chemical formula is not in our list of known molecular weights
        :param solution: A string that contains the chemical formula and molarity of the desired solution 
        :return: A string containing the chemical formula, molarity, and solute mass of the desired solution 
        """
        molarity, chemical_formula = parse_molarity_and_chemical_formula(solution)
        if chemical_formula in molecular_weights:  # check if the chemical formula is in our list of known molecular weights
            return f"{chemical_formula}-{molarity}M-{molarity * molecular_weights[chemical_formula]:.2f}g" # the .2f rounds the output to two digits
        else:
            return "unknown"
         
    return list(map(get_whole_output, solutions_needed))  # perform this operation on all elements of the input list
    

