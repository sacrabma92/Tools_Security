tools = {
    "gccgo": {"type": "apt", "command":"sudo apt install gccgo-go"},
    "assetfinder": {"type": "apt", "command": "sudo apt install assetfinder"},
    "golang": {"type": "apt", "command":"sudo apt install golang-go"},
    "amass": {"type": "apt", "command":"sudo apt install amass"},
    "naabu": {"type": "apt", "command":"sudo apt install naabu"},
    "dirsearch": {"type": "apt", "command":"sudo apt install dirsearch"},
    "anew": {"type": "go", "command": "go install -v github.com/tomnomnom/anew@latest"},
    "subfinder": {"type": "go", "command": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"},
    "httpx": {"type": "go", "command": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest"},
    "katana": {"type": "go", "command": "go install github.com/projectdiscovery/katana/cmd/katana@latest"},
    "hakrawler": {"type": "go", "command": "go install github.com/hakluke/hakrawler@latest"},
    "waybackurls": {"type": "go", "command": "go install github.com/tomnomnom/waybackurls@latest"},
}