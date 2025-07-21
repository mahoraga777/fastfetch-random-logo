import random
import subprocess
from pathlib import Path

# Paths
config_path = Path.home() / ".config/fastfetch/config.jsonc"
logo_dir = Path.home() / ".config/fastfetch/logo"

# Pick a random logo (01–09)
num = f"{random.randint(1, 9):02d}"
logo_path = str(logo_dir / num)

# Replace the source line directly
with open(config_path, "r") as f:
    lines = f.readlines()

with open(config_path, "w") as f:
    for line in lines:
        if "\"source\"" in line:
            indent = " " * (len(line) - len(line.lstrip()))
            f.write(f'{indent}"source": "{logo_path}",\n')
        else:
            f.write(line)

# Run Fastfetch
subprocess.run(["fastfetch"])

