# Guía de Reproducción — Realidad I.O

Este documento proporciona instrucciones paso a paso para reproducir las verificaciones formales del marco **Realidad I.O**.

## Requisitos

- Cuenta de GitHub (para usar Codespaces) **O** instalación local de Lean 4.9.0 y Python 3.9+
- Navegador web moderno (Chrome, Firefox, Edge)

## Opción A: Reproducción en la nube (recomendada, sin instalación)

### 1. Abrir el repositorio en Codespaces

1. Ve a: https://github.com/luisreygarciafigueroa-creator/IOM
2. Toca el botón verde **<> Code**
3. Selecciona la pestaña **Codespaces**
4. Toca **Create codespace on main**
5. Espera 2-5 minutos mientras se configura el entorno (Lean 4 se instala automáticamente)

### 2. Verificar los 16 teoremas de Lean 4

Abre la terminal (☰ → Terminal → New Terminal) y ejecuta:

```bash
lake build
mkdir -p .devcontainer
cat << 'EOF' > .devcontainer/devcontainer.json
{
  "name": "IOM - Realidad I.O",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    }
  },
  "postCreateCommand": "curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y --default-toolchain leanprover/lean4:v4.9.0 && source $HOME/.elan/env && pip install rdflib pyshacl",
  "postAttachCommand": "source $HOME/.elan/env",
  "customizations": {
    "vscode": {
      "extensions": [
        "leanprover.lean4"
      ]
    }
  }
}
