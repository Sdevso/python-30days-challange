# 🐍 30-Day Python for DevOps - Learning Tracker

Welcome to the **Fail-Proof, Hands-On Python Learning Plan** for DevOps Engineers! This repo is designed to help you build **real-world automation skills** in Python, step by step.

> ⏱️ Avg Time: 30 mins/day | 📍 Format: Concept → Code → Real Use | 💻 Focus: DevOps, Infra, Automation

---

## 📅 Weekly Breakdown

### ✅ Week 1: Python Scripting Fundamentals
| Day | Topic | Concepts | Mini Project/Script |
|-----|-------|----------|----------------------|
| 1 | Setup & Print | Python install, VS Code, `print()` | Hello Python DevOps Script |
| 2 | Variables | `str`, `int`, `bool`, `list` | Server inventory with metadata |
| 3 | Input + f-strings | `input()`, `f"..."` | Ask server name, print status |
| 4 | Conditions | `if/elif/else` | Health checker logic |
| 5 | Loops | `for`, `while` | Service restart loop |
| 6 | Functions | `def`, `return` | Wrap logic into `check_status()` |
| 7 | Modules | `os`, `sys` | File Checker Module |

---

### ✅ Week 2: Files, Shell, Configs
| Day | Topic | Concepts | Mini Project/Script |
|-----|-------|----------|----------------------|
| 8 | Read Files | `open()`, `read()` | Read server list from file |
| 9 | Write/Append | `'w'`, `'a'` | Write output to log file |
|10 | CLI Args | `sys.argv` | Pass input/output file to script |
|11 | Exceptions | `try/except` | Handle missing files |
|12 | Shell Commands | `subprocess.run()` | Run `ping`, `kubectl` |
|13 | JSON Configs | `json.load()` | Read config.json |
|14 | YAML Parsing | `pyyaml`, `configparser` | Parse NGINX config |

---

### ✅ Week 3: Automation & Mini Workflows
| Day | Topic | Concepts | Mini Project/Script |
|-----|-------|----------|----------------------|
|15 | System Monitor | `psutil` | Alert on CPU > 80% |
|16 | File Backup | `shutil`, `os.path` | Backup config with timestamp |
|17 | Email Alert | `smtplib` | Email on disk full |
|18 | API Calls | `requests.get()` | Get GitHub user data |
|19 | Git Automate | `subprocess` | Git pull & log checker |
|20 | HTTP Server | `http.server` | Serve local log files |
|21 | Env Vars | `os.environ` | Load credentials securely |

---

### ✅ Week 4: Combine & Apply
| Day | Topic | Concepts | Mini Project/Script |
|-----|-------|----------|----------------------|
|22 | Errors Deep Dive | Custom exceptions | Retry on connection fail |
|23 | Dictionaries | `dict`, loops | Server metadata handler |
|24 | OOP Basics | `class`, `__init__` | `Server` class abstraction |
|25 | External Libs | `pip install`, `tabulate` | Pretty report |
|26 | SDKs & Cloud | `azure`, `boto3` | List Azure/AWS resources |
|27 | CI/CD Scripts | GitHub/Jenkins logic | Version bump, tag script |
|28 | Logging | `logging` | Replace print in scripts |
|29 | Templating | `jinja2` | Generate config from template |
|30 | Review & Reflect | Git cleanup, README | Final commit, push to GitHub |

---

## 🧠 Logic Building Tips
- Use pen & paper to **draw flowcharts** for any script
- Use `print()` or `logging.debug()` for step-by-step tracing
- Write `assert` statements to test your logic early

---

## 📁 Folder Structure Example
```bash
python-for-devops-30day/
├── week1/
│   ├── day1_hello.py
│   ├── day2_variables.py
│   └── ...
├── week2/
├── week3/
├── week4/
├── config/
│   ├── config.json
│   └── config.yaml
├── logs/
├── README.md
```

---

## 📦 Final Projects
- 🔍 **Log File Parser** (Regex, File I/O)
- 🔔 **Health Monitor + Email** (System monitor + Alert)
- ⚙️ **Auto Config Generator** (Template engine)
- 🚀 **DevOps Toolbox CLI** (OOP + CLI args + subprocess)

---

## 🔗 Resources
- [Real Python](https://realpython.com)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/)
- [Python DevOps Projects](https://github.com/search?q=python+devops&type=repositories)

---

## 📌 How to Use This Repo
1. Create a new branch: `learning/python-devops`
2. Commit daily: `git commit -m "Day 3: Input and f-strings"`
3. Reflect and share progress weekly on LinkedIn
4. Reuse scripts in real automation tasks!

---

## 🎓 Next Steps After 30 Days
- Write pytest unit tests for each script
- Convert into a Python Package (CLI)
- Automate your DevOps pipelines with Python helpers

---

Happy Learning! 🚀  
**#LearnPython #DevOps #Automation #100DaysOfCode**