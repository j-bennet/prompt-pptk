# -*- coding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory


def main():
    history = InMemoryHistory()

    try:
        while True:
            try:
                text = prompt("pptk> ", history=history)
                print('You entered: {0}'.format(text))
            except KeyboardInterrupt:
                pass

    except EOFError:
        # user exited
        pass

    print('Goodbye!')

if __name__ == '__main__':
    main()
