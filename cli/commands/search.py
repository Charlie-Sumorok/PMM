#! /usr/bin/env python

"search for available packages"

import os
import json
import requests

BREW_API_BASE = "https://formulae.brew.sh/api"

data_urls = {
    "brew": {
        "macOS": {
            "formula": BREW_API_BASE + "/formula/{name}.json",
            "cask": BREW_API_BASE + "/cask/{name}.json",
            "analytics": {
                "one-category": BREW_API_BASE + "/analytics/{category}/{days}.json",
                "all": {
                    "all": BREW_API_BASE + "/analytics/{category}/{repo}/{days}.json",
                    "core": BREW_API_BASE
                    + "/analytics/{category}/homebrew-core/{days}.json",
                    "cask": BREW_API_BASE
                    + "/analytics/{category}/homebrew-cask/{days}.json",
                },
            },
        },
        "Linux": {
            "formula": BREW_API_BASE + "/formula-linux/{name}.json",
            "cask": BREW_API_BASE + "/cask/{name}.json",
            "analytics": {
                "one-category": BREW_API_BASE
                + "/analytics-linux/{category}/{days}.json",
                "all": {
                    "all": BREW_API_BASE + "/analytics/{category}/{repo}/{days}.json",
                    "core": BREW_API_BASE
                    + "/analytics/{category}/linuxbrew-core/{days}.json",
                    "cask": BREW_API_BASE
                    + "/analytics/{category}/homebrew-cask/{days}.json",
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
