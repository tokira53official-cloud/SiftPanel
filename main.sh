#!/usr/bin/env bash
set -Eeuo pipefail

clear
echo "========================================"
echo "          SIFTNODES - SIFTPANEL"
echo "       Your Ultimate IT & Hosting Partner"
echo "========================================"
echo
echo "1) Install SiftPanel"
echo "2) Install SiftPanel Node"
echo "3) Exit"
echo
read -rp "Choose an option (1-3): " choice

case "$choice" in
1)
if [[ -f "./install.sh" ]]; then
bash ./install.sh
else
echo "ERROR: install.sh was not found."
echo "Download the complete SiftPanel repository first."
exit 1
fi
;;
2)
if [[ -f "./node-install.sh" ]]; then
bash ./node-install.sh
else
echo "ERROR: node-install.sh was not found."
echo "Download the complete SiftPanel repository first."
exit 1
fi
;;
3)
echo "Goodbye!"
exit 0
;;
*)
echo "Invalid option. Please run the installer again."
exit 1
;;
esac
