import sys, functools
from typing import Optional, Dict, Callable, MutableMapping, Iterable, List, Tuple, Any

bases: List[str] = ["A","C","G","T"]
build: MutableMapping[str, str] = {}

class Handler:
    def __init__(self, info: str, func: Callable[[], str]) -> None:
        self.info = info
        self.func = func

    @classmethod
    def baseExchange(cls, base: str, info: str, func: Callable[[], str]) -> int:
        ''' compiles complement base exchange options '''
        build[base] = Handler(info, func)
        return 0

    @staticmethod
    def complement_transform(base: str) -> str:
        ''' look up dictionary build options, returns complement base relevant to input base '''
        return build[base].func()

def validate(val: Any) -> Any:
    ''' validates input string only contains true DNA bases '''
    @functools.wraps(val)
    def val_inner(*args: Tuple[str]) -> int:
        for base in args[0].upper():
            if base not in bases:
                print(f'Error. Incorrect base: {base}', file=sys.stderr)
                return 1
        return val(*args)
    return val_inner

Handler.baseExchange("A", "Adenine to Thymine", lambda: "T")
Handler.baseExchange("C", "Cytosine to Guanine", lambda: "G")
Handler.baseExchange("G", "Guanine to Cytosine", lambda: "C")
Handler.baseExchange("T", "Thymine to Adenine", lambda: "A")

@validate
def run(strand: Iterable[str]) -> int:
    '''
    Generates DNA complement strand through pattern matching and strand array reversal.
    '''
    print(''.join([Handler.complement_transform(c) for c in strand.upper()][::-1]))
    return 0

if __name__ == '__main__':
    strand = 'ACGTTgca'

    exit(run(strand))
