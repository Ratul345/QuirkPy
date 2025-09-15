#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QuirkPy - A Community-Driven Python Experiment 🌀

This is your canvas for chaos! Add anything you want:
- New greeting styles
- Random features
- Silly functions
- Useful tools
- Complete nonsense

The only rule: Make it fun! 🎉
"""

import random
import time


def hello_ascii_art():
    """Print Hello World in glorious ASCII art"""
    ascii_styles = [
        """
    ██╗  ██╗ ██████╗ ███╗   ███╗     ██████╗ ██████╗ ███╗   ███╗
    ██║  ██║██╔═══██╗████╗ ████║    ██╔════╝██╔═══██╗████╗ ████║
    ███████║██║   ██║██╔████╔██║    ██║     ██║   ██║██╔████╔██║
    ██╔══██║██║   ██║██║╚██╔╝██║    ██║     ██║   ██║██║╚██╔╝██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
        """,
        """
  _   _      _ _         _        _____ _           
 | | | |    | | |       | |      / ____| |          
 | |_| | ___| | | ___   | |     | |  __| | _____  __
 |  _  |/ _ \ | |/ _ \  | |     | | |_ | |/ _ \ \/ /
 | | | |  __/ | | (_) | | |____ | |__| | |  __/>  < 
 |_| |_|\___|_|_|\___/  |______|\_____|_|\___/_/\_\\
        """,
        """
    ╔╗ ╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔
    ╠╩╗╠╣ ║║║║╣  ║ ║ ║║║║
    ╚═╝╚  ╝╚╝╚═╝ ╩ ╚═╝╝╚╝
    ╔═╗ ╦ ╦╔═╗╔╗╔╔╦╗╔═╗╦═╗
    ║═╬╗║ ║╠╣ ║║║ ║║╠╣ ╠╦╝
    ╚═╝╚╚═╝╚  ╝╚╝═╩╝╚═╝╩╚═
        """
    ]
    return random.choice(ascii_styles)


def hello_reversed_text():
    """Print Hello World backwards because normal is boring"""
    reversed_styles = [
        "dlroW ,olleH 🙃",
        "¿dlroW olleH",
        "H€llø Wørld"[::-1],  # Actually reversed
        "Hello World"[::-1].upper(),
        "dlrow ,olleh" * 2
    ]
    return random.choice(reversed_styles)


def hello_emoji_party():
    """Hello World but make it an emoji celebration"""
    emoji_combos = [
        "👋🌍✨ Hello World! ✨🌍👋",
        "🤗🌎🎉 HELLO WORLD! 🎉🌎🤗",
        "🚀🌌 Hello from space world! 👽🪐",
        "🌈🎊 Hellooo beautiful world! 🎊🌈",
        "👑🗺️ Hello World, you're royalty! 👑🗺️",
        "🦄🌟 Magical Hello World! 🌟🦄"
    ]
    return random.choice(emoji_combos)


def hello_chaotic():
    """The main chaos orchestrator - picks a random greeting style"""
    greeting_functions = [
        hello_ascii_art,
        hello_reversed_text,
        hello_emoji_party
    ]
    
    # Add some dramatic pause for effect
    time.sleep(random.uniform(0.1, 0.3))
    
    chosen_greeting = random.choice(greeting_functions)()
    return chosen_greeting


def contribution_welcome():
    """Print a welcome message for potential contributors"""
    welcome_messages = [
        "🎨 Welcome to QuirkPy Your creativity is welcome here!",
        "🚀 Ready to add some chaos? Fork and contribute anything!",
        "🌟 This project grows through community magic - add your touch!",
        "🤝 All contributions welcome: features, fixes, jokes, or nonsense!",
        "🎉 The chaos continues with YOU! What will you add?"
    ]
    return random.choice(welcome_messages)


def main():
    """Main function that runs the show"""
    print("=" * 60)
    print(hello_chaotic())
    print("\n" + contribution_welcome())
    print("=" * 60)
    
    # Fun easter egg for contributors
    if random.random() < 0.15:  # 15% chance
        print("\n🥚 EASTER EGG! Add your own chaos below this line! 🥚")


# AI/ML EVOLUTION ZONE 🧠
#
# QuirkPy is evolving! Check out our new ML modules:
# from ml_modules.chaos_engine import BanglaChaosGenerator
#
# ✅ NEXT LEVEL CONTRIBUTIONS:
# - Add Bangla text datasets to chaos_engine.py
# - Create new ML modules in ml_modules/
# - Build chaos-based data augmentation tools
# - Train Bangla meme generation models
#
# Start with: python -c "from ml_modules.chaos_engine import test_bangla_chaos; test_bangla_chaos()"


if __name__ == "__main__":
    main()