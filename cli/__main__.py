#! /usr/bin/env python3

"Entry point to PMM"

import sys
import colorama
import commands

colorama.init(autoreset=True)


def parse_args(args):
    "parse arguments"
    if len(args) == 0:
        commands.pmm_help.parse_args([""])
    else:
        command, *subcommand_args = args
        if command in ["commands", "cmds"]:
            commands.commands.parse_args(subcommand_args)
        elif command == "home":
            commands.home.parse_args(subcommand_args)
        elif command in ["install", "i"]:
            commands.install.parse_args(subcommand_args)
        elif command in ["uninstall", "un"]:
            raise NotImplementedError(
                'The command, "uninstall", has not been implemented yet'
            )
        elif command in ["list", "ls"]:
            raise NotImplementedError(
                'The command, "list", has not been implemented yet'
            )
        elif command == "completion":
            commands.completion.parse_args(subcommand_args)
        else:
            raise NotImplementedError(
                f'The command, "{command}", has not been implemented yet'
            )


if __name__ == "__main__":
    parse_args(sys.argv[1:])
