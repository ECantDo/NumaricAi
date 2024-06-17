import numpy as np
from ai import CantDoAi


class MicroGameWrapper:
    def __init__(self, env_name="MicroGame-v0"):
        self.ai = CantDoAi()
        self.env_name = env_name
        self.ai.update_update_order()
        pass


if __name__ == "__main__":
    pass
