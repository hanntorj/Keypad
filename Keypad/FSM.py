from KPC_agent import *

class FSM:
    def __init__(self):
        self.state = "DONE"
        self.rules = [] #er dette liste over reglene vi legger til?
        switch = {
            1: "INIT",
            2: "READ",
            3: "VERIFY",
            4: "ACTIVE",
            5: "LED",
            6: "TIME",
            7: "READ2",
            8: "READ3",
            9: "LOGOUT",
            10: "DONE",
        }'''

    def add_rule(self, state1, state2, input, action):
        ''''add a new rule to the end of the FSM's rule list'''



    def get_next_signal(self):
        '''query the agent for the next signal'''

    def run_rules(self):
        '''go through the rule set, in order, applying each rule until one of the rules is fired'''

    def apply_rule(self):
        '''check whether the conditions of a rule are met'''

    def fire_rule(self):
        '''use the consequent of a rule to a) set the next state to FSM and b) call the appropriate agent action method'''

    def main_loop(self):
        '''begin in the FSM's default initial state and then repeatedly call get_next_signal and run_rules until the FSM enters its default final stat'''

class rule:
    '''Rule object for implementing a RBS'''
