from models.goal import Goal

class GoalController:
    def add_goal(self, description, target_amount, current_amount=0):
        goal = Goal(description, target_amount, current_amount)
        goal.save()
    
    def get_all_goals(self):
        return Goal.get_all()
