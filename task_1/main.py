from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

def create_production_model():
    """
    Creates and solves a linear programming model for maximizing the production of lemonade and juice.
    """
    # Create the optimization model
    model = LpProblem("Maximize_Production", LpMaximize)

    # Define decision variables
    lemonade = LpVariable("Lemonade", lowBound=0, cat="Continuous")
    juice = LpVariable("Juice", lowBound=0, cat="Continuous")

    # Objective function: maximize total products
    model += lpSum([lemonade, juice]), "Total_Products"

    # Constraints on resources
    model += (2 * lemonade + juice <= 100, "Water_Constraint")
    model += (lemonade <= 50, "Sugar_Constraint")
    model += (lemonade <= 30, "Lemon_Juice_Constraint")
    model += (2 * juice <= 40, "Fruit_Puree_Constraint")

    # Solve the model
    model.solve()

    return model, lemonade, juice

def display_results(model, lemonade, juice):
    """
    Displays the results of the optimized production model.
    """
    print("Status:", LpStatus[model.status])
    print("Lemonade:", value(lemonade))
    print("Juice:", value(juice))
    print("Total Products:", value(model.objective))

def main():
    # Create the production model and get results
    production_model, lemonade_var, juice_var = create_production_model()
    display_results(production_model, lemonade_var, juice_var)

if __name__ == "__main__":
    main()
