# usipipo-landing

> Landing Page oficial de uSipipo VPN

## Estado

- [x] En desarrollo
- [ ] Alpha
- [ ] Beta
- [ ] Producción

## Documentación

- [Architecture](docs/ARCHITECTURE.md)
- [Pages](docs/PAGES.md)
- [Deployment](docs/DEPLOYMENT.md)

## Desarrollo

```bash
# Clonar
git clone https://github.com/uSipipo-Team/usipipo-landing.git
cd usipipo-landing

# Instalar dependencias
uv sync --dev

# Configurar entorno
cp example.env .env

# Ejecutar tests
uv run pytest

# Ejecutar Landing
uv run python -m src
```

## Docker

```bash
# Build
docker build -t usipipo-landing .

# Ejecutar
docker run --env-file .env -p 5000:5000 usipipo-landing
```

## License

MIT © uSipipo
