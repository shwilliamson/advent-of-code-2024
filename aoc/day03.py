
DIGITS = ['0','1','2','3','4','5','6','7','8','9']

class Symbol:
    START = "START"
    END = "END"
    M = 'm'
    U = 'u'
    L = 'l'
    D = 'd'
    O = 'o'
    N = 'n'
    T = 't'
    APOSTROPHE = '\''
    OPEN_PARENTHESIS = '('
    CLOSED_PARENTHESIS = ')'
    COMMA = ','
    OPERAND1 = "OPERAND1"
    OPERAND2 = "OPERAND2"


class StateMachine:

    def __init__(self):
        self.state = Symbol.START
        self.enabled = True
        self.enabling = False
        self.disabling = False
        self.operand1 = ""
        self.operand2 = ""

    PREFIX_EDGES = [
        (Symbol.END, Symbol.M),
        (Symbol.START, Symbol.M),
        (Symbol.M, Symbol.U),
        (Symbol.U, Symbol.L),
        (Symbol.L, Symbol.OPEN_PARENTHESIS),
    ]

    ENABLE_EDGES = [
        (Symbol.END, Symbol.D),
        (Symbol.START, Symbol.D),
        (Symbol.D, Symbol.O),
        (Symbol.O, Symbol.OPEN_PARENTHESIS),
    ]

    DISABLE_EDGES = [
        (Symbol.END, Symbol.D),
        (Symbol.START, Symbol.D),
        (Symbol.D, Symbol.O),
        (Symbol.O, Symbol.N),
        (Symbol.N, Symbol.APOSTROPHE),
        (Symbol.APOSTROPHE, Symbol.T),
        (Symbol.T, Symbol.OPEN_PARENTHESIS),
    ]

    def read(self, char: str) -> str:
        print(f"{self.state} -> {char}")
        # big ole switch statement, fun with compilers
        match (self.state, char):
            # parse mul(123,456)
            case n if n in self.PREFIX_EDGES:
                self.state = char
            case n if n[0] == Symbol.OPEN_PARENTHESIS and n[1] in DIGITS:
                self.state = Symbol.OPERAND1
                self.operand1 = char
            case n if n[0] == Symbol.OPERAND1 and n[1] in DIGITS and len(self.operand1) < 3:
                self.operand1 += char
            case n if n == (Symbol.OPERAND1, Symbol.COMMA) and len(self.operand1) > 0:
                self.state = char
            case n if n[0] == Symbol.COMMA and n[1] in DIGITS:
                self.state = Symbol.OPERAND2
                self.operand2 = char
            case n if n[0] == Symbol.OPERAND2 and n[1] in DIGITS and len(self.operand2) < 3:
                self.operand2 += char
            case n if n == (Symbol.OPERAND2, Symbol.CLOSED_PARENTHESIS) and len(self.operand2) > 0:
                self.state = Symbol.END

            # parse do() and don't()
            case n if n in self.ENABLE_EDGES:
                self.enabling = True
                self.disabling = False
                self.state = char
            case n if n in self.DISABLE_EDGES:
                self.enabling = False
                self.disabling = True
                self.state = char
            case (Symbol.OPEN_PARENTHESIS, Symbol.CLOSED_PARENTHESIS):
                if self.enabling:
                    self.enabled = True
                    print(f"State machine enabled.")
                elif self.disabling:
                    self.enabled = False
                    print(f"State machine disabled.")
                self.reset()

            # illegal state (gibberish)
            case _:
                print(f"illegal edge: {self.state} -> {char}")
                self.reset()

        return self.state


    def reset(self):
        self.state = Symbol.START
        self.operand1 = ""
        self.operand2 = ""
        self.enabling = False
        self.disabling = False


    def compute(self) -> int:
        if not self.enabled:
            return 0
        return int(self.operand1) * int(self.operand2)


def main():
    answer = 0
    parser = StateMachine()
    with open('resources/day03.txt', 'r') as file:
        for line in file:
            for char in line:
                if parser.read(char) == Symbol.END:
                    answer += parser.compute()

    print(f"The answer is {answer}")


if __name__ == '__main__':
    main()