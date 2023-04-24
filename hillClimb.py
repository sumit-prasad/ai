import random

# Define the objective function to be optimized
def objective_function(x):
    return x**2 + 5*x + 10

# Define the hill climbing algorithm
def hill_climbing(max_iter=1000, step_size=0.1):
    # Start from a random solution
    current_solution = random.uniform(-10, 10)
    
    # Evaluate the current solution
    current_score = objective_function(current_solution)
    
    # Iterate until the maximum number of iterations is reached or no improvement is possible
    for i in range(max_iter):
        # Generate a new candidate solution by adding a small random value to the current solution
        candidate_solution = current_solution + random.uniform(-step_size, step_size)
        
        # Evaluate the candidate solution
        candidate_score = objective_function(candidate_solution)
        
        # If the candidate solution is better, update the current solution
        if candidate_score < current_score:
            current_solution = candidate_solution
            current_score = candidate_score
        
        # If no improvement is possible, exit the loop
        else:
            break
    
    # Return the best solution found
    return current_solution, current_score

# Test the hill climbing algorithm
best_solution, best_score = hill_climbing()
print(f"Best solution: {best_solution}, Best score: {best_score}")
