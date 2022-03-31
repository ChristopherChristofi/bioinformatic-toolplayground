import sys, functools, argparse
from typing import Optional, Callable, MutableMapping, Iterable, List, Tuple, Any, Sequence

bases: List[str] = ["A","C","G","T"]
build: MutableMapping[str, str] = {}

class Handler:
    def __init__(self, info: str, func: Callable[[], str]) -> None:
        self.info = info
        self.func = func

    @classmethod
    def base_exchange(cls, base: str, info: str, func: Callable[[], str]) -> int:
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
        input_strand = set(args[0])
        for base in input_strand:
            if base not in bases:
                print(f'Error. Incorrect base: {base}', file=sys.stderr)
                return 1
        return val(*args)
    return val_inner

Handler.base_exchange("A", "Adenine to Thymine", lambda: "T")
Handler.base_exchange("C", "Cytosine to Guanine", lambda: "G")
Handler.base_exchange("G", "Guanine to Cytosine", lambda: "C")
Handler.base_exchange("T", "Thymine to Adenine", lambda: "A")

@validate
def generate_complement(strand: Iterable[str]) -> str:
    '''
    Generates DNA complement strand through pattern matching and strand array reversal.
    '''
    complement = ''.join([Handler.complement_transform(c) for c in strand][::-1])
    return complement

def run(strand: Optional[Sequence[str]] = None) -> int:
    '''
    main init function function processing standard input stream
    '''
    if sys.stdin.isatty():
        print(f'Error.', file=sys.stderr)
        return 1
    strand = sys.stdin.read()

    print(generate_complement(strand.rstrip().upper()))
    return 0

if __name__ == '__main__':
    exit(run())
