#!/bin/bash

# Astro AI Demo Launcher
# Double-click this file to launch the Astro AI demo

echo "🚀 Launching Astro AI Demo..."
echo "================================================"
echo "Astro AI - Private AI Chat Application"
echo "This is a demonstration of the rebranded interface"
echo "================================================"
echo ""

# Change to the directory containing this script
cd "$(dirname "$0")"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 to run Astro AI Demo"
    read -p "Press Enter to exit..."
    exit 1
fi

# Run the Astro AI demo
echo "Starting Astro AI Demo..."
python3 astro_ai_demo.py

echo ""
echo "Astro AI Demo has closed."
echo "Thank you for trying Astro AI!"
read -p "Press Enter to exit..."
