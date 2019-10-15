from FSM import FSM
from KPC_agent import KPC
import pdb


if __name__ == "__main__":
    AGENT = KPC()
    fsm = FSM(AGENT)
    fsm.setup_rules()
    while fsm.run:
        print(fsm.state)
        #print(AGENT.passcode_buffer)
        pdb.set_trace()
        fsm.get_next_signal()
