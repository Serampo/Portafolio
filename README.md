# 📝 Task Tracker CLI

A simple, lightweight Command Line Interface (CLI) designed to track and manage your daily tasks. This project was built using native Python to practice file system management and JSON data persistence without relying on external libraries.

# ✨ Features
Add, Update, and Delete tasks.

Track Status: Mark tasks as todo, in-progress, or done.

Smart Listing: Filter tasks by their current status.

Persistent Storage: All data is saved in a local tasks.json file.

Automatic Timestamps: Tracks when tasks are created and last updated.

# 🚀 Getting Started

Prerequisites
Python 3.x installed on your machine.

No external packages required (json, os, and sys are native).

Installation
Switch to this branch:

Bash

git checkout task-tracker
Run the application directly using the Python interpreter.

# 🛠️ Technical Implementation
Language: Python

Storage: Native json module.

CLI Logic: Argument parsing via sys.argv.

Error Handling: Graceful management of missing files and invalid IDs.
