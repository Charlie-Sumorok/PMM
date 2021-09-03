#! /usr/bin/env python

"Go to the homepage of PMM or a specified package manager"

from webbrowser import open_new_tab as open_url

import requests


def parse_args(args):
    "parse arguments"
    if len(args) == 0:
        url = "https://github.com/Charlie-Sumorok/PMM"
    else:
        package_manager_name = args[0]
        raw_repo_url = "https://raw.githubusercontent.com/Charlie-Sumorok/PMM"
        branch = "main"
        path = "package-managers/data.json"
        data_url = f"{raw_repo_url}/{branch}/{path}"
        package_manager_data = requests.get(data_url).json()
        package_manager = package_manager_data[package_manager_name]
        urls = package_manager["urls"]
        url = urls["standard"]
    open_url(url)
