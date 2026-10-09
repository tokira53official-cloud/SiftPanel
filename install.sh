#!/usr/bin/env bash
set -Eeuo pipefail

if [[ $EUID -ne 0 ]]; then
echo "Please run this installer as root."
exit 1
fi

echo "========================================"
echo "          SIFTPANEL INSTALLER"
echo "========================================"

if ! command -v apt-get >/dev/null 2>&1; then
echo "This installer currently supports Ubuntu/Debian only."
exit 1
fi

export DEBIAN_FRONTEND=noninteractive

echo "[1/5] Updating packages..."
apt-get update

echo "[2/5] Installing dependencies..."
apt-get install -y python3 python3-venv python3-pip git curl ca-certificates

echo "[3/5] Setting up SiftPanel directory..."
mkdir -p /opt/siftpanel

if [[ -d "./panel" ]]; then
cp -a ./panel/. /opt/siftpanel/
else
echo "ERROR: The panel directory is missing."
echo "Please download the complete repository and run this script from its root."
exit 1
fi

if [[ ! -f /opt/siftpanel/app.py ]]; then
echo "ERROR: panel/app.py is missing."
echo "The panel application file must be added before installation."
exit 1
fi

echo "[4/5] Creating Python environment..."
python3 -m venv /opt/siftpanel/venv
/opt/siftpanel/venv/bin/pip install --upgrade pip

if [[ -f /opt/siftpanel/requirements.txt ]]; then
/opt/siftpanel/venv/bin/pip install -r /opt/siftpanel/requirements.txt
fi

echo "[5/5] Creating system service..."
cat >/etc/systemd/system/siftpanel.service <<'SERVICE'
[Unit]
Description=SiftPanel Web Panel
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/siftpanel
ExecStart=/opt/siftpanel/venv/bin/python /opt/siftpanel/app.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
SERVICE

systemctl daemon-reload
systemctl enable siftpanel

echo
echo "Installation files prepared successfully."
echo "The panel application must be configured before the service can start."
echo "Next, add the remaining SiftPanel application files."
echo
echo "Do not expose the panel publicly until authentication and HTTPS are configured."
