# 🚀 FastAPI Starter Kit

A production-ready template for building APIs with FastAPI. Get started quickly with best practices already in place! ⚡

## 📖 Description

FastAPI Starter Kit provides a well-structured and scalable foundation for building high-performance APIs with FastAPI. It includes pre-configured best practices such as code linting, type checking, and a structured project layout to accelerate development and ensure maintainability. 🏗️

## 🛠️ Getting Started

### ✅ Prerequisites

-   Python 3.8 or higher 🐍
-   pip (Python package installer) 📦
-   virtualenv or venv 🔒

### 🔧 Development Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/matthewdinata/fastapi-starter-kit.git <new-repository-name>
    cd <repository-name>
    ```

2. **Initialize a fresh git repository:**

    ```sh
    rm -rf .git
    git init
    ```

3. **Create and activate a virtual environment:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux 🍏🐧
    .venv\Scripts\activate     # On Windows 🖥️
    ```

4. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

5. **Set up pre-commit hooks:**
    ```sh
    pre-commit install
    ```

### 🎯 Working with Pre-Commit Hooks

-   **Bypass hooks during commit:** 🚨

    ```sh
    git commit --no-verify
    ```

-   **Run hooks manually on all files:** 🔄

    ```sh
    pre-commit run --all-files
    ```

-   **Update hooks:** 🔃
    ```sh
    pre-commit autoupdate
    ```

### 📂 Recommended Folder Structure

```
fastapi-starter-kit/
├── src/
│   ├── main.py          # 🚀 FastAPI application entry point
│   ├── api/             # 🌍 API routes and endpoints
│   ├── core/            # ⚙️ Core configurations
│   ├── models/          # 🗄️ Database models
│   ├── schemas/         # 📜 Pydantic models for request/response
│   └── services/        # 🏗️ Business logic
├── .env                 # 🔑 Environment variables
├── .flake8
├── mypy.ini
├── pyproject.toml
├── .gitignore
├── .pre-commit-config.yaml
├── requirements.txt     # 📦 Project dependencies
├── requirements-dev.txt # 🛠️ Project dev dependencies
└── README.md
```

### 📌 Folder Descriptions

**src/**: Main application package 📁

-   **main.py**: FastAPI application initialization and configuration 🚀
-   **api/**: Contains all API routes organized by versions 🌍
-   **core/**: Core configurations and utilities ⚙️
-   **models/**: SQLAlchemy models for database tables 🗄️
-   **schemas/**: Pydantic models for request/response validation 📜
-   **services/**: Business logic and external service integrations 🏗️

### 🤖 CI Integration

#### GitLab CI/CD 🏗️

Add the following to `.gitlab-ci.yml`:

```yaml
lint:
    script:
        - pip install pre-commit
        - pre-commit run --all-files
```

#### GitHub Actions 🚀

Include the following step in your workflow:

```yaml
- name: Run Pre-Commit Hooks
  run: |
      pip install pre-commit
      pre-commit run --all-files
```

### 🔍 Code Quality

Your `.pre-commit-config.yaml` ensures that the project maintains high code quality by including:

-   **Code formatting** (black) 🎨
-   **Import sorting** (isort) 📂
-   **Linting** (flake8) 🕵️‍♂️
-   **Type checking** (mypy) 🔢
-   **Basic file checks** (trailing whitespace, YAML validation, etc.) ✅

## 👨‍💻 Prepared By

This FastAPI Starter Kit was prepared by Matthew Dinata.

Feel free to reach out for questions!
