from KPC_agent import *


class FSM:
    def __init__(self):
        self.state = "INIT"
        self.state = "DONE"
        self.rules = [] #er dette liste over reglene vi legger til? Ja, tenker det foreløpig
        self.switch = {
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
        }

    def add_rule(self, state1, state2, condition, action):
        """add a new rule to the end of the FSM's rule list"""
        rule = Rule(state1, state2, condition, action)
        self.rules.append(rule)

    def get_next_signal(self):
        """query the agent for the next signal"""

    def run_rules(self, signal):
        """go through the rule set, in order, applying each rule until one of the rules is fired"""
        for rule in self.rules:
            if self.apply_rule(signal, rule):
                self.fire_rule(rule)
                return

    def apply_rule(self, signal, rule):
        """check whether the conditions of a rule are met"""
        if rule.get_condition() == signal
            return True
        return False

    def fire_rule(self, rule):
        """use the consequent of a rule to a) set the next state to FSM
        and b) call the appropriate agent action method"""
        old_state, new_state = rule.get_states()
        #TODO gjennomfør rule.get_action()
        self.state = new_state


    def main_loop(self):
        """begin in the FSM's default initial state and then repeatedly call get_next_signal
        and run_rules until the FSM enters its default final stat"""

class Rule:
    """Rule object for implementing a RBS"""

    def __init__(self, state1, state2, condition, action):
        """Konstruktør for regel-klassen"""
        self.state1 = state1
        self.state2 = state2
        self.condition = condition
        self.action = action

    def get_condition(self):
        """Get-funksjon for condition til regelen"""
        return self.condition

    def get_states(self):
        """Get-funksjon som returnerer state1 og state2 som en tuple"""
        return self.state1, self.state2

    def get_action(self):
        """Get-funksjon for handling til regelen"""