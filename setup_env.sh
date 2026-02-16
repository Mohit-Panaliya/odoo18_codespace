#!/bin/bash
set -e
# --- CONFIGURATION ---
ODOO_VER="18.0" # Change to "master" for Odoo 19 (Odoo 19 is currently the master branch)
PYTHON_VER="3.12.8"
# ---------------------

WORKING_DIR=$(pwd)
echo "🧹 1. Cleaning up GPG keys and fixing repos..."
sudo rm -f /etc/apt/sources.list.d/yarn.list
sudo apt-key del 62D54FD4003F6525 2>/dev/null || true

echo "📦 2. Installing System Dependencies for Odoo $ODOO_VER..."
sudo apt-get update -y
sudo apt-get install -y postgresql postgresql-contrib libldap2-dev libsasl2-dev libpq-dev python3-dev build-essential wkhtmltopdf libjpeg-dev zlib1g-dev

echo "🐘 3. Configuring PostgreSQL Trust Mode..."
sudo service postgresql start
sudo sed -i 's/scram-sha-256/trust/g' /etc/postgresql/*/main/pg_hba.conf
sudo sed -i 's/md5/trust/g' /etc/postgresql/*/main/pg_hba.conf
sudo service postgresql restart

echo "📂 4. Initializing Python $PYTHON_VER..."
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if ! command -v pyenv &> /dev/null; then
    curl https://pyenv.run | bash
    eval "$(pyenv init -)"
fi
pyenv install $PYTHON_VER -s
pyenv local $PYTHON_VER

echo "📥 5. Cloning Odoo $ODOO_VER..."
if [ ! -d "odoo" ]; then
    git clone https://www.github.com/odoo/odoo --depth 1 --branch $ODOO_VER odoo
fi

if [ ! -d "odoo-venv" ]; then
    $(pyenv root)/versions/$PYTHON_VER/bin/python -m venv odoo-venv
fi

if [ ! -f "odoo.conf" ]; then
    cat <<EOF > odoo.conf
[options]
admin_passwd = admin
db_host = 127.0.0.1
db_user = odoo
db_password = odoo
db_port = 5432
addons_path = $WORKING_DIR/odoo/addons,$WORKING_DIR/custom_addons
EOF
fi

mkdir -p custom_addons
echo "✅ Infrastructure for Odoo $ODOO_VER Ready!"
