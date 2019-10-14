from Keypad.FSM import *
from Keypad.KPC_agent import KPC

AGENT = KPC()
FSM = FSM(AGENT)

while FSM.run:
    print(FSM.current_state)
    print(AGENT.cump)
    FSM.get_next_signal()
    FSM.run_rules()
