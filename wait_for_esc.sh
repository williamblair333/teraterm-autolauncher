#!/bin/bash

# Change terminal settings to immediately return input
old_settings=$(stty -g)
stty -icanon -echo min 0 time 0

echo "Press Esc key to exit..."

# Loop indefinitely
while true; do
    # Read a single character
    read -s -n 1 key

    # Check if the key is the Esc character
    if [[ $key == $'\e' ]]; then
        break
    fi
done

# Restore original terminal settings
stty "$old_settings"
echo "Esc key pressed, exiting."
