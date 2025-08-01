# 🎨 Fastfetch Random Logo

> Transform your terminal into a dynamic showcase with randomly rotating logos every time you open it!

![Terminal](https://img.shields.io/badge/Terminal-Enhanced-brightgreen)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Fastfetch](https://img.shields.io/badge/Fastfetch-Compatible-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🎲 **Random Logo Selection** - Automatically picks from your logo collection
- 🔧 **Smart Height Adjustment** - Optimizes display for different image sizes  
- 🛡️ **Error Handling** - Robust file validation and backup protection
- 🚀 **Zero Configuration** - Works out of the box after setup
- 🎯 **Silent Operation** - Clean output, only shows errors when needed

## 🚀 Quick Setup

### 1. **Clone the Repository**
```bash
git clone https://github.com/mahoraga777/fastfetch-random-logo.git
cd fastfetch-random-logo
```

### 2. **Copy the Script**
```bash
# Copy the script to your fastfetch config directory
cp fastfetch_randomizer.py ~/.config/fastfetch/
```

### 3. **Make it Executable**
```bash
chmod +x ~/.config/fastfetch/fastfetch_randomizer.py
```

### 4. **Test the Script**
```bash
python3 ~/.config/fastfetch/fastfetch_randomizer.py
fastfetch
```

### 5. **Auto-Run Setup** (Choose your shell)

#### For **Zsh** users (`~/.zshrc`):
```bash
echo 'python3 ~/.config/fastfetch/fastfetch_randomizer.py' >> ~/.zshrc
echo 'fastfetch' >> ~/.zshrc
source ~/.zshrc
```

#### For **Bash** users (`~/.bashrc`):
```bash
echo 'python3 ~/.config/fastfetch/fastfetch_randomizer.py' >> ~/.bashrc
echo 'fastfetch' >> ~/.bashrc
source ~/.bashrc
```

#### For **Fish** users (`~/.config/fish/config.fish`):
```bash
echo 'python3 ~/.config/fastfetch/fastfetch_randomizer.py' >> ~/.config/fish/config.fish
echo 'fastfetch' >> ~/.config/fish/config.fish
```

#### Manual Setup:
Add these lines to your shell's config file:
```bash
python3 ~/.config/fastfetch/fastfetch_randomizer.py
fastfetch
```

## 📁 Directory Structure

Your fastfetch logo directory should look like this:
```
~/.config/fastfetch/logo/
├── 01          # Logo file 1
├── 02          # Logo file 2  
├── 03          # Logo file 3
├── ...
└── 10          # Logo file 10
```

## ⚙️ Configuration

The script automatically handles:
- **Logo Selection**: Randomly picks from available logos (01-10)
- **Height Optimization**: Adjusts display height based on image size
- **Error Recovery**: Skips corrupted/missing files
- **Backup Protection**: Creates backups before config changes

### Custom Height Settings
For logos that need specific heights, edit the script:
```python
if logo_num_int == 7:
    logo_height = 20  # Custom height for logo 07
elif logo_num_int == 3:
    logo_height = 15  # Custom height for logo 03
else:
    logo_height = 18  # Default height
```

## 🔧 Advanced Usage

### Create an Alias
```bash
alias ff='python3 ~/.config/fastfetch/fastfetch_randomizer.py && fastfetch'
```

### Run on Terminal Startup Only
```bash
# Add to shell config for new terminals only
if [[ -o interactive ]]; then
    python3 ~/.config/fastfetch/fastfetch_randomizer.py
    fastfetch
fi
```

### Debug Mode
Uncomment the print statements in the script to see detailed operation logs.

## 🛠️ Requirements

- **Python 3.6+**
- **Fastfetch** (installed and configured)
- **Logo files** in `~/.config/fastfetch/logo/` (numbered 01-10)

## 🐛 Troubleshooting

### Logo Not Showing?
1. Check if the image file exists and is readable
2. Try different height values for that specific logo
3. Verify the file format (PNG recommended)
4. Run the script manually to see error messages

### Script Not Running?
1. Ensure Python 3 is installed: `python3 --version`
2. Check file permissions: `ls -la ~/.config/fastfetch/fastfetch_randomizer.py`
3. Verify the path in your shell config file

### Config Not Updating?
1. Check if `~/.config/fastfetch/config.jsonc` exists
2. Ensure you have write permissions to the config directory
3. Look for backup files (`.backup` extension) if something went wrong

## 🤝 Contributing

Found a bug or have a feature request? 
- 🐛 **Issues**: [Report bugs or request features](https://github.com/mahoraga777/fastfetch-random-logo/issues)
- 🔄 **Pull Requests**: [Contribute improvements](https://github.com/mahoraga777/fastfetch-random-logo/pulls)
- ⭐ **Star**: [Show your support!](https://github.com/mahoraga777/fastfetch-random-logo)

## 📄 License

MIT License - feel free to use, modify, and distribute!

## 🙏 Acknowledgments

- **Fastfetch Team** - For the amazing system info tool
- **Terminal Enthusiasts** - For inspiring dynamic terminal experiences
- **Open Source Community** - For making tools like this possible

---

<div align="center">

**Made with ❤️ for terminal lovers**

[⭐ Star this repo](https://github.com/mahoraga777/fastfetch-random-logo) • [🐛 Report Bug](https://github.com/mahoraga777/fastfetch-random-logo/issues) • [🚀 Request Feature](https://github.com/mahoraga777/fastfetch-random-logo/issues)

</div>
