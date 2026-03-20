# Changelog

All notable changes to uSipipo VPN Landing Page will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-19

### 🎉 Initial Release

Primer release oficial de la Landing Page de uSipipo VPN.

### ✨ Features

- **Landing Page Completa** - Página de aterrizaje con diseño cyberpunk neon night
- **Múltiples Páginas**:
  - Home con hero section y call-to-action a Telegram
  - Pricing con planes de suscripción
  - Docs con documentación del servicio
  - Status page para monitoreo
- **Diseño Cyberpunk** - Estética Neon Night con colores neón (cyan, magenta, verde terminal)
- **Sección de Protocolos** - Información sobre Outline, WireGuard y Trust Tunnel
- **Sección de Ubicaciones** - Información de servidores en Estados Unidos
- **FAQ Interactivo** - Acordeón de preguntas frecuentes
- **Integración con Telegram** - Enlaces directos a @uSipipo_Bot

### 🔧 Infrastructure

- **Python 3.13** - Runtime actualizado
- **Flask 3.1.3** - Framework web moderno
- **uv Package Manager** - Gestión rápida de dependencias
- **systemd Service** - Servicio del sistema para producción
- **Caddy Reverse Proxy** - Proxy inverso con TLS automático
- **Routing Inteligente**:
  - `/` → Landing Page (puerto 5000)
  - `/miniapp/*` → Telegram Mini App (puerto 8000)

### 📄 Documentation

- **README Profesional** - Documentación completa con badges y CTAs
- **LICENSE** - MIT License
- **CONTRIBUTING.md** - Guía para contribuidores
- **Code Quality Rules** - Reglas de calidad de código Linus Torvalds para agentes IA

### 🐛 Bug Fixes

- **pyproject.toml** - Corregida coma extra en dependencias de desarrollo

### 🔒 Security

- **Security Headers** - HSTS, X-Frame-Options, X-Content-Type-Options, CSP
- **HTTPS Forzado** - Redirección automática HTTP → HTTPS
- **NoNewPrivileges** - Hardening del servicio systemd

---

## Unreleased

Changes that have been committed but not yet released.

[0.1.0]: https://github.com/uSipipo-Team/usipipo-landing/releases/tag/v0.1.0
