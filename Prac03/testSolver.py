import EquationSolver as es

equation = "( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )"
print("\nEquation to solve: ", equation)
es.solve(equation)

equation = str(input("\nEnter an equation (ensure spaces between everything): "))
es.solve(equation)