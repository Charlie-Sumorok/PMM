#! /usr/bin/env python

'get help for a command'

import re

from .commands import  commands_info


def parse_args(args):
	'parse arguments'
	if re.search('^([a-zA-Z]+)?$', args[0]):
		print(commands_info[args[0]])

#print(cli_docs)
options = {
	"update": "",
	"upgrade": "{package_manager_name}",
	"home": "{package_manager_name}",
	"info": "{package_manager_name}",
	"init": "",
	"h": "-> help",
	"list": "",
	"ls": "-> list",
	"install": {
		"[{package_manager_name}...]",
		"{package_manager_name}@<package_manager_version>",
		"{git_remote}",
		"{github_username}/{github_project}",
		"--package_managers-file my-package_managers.txt",
		"--file my-package_managers.txt",
		"-f my-package_managers.txt",
	},
	"i": "-> install",
	"uninstall": "[{package_manager_name}...]",
	"un": "-> uninstall",
	"docs": "{package_manager_name}",
	"help": "{command}",
	"login": "?",
	"logout": "",  # undo login
	"view": "{package_manager_name}",
	"search": {
		"{package_manager_name}",
		"{search_term}"  # searches all package managers
	},
	"show": "",  # show on website
	"enable": "{package_manager_name}",  # enable package manager
	"disable": "{package_manager_name}",  # disable package manager
	"repo": "{package_manager_name}",  # show package manager repo
	"config": "",  # show or edit settings
	"commands": "",  # list commands
	"completion": "--shell <SHELL>", # (prints | writes) completion script
	"cmds": "-> commands",
}
