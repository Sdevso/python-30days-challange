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

## 🚀 Quick Start

1. **Clone the Repository**
   ```powershell
   git clone https://github.com/yourusername/python-30days.git
   cd python-30days
   ```

2. **Set Up Environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. **Start Learning!**
   - Begin with Week 1, Day 1
   - Complete daily challenges
   - Track your progress
   - Share your solutions

## 📚 Course Structure

### Week 1: Python Fundamentals & System Operations
- Day 1: Hello DevOps - Your First Automation Script
- Day 2: Server Inventory Management
- Day 3: Interactive Status Checker
- Day 4: Health Monitoring System
- Day 5: Service Management
- Day 6: Status Check Functions
- Day 7: File Operations & Logging

### Week 2: Error Handling & API Integration
- Day 8-9: Robust Error Handling & Logging
- Day 10-11: Configuration Management
- Day 12: Log Analysis with Regex
- Day 13: Unit Testing Your Code
- Day 14: REST API Integration

### Week 3: Databases & Task Automation
- Day 15: Database Operations
- Day 16: Parallel Processing
- Day 17: SSH Operations
- Day 18: Alert System
- Day 19: Web Dashboard
- Day 20: Data Visualization
- Day 21: Task Scheduler

### Week 4: Cloud & Containers
- Day 22: Docker Management
- Day 23: AWS Automation
- Day 24: Kubernetes Operations
- Day 25: CI/CD Pipeline
- Day 26: Monitoring Integration
- Day 27: Security Automation
- Day 28-30: Final Project

## 🛠️ Technologies Covered

- **Languages:** Python 3.8+
- **Cloud:** AWS, Docker, Kubernetes
- **Databases:** SQLite, PostgreSQL
- **Tools:** Git, CI/CD, Monitoring
- **Libraries:** boto3, paramiko, flask

## 🌟 Features

- 📝 Detailed explanations
- 💻 Practical examples
- 🔄 Progressive difficulty
- 🎯 Clear learning goals
- 📊 Real-world projects

## 🏆 Learning Path

1. **Foundation (Week 1)**
   - Python basics for automation
   - System operations
   - File handling

2. **Building Blocks (Week 2)**
   - Error handling
   - Testing
   - API integration

3. **Advanced Topics (Week 3)**
   - Database management
   - Web development
   - Task automation

4. **Professional Skills (Week 4)**
   - Cloud integration
   - Container orchestration
   - Security automation

## 🤝 Contributing

Your contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📖 Resources

