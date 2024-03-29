"""Package for finite state machine"""
from KPC_agent import *
import pdb

""""""


class FSM:
    """Klasse for finite state machine"""
    all = '#*0123456789'

    def __init__(self, agent):
        """Initializer for the FSM class."""
        self.run = True
        self.state = "INIT"
        self.agent = agent
        self.rules = []
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
            11: "LED",
            12: "TIME"
        }
        self.signal = ''
        self.setup_rules()

    def setup_rules(self):
        """this method adds all our basic rules for this project in particular.
        Our final state machine is designed to be used in any given project in need of a FSM, this method
        simply adds the rules of this given assignment."""
        """Ruleset for initializer"""
        self.add_rule(self.switch[1], self.switch[2], FSM.all, self.agent.init_passcode_entry)

        # Lesing av passord (READ -> READ/VERIFY/INIT)
        """Ruleset for read-password"""
        self.add_rule(self.switch[2], self.switch[2], FSM.all[2:], self.agent.append_password_buffer)
        self.add_rule(self.switch[2], self.switch[3], FSM.all[1], self.agent.verify_login)
        self.add_rule(self.switch[2], self.switch[1], FSM.all, self.agent.reset_all_variables)

        # Verifisering av passord (VERIFY -> ACTIVE/INIT)
        """Ruleset for verifying password"""
        self.add_rule(self.switch[3], self.switch[4], "Y", self.agent.init_passcode_entry)
        self.add_rule(self.switch[3], self.switch[1], FSM.all, self.agent.init_passcode_entry)

        # Powerdown prosess
        """Ruleset for shutting down the RPI"""
        self.add_rule(self.switch[4], self.switch[9], FSM.all[0], self.agent.nothing)
        self.add_rule(self.switch[9], self.switch[1], FSM.all[0], self.agent.power_down)
        self.add_rule(self.switch[1], self.switch[2], FSM.all, self.agent.nothing)

        # Forandring av passord:
        """Ruleset for changing the password"""
        self.add_rule(self.switch[4], self.switch[7], FSM.all[1], self.agent.nothing)
        self.add_rule(self.switch[4], self.switch[4], FSM.all, self.agent.nothing)
        self.add_rule(self.switch[7], self.switch[7], FSM.all[2:], self.agent.append_new_pass)
        self.add_rule(self.switch[7], self.switch[4], FSM.all[0], self.agent.reset_all_variables)
        self.add_rule(self.switch[7], self.switch[8], FSM.all[1], self.agent.nothing)
        self.add_rule(self.switch[8], self.switch[8], FSM.all[2:], self.agent.append_new_pass_check)
        self.add_rule(self.switch[8], self.switch[4], FSM.all[1], self.agent.validate_passcode_change)
        self.add_rule(self.switch[8], self.switch[4], FSM.all[0], self.agent.reset_all_variables)

        # Opplysing av LEDS
        """Ruleset for the visual feedback in form of LEDs on the breadboard"""
        self.add_rule(self.switch[4], self.switch[11], FSM.all[2:8], self.agent.set_led)
        self.add_rule(self.switch[11], self.switch[12], FSM.all[1], self.agent.nothing)
        self.add_rule(self.switch[11], self.switch[4], FSM.all, self.agent.reset_all_variables)
        self.add_rule(self.switch[12], self.switch[12], FSM.all[2:], self.agent.append_Ldur)
        self.add_rule(self.switch[12], self.switch[4], FSM.all[1], self.agent.light_one_led)
        self.add_rule(self.switch[12], self.switch[4], FSM.all, self.agent.reset_all_variables)

    def add_rule(self, state1, state2, condition, action):
        """Appends rule to the end of the FSM's rule list.
        state1 is the state the FSM needs to be in for the rule to verify,
        state2 is the new state of the FSM,
        condition is the condition that needs to be met for the rule to fire,
        action is the action to be carried out """
        rule = Rule(state1, state2, condition, action)
        self.rules.append(rule)

    def get_next_signal(self):
        """query the agent for the next signal"""
        self.signal = self.agent.get_next_signal()
        return self.signal

    def run_rules(self, signal):
        """go through the rule set, in order, applying each rule until one of the rules is fired"""
        for rule in self.rules:
            if self.apply_rule(signal, rule):
                self.fire_rule(rule)
                break

    def apply_rule(self, signal, rule):
        """checks whether the conditions of a rule are met"""
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
         Constructor for the rule class
        :param state1: The state the FSM needs to be in for the rule to be fired
        :param state2: The state the FSM should go to after the rule is fired
        :param condition: Input from keypad that fires the rule if the conditions are met
        :param action: The action that is initialized of the conditions are met
        """
        self.state1 = state1
        self.state2 = state2
        self.condition = condition
        self.action = action

    def check_rule(self, state, signal):
        """
        Method that confirms if a rule should be fired or not
        :param state: str?
        :param signal: str
        :return: boolean
        """
        # pdb.set_trace()
        return (self.state1 == state) and (signal in self.condition)
