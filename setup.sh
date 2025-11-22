#!/bin/bash
# Setup script for Quantum VES simulation

echo "=========================================="
echo "Quantum VES Setup"
echo "=========================================="
echo

# Check Python version
echo "Checking Python version..."
python3 --version

# Create virtual environment
echo
echo "Creating virtual environment..."
python3 -m venv qves_env

# Activate virtual environment
echo "Activating virtual environment..."
source qves_env/bin/activate

# Upgrade pip
echo
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo
echo "Installing required packages..."
pip install -r requirements.txt

echo
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo
echo "To activate the environment, run:"
echo "  source qves_env/bin/activate"
echo
echo "Then run simulations with:"
echo "  python3 rbe_quantum_ves.py"
echo