- [Python Documentation](https://docs.python.org/3/)
- [DevOps Best Practices](https://devops.com/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

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

## 🔗 Getting Started

1. Clone the repository and create a Python virtual environment
2. Install required packages: `pip install -r requirements.txt`
3. Start with Week 1, Day 1 and progress through each day
4. Complete the challenges and exercises
5. Use the hints and documentation when needed

---

# 🚀 Python for DevOps: 30-Day Learning Adventure

Master Python for DevOps through hands-on projects! This practical, project-based course takes you from basics to advanced DevOps automation in 30 days.

[![GitHub stars](https://img.shields.io/github/stars/yourusername/python-30days?style=social)](https://github.com/yourusername/python-30days)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 What You'll Learn

- **Week 1:** Python Fundamentals & System Operations
- **Week 2:** Advanced Error Handling & API Integration
- **Week 3:** Database Operations & Task Automation
- **Week 4:** Cloud & Container Orchestration

## 💡 Why This Course?

- 🔨 **Practical Projects:** Real-world automation tasks
- 🎓 **Progressive Learning:** From basics to advanced
- 🛠️ **Modern Tools:** Docker, Kubernetes, AWS, and more
- 👥 **Community Driven:** Share and learn together

## Week 1: Basic Python and System Operations

### Day 1: Hello DevOps
- **Challenge**: Create a simple Python script that prints "Hello DevOps" and the current time
- **Skills**: Basic Python syntax, importing modules (time module)
- **File**: `week1/day1_hello_devops.py`

### Day 2: Server Inventory Reader
- **Challenge**: Read and display server inventory from a JSON file
- **Skills**: JSON handling, file operations, data structures
- **File**: `week1/day2_server_inventory.py`
- **Hint**: Use the `json` module to parse the inventory file

### Day 3: Interactive Server Status
- **Challenge**: Allow users to input server names and display their details
- **Skills**: User input handling, string manipulation, conditional statements
- **File**: `week1/day3_input_status.py`
- **Hint**: Use `.split()` for handling comma-separated input

### Day 4: Server Health Checker
- **Challenge**: Create a script to check server health status
- **Skills**: Boolean operations, dictionaries, error handling
- **File**: `week1/day4_health_checker.py`

### Day 5: Service Monitor
- **Challenge**: Monitor multiple services running on servers
- **Skills**: Loops, lists, conditional statements
- **File**: `week1/day5_service_loops.py`

### Day 6: Status Check Function
- **Challenge**: Create reusable functions for checking server status
- **Skills**: Functions, parameters, return values
- **File**: `week1/day6_check_status_function.py`

### Day 7: File Operations
- **Challenge**: Work with system files and perform basic operations
- **Skills**: File handling, path operations, error handling
- **File**: `week1/day7_file_checker.py`

## Week 2: Intermediate Python for DevOps

### Day 8: Error Handling
- **Challenge**: Implement proper error handling in server operations
- **Skills**: Try-except blocks, raising exceptions
- **File**: `week2/day8_error_handling.py`

### Day 9: Logging Implementation
- **Challenge**: Add logging to server monitoring scripts
- **Skills**: Python logging module, file handlers
- **File**: `week2/day9_logging_impl.py`

### Day 10: Configuration Management
- **Challenge**: Create a configuration management system
- **Skills**: ConfigParser, YAML handling
- **File**: `week2/day10_config_management.py`

### Day 11: Command Line Arguments
- **Challenge**: Add CLI arguments to your scripts
- **Skills**: argparse module, command line interfaces
- **File**: `week2/day11_cli_arguments.py`

### Day 12: Regular Expressions
- **Challenge**: Use regex for log parsing
- **Skills**: re module, pattern matching
- **File**: `week2/day12_regex_parser.py`

### Day 13: Unit Testing
- **Challenge**: Write tests for your server monitoring functions
- **Skills**: unittest module, assertions
- **File**: `week2/day13_unit_testing.py`

### Day 14: Working with APIs
- **Challenge**: Interact with a REST API
- **Skills**: requests module, HTTP methods
- **File**: `week2/day14_api_interaction.py`

## Week 3: Advanced Python for DevOps

### Day 15: Database Operations
- **Challenge**: Store server data in a SQLite database
- **Skills**: SQL, sqlite3 module
- **File**: `week3/day15_database_ops.py`

### Day 16: Parallel Processing
- **Challenge**: Implement parallel server checks
- **Skills**: multiprocessing, threading
- **File**: `week3/day16_parallel_proc.py`

### Day 17: SSH Operations
- **Challenge**: Execute commands over SSH
- **Skills**: paramiko module, SSH protocol
- **File**: `week3/day17_ssh_operations.py`

### Day 18: Email Notifications
- **Challenge**: Send email alerts for server status
- **Skills**: smtplib, email formatting
- **File**: `week3/day18_email_notifications.py`

### Day 19: Web Dashboard
- **Challenge**: Create a simple web dashboard for server status
- **Skills**: Flask framework, basic HTML
- **File**: `week3/day19_web_dashboard.py`

### Day 20: Data Visualization
- **Challenge**: Create graphs of server metrics
- **Skills**: matplotlib, data visualization
- **File**: `week3/day20_data_visualization.py`

### Day 21: Scheduled Tasks
- **Challenge**: Schedule periodic server checks
- **Skills**: schedule module, cron-like operations
- **File**: `week3/day21_scheduled_tasks.py`

## Week 4: DevOps Integration Projects

### Day 22: Docker Integration
- **Challenge**: Create Docker container management scripts
- **Skills**: Docker SDK for Python
- **File**: `week4/day22_docker_integration.py`

### Day 23: AWS Integration
- **Challenge**: Work with AWS services using boto3
- **Skills**: boto3, AWS SDK
- **File**: `week4/day23_aws_integration.py`

### Day 24: Kubernetes Integration
- **Challenge**: Manage Kubernetes resources
- **Skills**: kubernetes-client
- **File**: `week4/day24_kubernetes_integration.py`

### Day 25: CI/CD Pipeline Script
- **Challenge**: Create a script for CI/CD pipeline tasks
- **Skills**: Git integration, pipeline automation
- **File**: `week4/day25_cicd_pipeline.py`

### Day 26: Monitoring Integration
- **Challenge**: Integrate with monitoring systems
- **Skills**: Prometheus, Grafana APIs
- **File**: `week4/day26_monitoring_integration.py`

### Day 27: Security Scanning
- **Challenge**: Implement security scanning scripts
- **Skills**: Security tools integration
- **File**: `week4/day27_security_scanning.py`

### Day 28-30: Final Project
- **Challenge**: Build a complete DevOps automation tool
- **Skills**: All previous concepts combined
- **Files**: 
  - `week4/day28_final_project_part1.py`
  - `week4/day29_final_project_part2.py`
  - `week4/day30_final_project_part3.py`

## Getting Started

1. Clone this repository
2. Create a Python virtual environment
3. Install required packages: `pip install -r requirements.txt`
4. Complete each day's challenge
5. Check the hints and documentation when needed

## Notes
- Each script builds upon skills learned in previous days
- Focus on writing clean, well-documented code
- Test your scripts thoroughly
- Use proper error handling
- Follow Python best practices

---

## 📈 Project Roadmap

- [x] Basic Python automation
- [x] System operations
- [x] Error handling
- [x] API integration
- [x] Database operations
- [x] Cloud automation
- [ ] Mobile app integration
- [ ] AI/ML integration

## 📝 Additional Resources

Need help? Check out:
- [FAQ.md](FAQ.md) for common questions
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for technical issues
- [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines

## 📚 References

- [Python Documentation](https://docs.python.org/3/)
- [DevOps Best Practices](https://devops.com/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)