install python
#!/bin/bash

# Update package lists
sudo apt update

# Install Python (version 3.x)
sudo apt install python3

# Install pip (Python package manager)
sudo apt install python3-pip

# Install TQDM using pip
pip install tqdm

# Install tkinter for Python
sudo apt install python3-tk

# Install pillow
pip install pillow

echo "Python and TQDM installation completed successfully."
