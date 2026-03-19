# Architecture

## Overview

Landing Page oficial de uSipipo VPN.

## Tech Stack

- **Framework:** Flask 3+
- **Package Manager:** uv
- **Styling:** CSS personalizado

## Project Structure

```
src/
├── __init__.py
├── __main__.py
├── core/
│   └── config/          # Configuración
├── features/
│   ├── home/            # Página de inicio
│   ├── pricing/         # Página de precios
│   ├── docs/            # Documentación
│   └── status/          # Estado del servicio
└── infrastructure/
    └── web/             # App Flask, templates, static
```

## Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Landing page principal |
| Pricing | `/pricing` | Planes y precios |
| Docs | `/docs` | Documentación |
| Status | `/status` | Estado del servicio |
