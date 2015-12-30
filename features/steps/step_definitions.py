# -*- coding: utf-8
from __future__ import unicode_literals
import re
import pexpect
import platform
from behave import given, when, then
if platform.system() != 'Windows':
    from pexpect import spawnu as pxspawn
    from pexpect import EOF
else:
    from winpexpect import winspawn as pxspawn
    from winpexpect import EOF


@given('the module "{modulename}" is installed')
def step_module_import(context, modulename):
    """
    Tries to import a module with a given name to make sure it is installed.
    """
    module = __import__(modulename)


@when('we run cli')
def step_run_cli(context):
    """
    Run the process using pexpect.
    """
    context.cli = pxspawn('pptk')
    context.exit_sent = False


@when('we wait for prompt')
def step_wait_prompt(context):
    """
    Make sure prompt is displayed.
    """
    _expect_exact(context, 'pptk> ', timeout=5)


@when('we type in "{txt}"')
def step_send_text(context, txt):
    """
    Send line.
    """
    context.cli.sendline(txt)


@when('we send "ctrl + d"')
def step_ctrl_d(context):
    """
    Send Ctrl + D to hopefully exit.
    """
    context.cli.sendcontrol('d')
    context.exit_sent = True


@then('we see "{txt}"')
def step_see_text(context, txt):
    """
    See line displayed.
    """
    _expect_exact(context, txt, timeout=2)


@then('cli exits')
def step_wait_exit(context):
    """
    Make sure the cli exits.
    """
    _expect_exact(context, EOF, timeout=5)


def _expect_exact(context, expected, timeout):
    try:
        context.cli.expect_exact(expected, timeout=timeout)
    except:
        # Strip color codes out of the output.
        print('boo', context.cli.before)
        actual = re.sub(r'\x1b\[([0-9A-Za-z;?])+[m|K]?', '', context.cli.before)
        raise Exception('Expected:\n---\n{0}\n---\n\nActual:\n---\n{1}\n---'.format(
            expected,
            actual))
