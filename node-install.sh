#!/usr/bin/env bash
set -Eeuo pipefail

if [[ $EUID -ne 0 ]]; then
echo "Please run this installer as root."
exit 1
fi

clear
echo "========================================"
echo "       SIFTPANEL NODE INSTALLER"
echo "========================================"
echo
echo "This prepares an Ubuntu/Debian server for the SiftPanel node agent."
echo "The node agent must be installed separately before this node can manage servers."
echo

if ! command -v apt-get >/dev/null 2>&1; then
echo "This installer currently supports Ubuntu/Debian only."
exit 1
fi

export DEBIAN_FRONTEND=noninteractive

echo "[1/3] Updating system..."
apt-get update

echo "[2/3] Installing basic dependencies..."
apt-get install -y python3 python3-venv python3-pip curl ca-certificates

echo "[3/3] Creating node directory..."
mkdir -p /opt/siftpanel-node
chmod 750 /opt/siftpanel-node

echo
echo "Node prerequisites installed."
echo "The node agent and secure panel-to-node authentication are not configured yet."
echo "Do not run public workloads until those components are installed and secured."
