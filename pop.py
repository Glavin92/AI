class STRIPSPlanner:
    def __init__(self, init_state, goal_state, operators):
        # Initialize planner with initial state, goal state, and operators.
        self.init_state = set(init_state)  # Set of initial conditions
        self.goal_state = set(goal_state)  # Set of goal conditions
        self.operators = operators  # List of available operators
        self.plan = []  # List to store the sequence of steps to reach the goal

    def apply_operator(self, state, operator):
        """Applies an operator to a given state."""
        if operator['preconditions'].issubset(state):  # Check if preconditions are satisfied
            # Update state by applying the add and delete effects of the operator
            new_state = (state - operator['del_effects']) | operator['add_effects']
            return new_state, True  # Return new state and success
        return state, False  # Return current state and failure if preconditions are not met

    def achieve_goal(self, state, goal):
        """Finds an operator that can achieve a specific goal."""
        for op in self.operators:
            if goal in op['add_effects']:  # Check if operator can achieve the goal
                return op
        return None  # Return None if no operator found to achieve the goal

    def resolve_threats(self):
        """Resolves threats in the plan."""
        print("Checking for and resolving threats in the plan...")
        return self.plan  # For simplicity, not resolving threats in this example.

    def plan_steps(self):
        """Generates a stepwise plan to achieve the goal state."""
        current_state = self.init_state.copy()  # Start from the initial state
        print("Initial State:", current_state)

        # Loop through the goal states and apply operators to achieve them
        for goal in self.goal_state:
            if goal not in current_state:  # If the goal is not in the current state
                operator = self.achieve_goal(current_state, goal)  # Find an operator to achieve the goal
                if operator:
                    print(f"Applying: {operator['name']}")
                    self.plan.append(operator['name'])  # Add operator to plan

                    current_state, success = self.apply_operator(current_state, operator)  # Apply operator
                    if not success:
                        print("Failed to apply operator for", goal)
                    print("New State:", current_state)

        # Resolve any potential threats (though this part is just a placeholder in this example)
        self.plan = self.resolve_threats()
        print("Final Plan (after threat resolution):", self.plan)


# Example usage for Block World Problem
# Sample Input:
# Initial state: On(C, A), Clear(C), Clear(Table), On(B, Table), Clear(B)
# Goal state: On(C, Table), Clear(A), On(B, C)

init_state = set(input("Enter initial state: ").replace(" ", "").replace("):", ")").split(','))
goal_state = set(input("Enter goal state: ").replace(" ", "").replace("):", ")").split(','))

# Defining operators (actions) available for the planner
operators = [
    {
        'name': 'Move(C, A, Table)',  # Operator name
        'preconditions': {'On(C, A)', 'Clear(C)', 'Clear(Table)'},  # Preconditions
        'add_effects': {'On(C, Table)', 'Clear(A)'},  # Add effects
        'del_effects': {'On(C, A)'}  # Delete effects
    },
    {
        'name': 'Move(B, Table, C)',
        'preconditions': {'On(B, Table)', 'Clear(B)', 'Clear(C)'},
        'add_effects': {'On(B, C)', 'Clear(Table)'},
        'del_effects': {'On(B, Table)'}
    },
    {
        'name': 'Move(A, Table, B)',
        'preconditions': {'On(A, Table)', 'Clear(A)', 'Clear(B)'},
        'add_effects': {'On(A, B)', 'Clear(Table)'},
        'del_effects': {'On(A, Table)'}
    }
]

# Create a planner object with the initial state, goal state, and operators
planner = STRIPSPlanner(init_state, goal_state, operators)

# Start planning process
planner.plan_steps()