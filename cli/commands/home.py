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
        data_url = "https://raw.githubusercontent.com/Charlie-Sumorok/PMM/main/package-managers/data.json"
        package_manager_data = requests.get(data_url).json()
        package_manager = package_manager_data[package_manager_name]
        urls = package_manager["urls"]
        url = urls["standard"]
    open_url(url)
