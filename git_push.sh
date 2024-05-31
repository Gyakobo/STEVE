#!/bin/bash

# Prompt the user for input
echo "Enter a commit comment:"
read user_command

# Check if the input is empty
if [ -z "$user_command" ]; then
    echo "Error: No comment entered."
    exit 1
fi

# Run the command provided by the user
eval "sudo git add ."
eval "sudo git commit -m \"$user_command\""
eval "sudo git push -u origin main"
