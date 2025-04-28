class STRIPSPlanner:
    def __init__(self, init_state, goal_state, operators):
        self.init_state = set(init_state) 
        self.goal_state = set(goal_state)
        self.operators = operators
        self.plan = [] 

    def apply_operator(self, state, operator):
        if operator['preconditions'].issubset(state):
            new_state = (state - operator['del_effects']) | operator['add_effects']
            return new_state, True
        return state, False  

    def achieve_goal(self, state, goal):
        for op in self.operators:
            if goal in op['add_effects']: 
                return op
        return None  

    def resolve_threats(self):
        print("Checking for and resolving threats in the plan...")
        return self.plan  

    def plan_steps(self):
        current_state = self.init_state.copy()  
        print("Initial State:", current_state)

        for goal in self.goal_state:
            if goal not in current_state:  
                operator = self.achieve_goal(current_state, goal)  
                if operator:
                    print(f"Applying: {operator['name']}")
                    self.plan.append(operator['name'])  

                    current_state, success = self.apply_operator(current_state, operator)  
                    if not success:
                        print("Failed to apply operator for", goal)
                    print("New State:", current_state)

        self.plan = self.resolve_threats()
        print("Final Plan (after threat resolution):", self.plan)


# Initial state: On(C, A), Clear(C), Clear(Table), On(B, Table), Clear(B)
# Goal state: On(C, Table), Clear(A), On(B, C)

init_state = set(input("Enter initial state: ").replace(" ", "").replace("):", ")").split(','))
goal_state = set(input("Enter goal state: ").replace(" ", "").replace("):", ")").split(','))

operators = [
    {
        'name': 'Move(C, A, Table)',
        'preconditions': {'On(C, A)', 'Clear(C)', 'Clear(Table)'},
        'add_effects': {'On(C, Table)', 'Clear(A)'},
        'del_effects': {'On(C, A)'}
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

planner = STRIPSPlanner(init_state, goal_state, operators)

planner.plan_steps()