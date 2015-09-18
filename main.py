# -*- coding: utf-8
"""
Simple example of a layout with a horizontal split.
"""
from __future__ import unicode_literals

import click

from prompt_toolkit import AbortAction
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.completion import Completion, Completer
from prompt_toolkit.filters import Always
from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.layout import Window, VSplit, HSplit, Float, FloatContainer
from prompt_toolkit.layout.controls import TokenListControl, FillControl, BufferControl
from prompt_toolkit.layout.dimension import LayoutDimension
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.layout.prompt import DefaultPrompt
from prompt_toolkit.layout.toolbars import SystemToolbar, ArgToolbar, CompletionsToolbar, SearchToolbar
from prompt_toolkit.shortcuts import create_eventloop
from prompt_toolkit.styles import default_style_extensions

from pygments.style import Style
from pygments.styles.default import DefaultStyle
from pygments.token import Token


class TestCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor()

        for i in range(0, 20):
            yield Completion('Completion %i' % i, -len(word_before_cursor))


class TestStyle(Style):
    styles = {
        Token.Line: '#FFFFFF bg:#0000FF',
        Token.Info: '#CCCCCC bg:#FFFF00',

        Token.LineNumber:  'bg:#ffffaa #000000',
        Token.Menu.Completions.Completion.Current: 'bg:#00aaaa #000000',
        Token.Menu.Completions.Completion:         'bg:#008888 #ffffff',
        Token.Menu.Completions.ProgressButton:     'bg:#003333',
        Token.Menu.Completions.ProgressBar:        'bg:#00aaaa',

        Token.Toolbar.Completions:  'bg:#888800 #000000',
        Token.Toolbar.Completions.Arrow: 'bg:#888800 #000000',
        Token.Toolbar.Completions.Completion:  'bg:#aaaa00 #000000',
        Token.Toolbar.Completions.Completion.Current:  'bg:#ffffaa #000000 bold',

        Token.Prompt: 'bg:#00ffff #000000',
        Token.AfterInput: 'bg:#ff44ff #000000',

    }
    styles.update(DefaultStyle.styles)
    styles.update(default_style_extensions)


def main():
    manager = KeyBindingManager(enable_system_bindings=Always())

    D = LayoutDimension

    containers = ['AAABBBCCC']

    container_list = TokenListControl.static([(Token.Line, c) for c in containers])
    container_info = TokenListControl.static([(Token.Info, 'BOO FOO')])

    lp = Window(content=container_list, width=D(min=20, max=40, preferred=40))
    rp = Window(content=container_info, width=D(min=20, max=40, preferred=40))

    vdv = Window(content=FillControl('|', token=Token.Line), width=D.exact(1))
    hdv = Window(content=FillControl('-', token=Token.Line), height=D.exact(1))

    cmdline = Window(content=BufferControl(
        input_processors=[
            DefaultPrompt.from_message('$> ')
        ]
    ))

    panels = VSplit([lp, vdv, rp])
    content = HSplit([
        hdv,
        panels,
        hdv,
        cmdline,
        CompletionsToolbar(),
        SystemToolbar()
    ])

    layout = FloatContainer(
        content=content,
        floats=[
            Float(xcursor=True,
                  ycursor=True,
                  content=VSplit([
                      Window(width=D.exact(5),
                             content=FillControl('f', token=Token.F)),
                      CompletionsMenu(),
                  ])
            ),
        ]
    )

    eventloop = create_eventloop()
    application = Application(
        layout=layout,
        style=TestStyle,
        key_bindings_registry=manager.registry,
        buffer=Buffer(is_multiline=Always(), completer=TestCompleter()),
        on_exit=AbortAction.RAISE_EXCEPTION)

    cli = CommandLineInterface(application=application, eventloop=eventloop)
    try:
        cli.run()
    except EOFError:
        # exit out of the CLI
        pass

    eventloop.close()
    click.clear()
    print('Goodbye!')


if __name__ == '__main__':
    main()
