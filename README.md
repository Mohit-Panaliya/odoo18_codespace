
# 📂 Preparation

Before starting, ensure your three master scripts are saved in the root directory:

* `setup_env.sh`
* `install_deps.sh`
* `run.sh`

### 1️⃣ Open the Terminal

### 2️⃣ Grant Execution Permissions

```bash
chmod +x *.sh
```

---

# 🛠️ Step 1: Infrastructure Initialization

This step installs the PostgreSQL server, required system headers, and the Odoo source code.

### ▶ Run:

```bash
./setup_env.sh
```

### ✅ Status Check

Wait until you see:

```
✅ Infrastructure Ready!
```

---

# 🐍 Step 2: Python Environment & Dependencies

This step creates the virtual environment and installs the patched Odoo dependencies.

### 1️⃣ Activate the Virtual Environment

```bash
source odoo-venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
./install_deps.sh
```

### ✅ Status Check

Wait until you see:

```
🚀 Python Environment Ready!
```

---

# 🚀 Step 3: Launch Odoo

This step starts the database services and launches the Odoo web server.

### ▶ Run:

```bash
./run.sh
```

### ✅ Status Check

You should see:

```
HTTP service (werkzeug) running on localhost:8069
```

---

# 🌐 Step 4: Web Browser Configuration

1. Click **"Open in Browser"** from the Codespaces popup.
2. Complete the **Database Management** form using the following values:

| Field           | Value      |
| --------------- | ---------- |
| Master Password | `admin`    |
| Database Name   | `odoo_dev` |
| Email (Login)   | `admin`    |
| Password        | `admin`    |

3. Click **Create Database**

⏳ This process may take up to 2 minutes.

---
