from datetime import datetime
from typing import Callable
from functools import partial

GreetingReader = Callable[[],str]
GreetingFunction = Callable[[str], str]

def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name == 'Kostya':
        return f'{greeting_reader()}, sir'
    return f'{greeting_reader()}, {name}'

def greet_list(names: list[str], greeting_fn: GreetingFunction) -> list[str]:
    return [greeting_fn(name) for name in names]

def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return 'Good morning'
    elif 12 <= current_time.hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'
    
def read_name() -> str:
    return input('Enter your name: ')

def main():
    greet_fn = partial(greet, greeting_reader = read_greeting)
    print(greet_fn(read_name()))
    print(greet_list(['John','jane','Joe'], greet_fn))

if __name__ == '__main__':
    main()