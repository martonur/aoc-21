from enum import Enum


class SubmarineCommand(Enum):
    FORWARD = 1
    UP = 2
    DOWN = 3

    def from_string(cmd_name: str):
        if cmd_name == "forward":
            return SubmarineCommand.FORWARD
        elif cmd_name == "up":
            return SubmarineCommand.UP
        elif cmd_name == "down":
            return SubmarineCommand.DOWN

class SubmarinePosition:
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal_position = 0
    
    def update(self, cmd: SubmarineCommand, value: int):
        if cmd == SubmarineCommand.DOWN:
            self.depth += value
        elif cmd == SubmarineCommand.UP:
            self.depth -= value
        elif cmd == SubmarineCommand.FORWARD:
            self.horizontal_position += value
    
    def calculate_result(self):
        return self.depth * self.horizontal_position
        

def main():
    current_position = SubmarinePosition()
    
    with open("day_2/input.txt") as input_file:
        for line in input_file:
            cmd, val = line.split()
            current_position.update(SubmarineCommand.from_string(cmd), int(val))
    
    print(current_position.calculate_result())


if __name__ == "__main__":
    main()
