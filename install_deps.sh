#!/bin/bash
if [[ "$VIRTUAL_ENV" != *"odoo-venv"* ]]; then
    echo "❌ ERROR: Activate venv first: source odoo-venv/bin/activate"
    exit 1
fi

echo "🆙 Updating Core Build Tools..."
pip install --upgrade pip setuptools wheel

echo "🧹 Installing Odoo 18/19 Dependencies..."
# Newer versions of Odoo handle their requirements better,
# but we still ensure the core libraries are built correctly.
pip install -r odoo/requirements.txt

# Post-install fix for common Python 3.12 issues
pip install psycopg2-binary==2.9.9 python-ldap==3.4.4 inotify

echo "🚀 Python Environment for Odoo 18/19 Ready!"
