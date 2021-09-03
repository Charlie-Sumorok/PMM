#! /usr/bin/env python

"get shell completion"
import sys
import os


def get_completion(shell):
    "get shell completion"
    completion = " ".join(
        [
            "cmds",
            "commands",
            "completion",
            "config",
            "dev",
            "develop",
            "disable",
            "docs",
            "enable",
            "h",
            "help",
            "home",
            "i",
            "install",
            "info",
            "init",
            "list",
            "login",
            "logout",
            "ls",
            "repo",
            "search",
            "show",
            "un",
            "uninstall",
            "update",
            "upgrade",
            "view",
        ]
    )
    if shell == "bash":
        return f'complete -F "{completion}" pmm'
    if shell == "zsh":
        return f'compctl -K "{completion}" pmm'

    sys.exit("Shell completion Unavailable")


def parse_args(args):
    "parse arguments"
    if len(args) == 0:
        shell_path = os.getenv("SHELL")
    elif (args[0] in ["--shell", "-s"]) and (len(args) > 1):
        shell_path = args[1]
    else:
        sys.exit()

    if shell_path:
        shell = shell_path.split("/")[-1]
        completion = get_completion(shell)
        print(completion)
