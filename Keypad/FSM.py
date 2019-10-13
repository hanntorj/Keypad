from KPC_agent import *
from KPC_agent import KPC

class FSM:
    """Klasse for finite state machine"""

    def __init__(self, agent):
        self.state = "INIT"
        self.agent = agent
        self.rules = []  # er dette liste over reglene vi legger til? Ja, tenker det foreløpig
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
        self.signal = None
        self.add_rule(self.switch[1], self.switch[2], FSM.all, agent.init_passcode_entry)

    def add_rule(self, state1, state2, condition, action):
        """add a new rule to the end of the FSM's rule list"""
        rule = Rule(state1, state2, condition, action)
        self.rules.append(rule)

    def get_next_signal(self):
        """query the agent for the next signal"""
        self.signal = self.agent.get_next_signal()

    def run_rules(self, signal):
        """go through the rule set, in order, applying each rule until one of the rules is fired"""
        for rule in self.rules:
            if self.apply_rule(signal, rule):
                self.fire_rule(rule)
                break

    def apply_rule(self, signal, rule):
        """check whether the conditions of a rule are met"""
        return rule.check_rule(self.state, signal)

    def fire_rule(self, rule):
        """use the consequent of a rule to a) set the next state to FSM
        and b) call the appropriate agent action method"""
        self.state = rule.state2
        rule.action()

    def main_loop(self):
        """begin in the FSM's default initial state and then repeatedly call get_next_signal
        and run_rules until the FSM enters its default final stat"""
        


class Rule:
    """Rule object for implementing a RBS"""

    def __init__(self, state1, state2, condition, action):
        """
        Konstruktør for klassen
        :param state1: Tilstand som FSM skal være i for at regelen skal utføres
        :param state2: Tilstand som FSM skal sendes til etter regelen er utført
        :param condition: Input fra Keypad for at regelen skal utførses
        :param action: Handling som skjer dersom condtions er møtt
        """
        self.state1 = state1
        self.state2 = state2
        self.condition = condition
        self.action = action

    def check_rule(self, state, signal):
        """
        Metode som sjekker om en regel skal fyres eller ikke
        :param state: str?
        :param signal: str
        :return: boolean
        """
        return self.state1 == state and signal in self.signal

