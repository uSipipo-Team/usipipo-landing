# uSipipo Landing - Project Context

## 📋 Overview

**usipipo-landing** is the official marketing landing page for uSipipo VPN. It showcases the service features, pricing, and provides a gateway to the Telegram bot for user onboarding.

**Current Version:** v0.1.0  
**Status:** Production Ready  
**Framework:** Flask 3+  
**Design:** Cyberpunk Neon Night theme

---

## 🏗️ Architecture

### Project Structure

```
src/
├── __init__.py
├── __main__.py
├── core/
│   ├── config/
│   │   └── settings.py       # Pydantic settings
│   └── domain/
│       └── entities/         # Domain entities
├── features/
│   ├── home/
│   │   ├── __init__.py
│   │   └── home_routes.py    # Landing page
│   ├── pricing/
│   │   ├── __init__.py
│   │   └── pricing_routes.py # Pricing section
│   └── about/
│       ├── __init__.py
│       └── about_routes.py   # About section
├── infrastructure/
│   └── web/
│       ├── app.py            # Flask app factory
│       ├── templates/        # Jinja2 templates
│       │   ├── base.html
│       │   ├── index.html
│       │   └── components/
│       └── static/
│           ├── css/
│           │   └── style.css # Cyberpunk theme
│           ├── js/
│           └── images/
└── shared/
    ├── __init__.py
    └── utils.py
```

### Design System

**Colors (Cyberpunk Neon Night):**

```css
:root {
  --primary: #00F0FF;      /* Cyan neon */
  --secondary: #FF00AA;    /* Magenta neon */
  --accent: #00FF41;       /* Terminal green */
  --background: #0A0A0F;   /* Void dark */
  --surface: #12121A;      /* Surface */
  --card: #1A1A24;         /* Card */
  --text: #FFFFFF;
  --text-muted: #A0A0A0;
}
```

**Typography:**

- **Headings:** JetBrains Mono (monospace)
- **Body:** Inter (readable)

---

## 🚀 Building and Running

### Prerequisites

- Python 3.13+
- uv package manager

### Local Development

```bash
cd usipipo-landing

# Install dependencies
uv sync --dev

# Configure environment
cp example.env .env

# Run tests
uv run pytest

# Start development server
uv run python -m src

# Or with Flask CLI
uv run flask --app src.main run --debug --port 5000
```

### Docker

```bash
# Build
docker build -t usipipo-landing .

# Run
docker run --env-file .env -p 5000:5000 usipipo-landing
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Flask secret key | ✅ | - |
| `APP_ENV` | Environment | ❌ | development |
| `DEBUG` | Debug mode | ❌ | false |
| `PORT` | Server port | ❌ | 5000 |
| `TELEGRAM_BOT_URL` | Telegram bot link | ❌ | https://t.me/uSipipo_Bot |

---

## 🧪 Testing

### Run Tests

```bash
# All tests
uv run pytest

# With coverage
uv run pytest --cov=src --cov-report=html

# Specific test
uv run pytest tests/features/test_home.py -v
```

### Test Structure

```
tests/
├── unit/
│   ├── test_routes/
│   └── test_utils/
├── integration/
│   └── test_app.py
└── conftest.py
```

---

## 📦 Features

### Sections

| Section | Description | Status |
|---------|-------------|--------|
| Hero | Main value proposition + CTA | ✅ |
| Features | VPN features showcase | ✅ |
| Pricing | Subscription plans | ✅ |
| About | Company information | ✅ |
| FAQ | Frequently asked questions | ✅ |
| Contact | Contact information | ✅ |

### Call-to-Action

| CTA | Destination | Status |
|-----|-------------|--------|
| "Start Now" | Telegram Bot | ✅ |
| "Get Key" | Telegram Bot | ✅ |
| "View Plans" | Pricing section | ✅ |

---

## 🔧 Development Conventions

### Code Style

- **Line Length:** 100 characters
- **Quote Style:** Double quotes
- **Indent:** 4 spaces
- **Type Hints:** Required for all public functions

### Route Pattern

```python
from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    """Render landing page"""
    return render_template('index.html')
```

### Template Pattern

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}uSipipo VPN - Secure & Private{% endblock %}

{% block content %}
<section class="hero">
    <h1>Secure VPN for LATAM</h1>
    <p>Get your VPN key in seconds via Telegram</p>
    <a href="{{ telegram_url }}" class="btn-primary">
        Start Now
    </a>
</section>
{% endblock %}
```

### CSS Pattern

```css
/* static/css/style.css */
.hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, var(--background), var(--surface));
}

.btn-primary {
    background: var(--primary);
    color: var(--background);
    padding: 1rem 2rem;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 20px var(--primary);
}
```

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `src/main.py` | Flask app entry |
| `src/__main__.py` | Python module entry |
| `src/features/` | Feature modules |
| `src/infrastructure/web/templates/` | Jinja2 templates |
| `src/infrastructure/web/static/` | Static assets |
| `pyproject.toml` | Project configuration |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CHANGELOG.md` | Version history |

---

## 🔗 Dependencies

### Runtime

- `flask>=3.0.0`
- `pydantic-settings>=2.0.0`
- `python-dotenv>=1.0.0`

### Development

- `pytest>=8.0.0`
- `pytest-flask>=1.3.0`
- `pytest-cov>=4.0.0`
- `mypy>=1.0.0`
- `ruff>=0.1.0`
- `pre-commit>=3.6.0`
- `bandit>=1.7.0`

---

## 📚 Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Deployment](docs/DEPLOYMENT.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

---

## 🔗 Links

- **GitHub:** https://github.com/uSipipo-Team/usipipo-landing
- **Production:** https://usipipo.com
- **Telegram Bot:** https://t.me/uSipipo_Bot

---

**Last Updated:** 2026-03-21  
**Maintained By:** uSipipo Team <dev@usipipo.com>
