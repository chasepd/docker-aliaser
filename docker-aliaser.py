#!/usr/bin/env python3

import argparse
from os.path import expanduser
import os
import subprocess


def write_alias(alias_name, image_name, keep):
    bash_profile = open(expanduser("~") + "/.bash_profile", "a")

    alias_statement = "alias " + alias_name + "='docker run -it"

    if not keep:
        alias_statement = alias_statement + " --rm "

    alias_statement = alias_statement + " -v \"$(PWD):/shared\" -w \"/shared\" " + image_name + "'\n"

    bash_profile.write(alias_statement)

    cmd = "source " + expanduser("~") + "/.bash_profile"

    print ("Alias created. Please run \"" + cmd + "\" to update your current terminal with your new alias.")


def alias_exists(alias_name):
    profile_text = ""
    with open(expanduser("~") + "/.bash_profile", "r") as bash_profile:
        for line in bash_profile:
            profile_text = profile_text + line

    text_to_check = "alias " + alias_name + "="

    if text_to_check in profile_text:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("alias_name", help="Name of created alias",
                        type=str)
    parser.add_argument("image_name", help="Name of docker image",
                        type=str)
    parser.add_argument("--keep", help="Keep image after running",
                        action="store_true")

    args = parser.parse_args()

    if alias_exists(args.alias_name):
        print ("Alias already exists. Please choose another alias name.")
    else:
        write_alias(args.alias_name, args.image_name, args.keep)
