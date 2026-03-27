# python-toolkit
A modular Python framework for user authentication and data management.
##  Project Overview | 项目概览

**[English]** This toolkit is a professional-grade authentication system built with Python. Unlike traditional linear scripts, it employs a **Layered Architecture** to separate data handling, utility functions, and application logic. This ensures the code is scalable and reusable for future software development.

**[中文]** 本项目是一个模块化的 Python 用户验证系统。它采用了**分层架构**，将数据处理、通用工具和业务逻辑完全解耦。这种设计不仅提升了代码的可读性，也方便我在未来的项目中直接复用这些底层模块。

---

##  Architecture | 目录架构

> **"Separation of Concerns" (关注点分离)** is the core philosophy of this project.

.
├── core_logic/           # Data persistence & validation (数据核心)
│   ├── __init__.py
│   ├── account_manager.py
│   └── user_data.json.example  # Template for database (数据库模板)
├── utils/                # General purpose tools (通用工具)
│   ├── __init__.py
│   └── user_input.py
├── my_apps/              # User-facing applications (应用接口)
│   ├── __init__.py
│   └── login_system.py
└── README.md             # Project documentation (项目文档)

* **`core_logic/`**: The "Back-end." Handles JSON reading/writing and credential validation. (数据核心：负责 JSON 读写与身份校验)
* **`utils/`**: The "Processors." Manages input cleaning, error trapping, and type conversion. (通用工具：负责输入清洗、异常捕获与类型转换)
* **`my_apps/`**: The "Interface." Implements the interactive Login/Register workflow. (应用接口：实现交互式的登录与注册流程)

---

##  Key Features | 技术亮点

* **Robust Input Validation (鲁棒性校验)**: Uses recursive loops and exception handling to ensure zero crashes from invalid user inputs. (通过循环和异常处理，确保程序不会因非法输入而崩溃。)
* **Data Persistence (数据持久化)**: Implements lightweight database functionality using structured JSON files. (利用 JSON 文件实现轻量级数据存储。)
* **Modular Design (模块化设计)**: Organized as Python packages (`__init__.py`), making it ready to be imported into any larger project. (标准化的包结构，可随时被集成到其他项目中。)

---

##  Reflection | 项目思考

**[English]** The biggest challenge was transitioning from "spaghetti code" to a modular structure. I spent significant time debugging cross-module imports and ensuring that the `core_logic` remained independent of the UI. This project deepened my understanding of how professional software handles complexity through abstraction.

**[中文]** 在这个项目中，我最大的挑战是从编写“面条式代码”转向“模块化架构”。我投入了大量精力处理跨模块导入问题，并确保底层逻辑独立于界面展示。这次实践让我深刻理解了专业软件如何通过“抽象”来管理复杂度，这对我未来的工程学习非常有启发。

---

##  Quick Start | 快速开始

1. **Clone the repo** / 克隆仓库。
2. **Setup Data**: Rename `core_logic/user_data.json.example` to `user_data.json`. / 将例子文件重命名为正式数据文件。
3. **Run**: Run `main_menu()` in `my_apps/login_system.py`. / 运行主菜单函数。
