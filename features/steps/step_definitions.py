# -*- coding: utf-8
from __future__ import unicode_literals
import subprocess
import win32con
from behave import given, when, then
from threading import Timer


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
    si = subprocess.STARTUPINFO()
    si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = win32con.SW_MAXIMIZE
    context.cli = subprocess.Popen('pptk', stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
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
    context.cli.stdin.write(txt + "\n")


@when('we send "ctrl + d"')
def step_ctrl_d(context):
    """
    Send Ctrl + D to hopefully exit.
    """
    context.cli.terminate()
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
    context.cli.poll()


def _kill(child):
    child.kill()


def _expect_exact(context, expected, timeout):
    timer = Timer(timeout, _kill, [context.cli])
    try:
        timer.start()
        current_out = [l.rstrip() for l in context.cli.stdout.readlines()]
        current_err = [l.rstrip() for l in context.cli.stderr.readlines()]
    finally:
        timer.cancel()

    actual = current_out if current_out else current_err
    actual_text = '\n'.join(actual)

    print('Actual:\n{0}'.format(actual_text))

    if expected not in actual:
        raise Exception('Expected:\n---\n{0}\n---\n\nActual:\n---\n{1}\n---'.format(
            expected,
            actual_text))
