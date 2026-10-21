#!/usr/bin/env bash
# Instala y activa el timer de usuario de systemd (no requiere sudo).
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.config/systemd/user
cp "$DIR/falabella-piloto.service" "$DIR/falabella-piloto.timer" ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now falabella-piloto.timer
# Para que corra aunque no tengas sesión gráfica abierta:
loginctl enable-linger "$USER"
echo "Timer instalado. Próxima ejecución:"
systemctl --user list-timers falabella-piloto.timer
