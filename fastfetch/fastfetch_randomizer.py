#!/usr/bin/env python3

import json
import random
import os
from pathlib import Path

def update_fastfetch_logo():
    """Update fastfetch config with a random logo from 01-10"""
    
    # Path to your fastfetch config file
    config_path = Path.home() / ".config" / "fastfetch" / "config.jsonc"
    
    # Backup path (optional)
    backup_path = config_path.with_suffix('.jsonc.backup')
    
    # Get available logos only
    logo_dir = Path("/home/pirateking/.config/fastfetch/logo/")
    available_logos = []
    
    for i in range(1, 11):
        logo_file = logo_dir / f"{i:02d}"
        if logo_file.exists() and logo_file.is_file():
            available_logos.append(i)
    
    if not available_logos:
        print("No valid logo files found!")
        return False
    
    # Pick from available logos only
    logo_num_int = random.choice(available_logos)
    logo_num = f"{logo_num_int:02d}"
    logo_path = f"/home/pirateking/.config/fastfetch/logo/{logo_num}"
    
    # Set appropriate height based on logo
    if logo_num_int == 7:
        logo_height = 20  # Special height for logo 07
    else:
        logo_height = 18  # Default height for other logos
    
    # print(f"Available logos: {[f'{i:02d}' for i in available_logos]}")
    # print(f"Selected logo: {logo_num} (height: {logo_height})")
    
    try:
        # Read current config
        if not config_path.exists():
            print(f"Config file not found: {config_path}")
            return False
            
        with open(config_path, 'r') as f:
            content = f.read()
        
        # Create backup
        with open(backup_path, 'w') as f:
            f.write(content)
        
        # Parse JSON (handling JSONC comments if any)
        # For simple replacement, we'll use string manipulation
        # to preserve formatting and comments
        
        # Find and replace the logo source line
        lines = content.split('\n')
        updated_lines = []
        
        for line in lines:
            if '"source":' in line and '/home/pirateking/.config/fastfetch/logo/' in line:
                # Extract indentation
                indent = line[:len(line) - len(line.lstrip())]
                # Replace with new logo path
                updated_line = f'{indent}"source": "{logo_path}",'
                updated_lines.append(updated_line)
                # print(f"Updated logo to: {logo_num}")
            elif '"height":' in line:
                # Extract indentation
                indent = line[:len(line) - len(line.lstrip())]
                # Replace with appropriate height
                updated_line = f'{indent}"height": {logo_height},'
                updated_lines.append(updated_line)
                # print(f"Updated height to: {logo_height}")
            else:
                updated_lines.append(line)
        
        # Write updated config
        updated_content = '\n'.join(updated_lines)
        with open(config_path, 'w') as f:
            f.write(updated_content)
            
        # print("Successfully updated fastfetch config with logo {logo_num}")
        return True
        
    except Exception as e:
        print(f"Error updating config: {e}")
        # Restore backup if something went wrong
        if backup_path.exists():
            with open(backup_path, 'r') as f:
                backup_content = f.read()
            with open(config_path, 'w') as f:
                f.write(backup_content)
            print("Restored backup config")
        return False

def check_logo_files():
    """Check all logo files and report status"""
    logo_dir = Path("/home/pirateking/.config/fastfetch/logo/")
    
    # print("Checking logo files:")
    # print("-" * 20)
    
    for i in range(1, 11):
        logo_file = logo_dir / f"{i:02d}"
        status = "✓ OK"
        
        if not logo_file.exists():
            status = "✗ Missing"
        elif not logo_file.is_file():
            status = "✗ Not a file"
        elif logo_file.stat().st_size == 0:
            status = "✗ Empty file"
        
        # Only print if there's an error
        if "✗" in status:
            print(f"ERROR - Logo {i:02d}: {status} ({logo_file})")
    
    # print("-" * 20)

def main():
    """Main function"""
    # print("Fastfetch Logo Randomizer")
    # print("=" * 25)
    
    # Check if logo directory exists
    logo_dir = Path("/home/pirateking/.config/fastfetch/logo/")
    if not logo_dir.exists():
        print(f"ERROR: Logo directory not found: {logo_dir}")
        return
    
    # Check all logo files
    check_logo_files()
    
    # Update the config
    update_fastfetch_logo()

if __name__ == "__main__":
    main()