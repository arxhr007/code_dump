#!/bin/bash

r="\033[31m"
g="\033[32m"
y="\033[33m"
b="\033[36m"
p="\033[35m"
w="\033[37m"

URL="http://localhost:5000/call"

danger_message() {
    echo -e """
    ${g}[${w}flood prevention system${g}]${r}
    ▗▄▄▄   ▗▄▖ ▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖▗▄▄▖
    ▐▌  █ ▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌   ▐▌ ▐▌
    ▐▌  █ ▐▛▀▜▌▐▌ ▝▜▌▐▌▝▜▌▐▛▀▀▘▐▛▀▚▖
    ▐▙▄▄▀ ▐▌ ▐▌▐▌  ▐▌▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌
    """
}

safe_message() {
    echo -e """
    ${g}[${w}flood prevention system${g}]
     ▗▄▄▖ ▗▄▖ ▗▄▄▄▖▗▄▄▄▖
    ▐▌   ▐▌ ▐▌▐▌   ▐▌   
     ▝▀▚▖▐▛▀▜▌▐▛▀▀▘▐▛▀▀▘
    ▗▄▄▞▘▐▌ ▐▌▐▌   ▐▙▄▄▖
    """
}

handle_greater() {
    danger_message
    echo -e "${y}water level : ${p}$1"
    termux-vibrate -d 2000
    termux-torch on
    termux-torch off
}

handle_less_or_equal() {
    safe_message
    echo -e "${y}water level : ${p}$1"
}

while true; do
    response=$(curl -s $URL | jq -r '.result')

    if [[ $response =~ ^[0-9]+$ ]]; then
        if (( response > 400 )); then
            handle_greater "$response"
        else
            handle_less_or_equal "$response"
        fi
    else
        echo "Received non-numeric value: $response"
    fi

done
