from Keypad.FSM import *
from Keypad.KPC_agent import KPC

AGENT = KPC()
FSM = FSM(AGENT)

while FSM.run:
    print(FSM.state)
    print(AGENT.passcode_buffer)
    FSM.get_next_signal()
    FSM.setup_rules()
