#! /usr/bin/env python

"search for available packages"

import os
import json
import requests

data_urls = {
    "brew": {
        "macOS": {
            "formula": "https://formulae.brew.sh/api/formula/{name}.json",
            "cask": "https://formulae.brew.sh/api/cask/{name}.json",
            "analytics": {
                "one-category": "https://formulae.brew.sh/api/analytics/{category}/{days}.json",
                "all": {
                    "all": "https://formulae.brew.sh/api/analytics/{category}/{repo}/{days}.json",
                    "core": "https://formulae.brew.sh/api/analytics/{category}/homebrew-core/{days}.json",
                    "cask": "https://formulae.brew.sh/api/analytics/{category}/homebrew-cask/{days}.json",
                },
            },
        },
        "Linux": {
            "formula": "https://formulae.brew.sh/api/formula-linux/{name}.json",
            "cask": "https://formulae.brew.sh/api/cask/{name}.json",
            "analytics": {
                "one-category": "https://formulae.brew.sh/api/analytics-linux/{category}/{days}.json",
                "all": {
                    "all": "https://formulae.brew.sh/api/analytics/{category}/{repo}/{days}.json",
                    "core": "https://formulae.brew.sh/api/analytics/{category}/linuxbrew-core/{days}.json",
                    "cask": "https://formulae.brew.sh/api/analytics/{category}/homebrew-cask/{days}.json",
                },
            },
        },
    }
}


def search_npm(name):
    "search npm for package"
    results_info = os.popen(f"npm search --json {name}").read()
    results = [*map(lambda result: json.loads(result)["name"], results_info)]
    return results


def get_npm_info(package, registry_url="auto"):
    "get info of npm package"
    if registry_url == "auto":
        registry_url = "https://registry.npmjs.com"
    response = requests.get(f"{registry_url}/{package}")
    return response.json()
