# 🎨 Fastfetch Random Logo

> Transform your terminal into a dynamic showcase with randomly rotating logos every time you open it!
> Best part about this is its simplicity and easy to config

![Terminal](https://img.shields.io/badge/Terminal-Enhanced-brightgreen)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Fastfetch](https://img.shields.io/badge/Fastfetch-Compatible-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🎲 **Random Logo Selection** - Automatically picks from your logo collection
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
cp -r fastfetch/* ~/.config/fastfetch/
```

### 3. **Make it Executable**
```bash
chmod +x ~/.config/fastfetch/fastfetch_randomizer.py
```

### 4. **Test the Script**
```bash
python3 ~/.config/fastfetch/fastfetch_randomizer.py
```

### 5. **Auto-Run Setup** (Choose your shell)

#### For **Zsh** users (`~/.zshrc`):
```bash
echo 'python3 ~/.config/fastfetch/fastfetch_randomizer.py' >> ~/.zshrc
source ~/.zshrc
```

#### For **Bash** users (`~/.bashrc`):
```bash
echo 'python3 ~/.config/fastfetch/fastfetch_randomizer.py' >> ~/.bashrc
source ~/.bashrc
```

#### For **Fish** users (`~/.config/fish/config.fish`):
```bash
echo 'python3 ~/.config/fastfetch/fastfetch_randomizer.py' >> ~/.config/fish/config.fish

```

#### Manual Setup:
Add these lines to your shell's config file:
```bash
python3 ~/.config/fastfetch/fastfetch_randomizer.py
```
## 🖌️ Customization

You can add any logo inside `~/.config/fastfetch/logo` and assign it a new number.  
Then, increase the number from 10 to any desired value in the Python code at **line 11**.  

> Note: The process isn’t simplified, but you should be able to manage it :) .


## 🛠️ Requirements

- **Python 3.6+**
- **Fastfetch** (installed and configured)
- **Logo files** in `~/.config/fastfetch/logo/` (numbered 01-10)

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
