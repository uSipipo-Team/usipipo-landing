# Deployment

## Local Development

```bash
# Clonar repositorio
git clone https://github.com/uSipipo-Team/usipipo-landing.git
cd usipipo-landing

# Instalar dependencias
uv sync --dev

# Configurar entorno
cp example.env .env

# Ejecutar
uv run python -m src
```

## Docker

```bash
# Build
docker build -t usipipo-landing .

# Ejecutar
docker run --env-file .env -p 5000:5000 usipipo-landing
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Environment | development |
| `FLASK_DEBUG` | Debug mode | true |
| `SECRET_KEY` | Secret key for sessions | Required |
| `APP_ENV` | Application environment | development |
| `DEBUG` | Debug flag | true |
| `LOG_LEVEL` | Logging level | INFO |
| `SITE_URL` | Site URL | https://usipipo.com |
| `SITE_NAME` | Site name | uSipipo VPN |

## Production Deployment

TBD
