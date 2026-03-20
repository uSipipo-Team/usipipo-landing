# 🛡️ uSipipo VPN Landing

<p align="center">
  <a href="https://github.com/uSipipo-Team/usipipo-landing/actions"><img src="https://img.shields.io/github/workflow/status/uSipipo-Team/usipipo-landing/main?style=flat-square" alt="Build"></a>
  <a href="https://github.com/uSipipo-Team/usipipo-landing/blob/main/LICENSE"><img src="https://img.shields.io/github/license/uSipipo-Team/usipipo-landing?style=flat-square" alt="License"></a>
  <a href="https://t.me/uSipipo_Bot"><img src="https://img.shields.io/badge/Chat-Telegram-blue?style=flat-square&logo=telegram" alt="Telegram"></a>
</p>

> Landing page oficial de uSipipo VPN — Tu proveedor de claves VPN seguras y privadas, diseñado para la comunidad LATAM.

## ✨ Características

- 🔑 **Keys Instantáneas** — Genera tu clave VPN en segundos desde Telegram
- 🌍 **Múltiples Protocolos** — Outline, WireGuard y Trust Tunnel
- 🔐 **Privacidad Total** — Política de NO LOGS. Tu tráfico es 100% privado
- ⚡ **Alta Velocidad** — Servidores optimizados para máximo rendimiento
- 🌎 **Enfoque LATAM** — Servicio diseñado para la comunidad latinoamericana
- 📱 **Fácil de Usar** — Todo desde Telegram, sin apps complicadas

## 🚀 Empezar

¿Listo para navegar seguro y privado?

<a href="https://t.me/uSipipo_Bot">
  <img src="https://img.shields.io/badge/Iniciar_en_Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Iniciar en Telegram">
</a>

### Demo

Ver el landing en producción: **[usipipo.com](https://usipipo.com)** (o la URL de producción)

## 🛠️ Tech Stack

- **Framework:** Flask 3+
- **Styling:** CSS Custom (Cyberpunk Neon Night)
- **Package Manager:** uv

## 📦 Desarrollo Local

```bash
# Clonar el repositorio
git clone https://github.com/uSipipo-Team/usipipo-landing.git
cd usipipo-landing

# Instalar dependencias
uv sync --dev

# Configurar entorno
cp example.env .env

# Ejecutar en desarrollo
uv run python -m src

# Ejecutar tests
uv run pytest
```

### Docker

```bash
# Build
docker build -t usipipo-landing .

# Ejecutar
docker run --env-file .env -p 5000:5000 usipipo-landing
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles.

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Distribuido bajo MIT License. Ver [LICENSE](LICENSE) para más información.

## 📱 Comunidad

- **Telegram:** [@uSipipo_Bot](https://t.me/uSipipo_Bot)
- **GitHub:** [uSipipo-Team](https://github.com/uSipipo-Team)

---

<p align="center">
  <subcode>Made with ❤️ by <a href="https://github.com/uSipipo-Team">uSipipo Team</a></subcode>
</p>
