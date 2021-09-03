#! /usr/bin/env python

"list all commands"

import sys
import colorama

colorama.init(autoreset=True)


def snippet(
    string,
    style=colorama.Style.RESET_ALL,
    foreground=colorama.Fore.RESET,
    background=colorama.Back.RESET,
):
    "get snippet coloring"
    return (
        colorama.Back.LIGHTBLACK_EX
        + colorama.Style.BRIGHT
        + string
        + style
        + background
        + foreground
    )


commands_info = {
    "alias": f"""create command aliases (same syntax as {
		snippet('alias', foreground=colorama.Fore.CYAN)
	})""",  # `alias key=value`
    "update": "update all package managers",
    "upgrade": "update specific package managers",
    "home": "Go to the homepage of PMM or a specified package manager",
    "info": "Get info about PMM or a specified package manager",
    "init": "Initialize a pull request to add a new package managers",
    "list": "list package managers",
    "ls": "alias of list",
    "dev": "alias of develop",
    "edit": f"edit pull request made with {snippet('pmm init')}",
    "install": "install a package manager",
    "i": "alias of install",
    "uninstall": "uninstall a package manager",
    "un": "alias of uninstall",
    "status": "check status of pull requests",
    "docs": "Go to docs for PMM or a specified package manager",
    "login": "log in to GitHub to create the pull request",
    "logout": "log out of GitHub",
    "search": "search for available packages",
    # --manager <Package Manager> | -m <Package Manager> | <Package Name>
    "enable": "enable a package manager for searching",
    "disable": "disable a package manager for searching",
    "repo": "Go to the repo of PMM or a specified package manager or package",
    "config": "view or modifiy settings",
    "commands": "list all commands",
    "completion": "get shell completion",
    "cmds": "alias of commands",
    # "show": "show package manager on PMM website",
    # "": "Package Manager Manager",
}


def parse_args(args: list[str]):
    "parse arguments"
    verbose_flags = ["-v", "--verbose"]
    no_verbose_flags = ["-nv", "--no-verbose"]
    verbose_flag_indexes = [
        index for index, arg in enumerate(args) if arg in verbose_flags
    ]
    no_verbose_flag_indexes = [
        index for index, arg in enumerate(args) if arg in no_verbose_flags
    ]
    max_verbose_flags = (
        max(verbose_flag_indexes) if len(verbose_flag_indexes) != 0 else -1
    )
    max_no_verbose_flags = (
        max(no_verbose_flag_indexes) if len(no_verbose_flag_indexes) != 0 else -1
    )
    if len(args) != len(
        [arg for arg in args if arg in [*verbose_flags, *no_verbose_flags]]
    ):
        sys.exit(
            f"""{
			colorama.Fore.RED
		}The specified flags, {
			colorama.Back.LIGHTBLUE_EX
		}{
			colorama.Style.BRIGHT
		}{
			", ".join([
				arg for arg in args
				if arg not in [*verbose_flags, *no_verbose_flags]
			])
		}{
			colorama.Style.RESET_ALL
		}{
			colorama.Back.RESET
		},{
			colorama.Fore.RED
		} are not allowed!{
			colorama.Fore.RESET
		}"""
        )
    elif (len(args) > 0) and max_verbose_flags > max_no_verbose_flags:
        print(" ".join(commands_info.keys()))
    elif (len(args) == 0) or max_verbose_flags < max_no_verbose_flags:
        print(
            "\n".join(
                [
                    f"""{
				colorama.Style.BRIGHT
			}{
				command_name
			}{
				colorama.Style.RESET_ALL
			}: {
				colorama.Fore.CYAN
			}{
					command_info
			}{
				colorama.Fore.RESET
			}"""
                    for command_name, command_info in commands_info.items()
                ]
            )
        )
