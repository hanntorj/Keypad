
class FSM:
        '''Holds a pointer back to the agent, since it will make many requests to the KCP'''

        def add_rule(self):
            '''add a new rule to the end of the FSM's rule list'''
        def get_next_signal(self):
            '''query the agent for the next signal'''
        def run_rules(self):
            '''go through the rule set, in order, applying each rule until one of the rules is fired'''
        def apply_rule(self):
            '''check whether the conditions of a ruøe are met'''
        def fire_rule(self):
            '''use the consequent of a rule to a) set the next state to FSM and b) call the appropriate agent action method'''
        def main_loop(self):
            '''begin in the FSM's default initial state and then repeatedly call get_next_signal and run_rules until the FSM enters its default final stat'''
def hanna():
    print("hei")

    
