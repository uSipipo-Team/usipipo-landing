# uSipipo Landing Infrastructure Deployment Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Deploy the uSipipo landing page as a systemd service with Caddy reverse proxy routing.

**Architecture:** Flask app running on port 5000, managed by systemd, proxied by Caddy alongside existing Telegram Mini App on port 8000.

**Tech Stack:** Python 3.13, uv, Flask 3, systemd, Caddy

**Prerequisites:**
- Working directory: `/home/mowgli/usipipo/usipipo-landing`
- uv installed
- sudo access for systemd and Caddy configuration

---

### Task 1: Set up Python virtual environment with uv

**Files:**
- Working directory: `/home/mowgli/usipipo/usipipo-landing`

**Step 1: Navigate to project directory**

```bash
cd /home/mowgli/usipipo/usipipo-landing
```

**Step 2: Create/recreate virtual environment**

```bash
uv venv
```

Expected: Creates or recreates `.venv` directory with Python 3.13

**Step 3: Install dependencies**

```bash
uv sync
```

Expected: Installs flask, pydantic-settings, python-dotenv and dev dependencies

**Step 4: Verify installation**

```bash
.venv/bin/python -c "import flask; print(f'Flask {flask.__version__}')"
```

Expected: `Flask 3.x.x`

**Step 5: Commit**

```bash
git add .venv/
git commit -m "chore: set up python virtual environment with uv"
```

---

### Task 2: Create production environment configuration

**Files:**
- Create: `.env`

**Step 1: Copy example environment file**

```bash
cp example.env .env
```

**Step 2: Update .env with production values**

```bash
cat > .env << 'EOF'
# Flask
FLASK_ENV=production
FLASK_DEBUG=false
SECRET_KEY=usipipo-landing-prod-secret-key-change-in-production-$(date +%s)

# Application
APP_ENV=production
DEBUG=false
LOG_LEVEL=INFO

# Site
SITE_URL=https://usipipo.duckdns.org
SITE_NAME=uSipipo VPN
EOF
```

**Step 3: Verify .env contents**

```bash
cat .env
```

Expected: Shows production configuration with FLASK_ENV=production

**Step 4: Commit**

```bash
git add .env
git commit -m "chore: add production environment configuration"
```

Note: .env should be in .gitignore for actual secrets, this is for initial setup

---

### Task 3: Create systemd service unit file

**Files:**
- Create: `/etc/systemd/system/usipipo-landing.service`

**Step 1: Create systemd service file**

```bash
sudo tee /etc/systemd/system/usipipo-landing.service > /dev/null << 'EOF'
[Unit]
Description=uSipipo VPN Landing Page
After=network.target

[Service]
Type=simple
User=mowgli
WorkingDirectory=/home/mowgli/usipipo/usipipo-landing
Environment="PATH=/home/mowgli/usipipo/usipipo-landing/.venv/bin"
ExecStart=/home/mowgli/usipipo/usipipo-landing/.venv/bin/python -m src
Restart=always
RestartSec=5
NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF
```

**Step 2: Verify service file contents**

```bash
sudo cat /etc/systemd/system/usipipo-landing.service
```

Expected: Shows complete systemd service configuration

**Step 3: Reload systemd daemon**

```bash
sudo systemctl daemon-reload
```

Expected: No output (success)

**Step 4: Enable service to start on boot**

```bash
sudo systemctl enable usipipo-landing
```

Expected: `Created symlink ... usipipo-landing.service`

**Step 5: Start the service**

```bash
sudo systemctl start usipipo-landing
```

Expected: No output (success)

**Step 6: Verify service status**

```bash
sudo systemctl status usipipo-landing --no-pager
```

Expected: `Active: active (running)`

**Step 7: Test application health endpoint**

```bash
curl -s http://localhost:5000/health
```

Expected: `{"status":"healthy"}`

---

### Task 4: Update Caddyfile with routing configuration

**Files:**
- Modify: `/etc/caddy/Caddyfile`

**Step 1: Backup current Caddyfile**

```bash
sudo cp /etc/caddy/Caddyfile /etc/caddy/Caddyfile.backup.$(date +%Y%m%d-%H%M%S)
```

Expected: Creates backup file

**Step 2: Read current Caddyfile to understand structure**

```bash
sudo cat /etc/caddy/Caddyfile
```

**Step 3: Update Caddyfile with new routing configuration**

```bash
sudo tee /etc/caddy/Caddyfile > /dev/null << 'EOF'
usipipo.duckdns.org {
    # Landing Page - everything except /miniapp/*
    @landing {
        not path /miniapp/*
    }
    reverse_proxy @landing localhost:5000

    # Telegram Mini App - only /miniapp/*
    @miniapp path /miniapp/*
    reverse_proxy @miniapp localhost:8000

    encode gzip zstd

    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        X-Content-Type-Options "nosniff"
        X-Frame-Options "DENY"
        X-XSS-Protection "1; mode=block"
        Referrer-Policy "strict-origin-when-cross-origin"
    }

    log {
        output file /var/log/caddy/usipipo.log
        format json
    }
}
EOF
```

**Step 4: Validate Caddy configuration**

```bash
sudo caddy validate --config /etc/caddy/Caddyfile
```

Expected: `Valid configuration`

**Step 5: Reload Caddy**

```bash
sudo systemctl reload caddy
```

Expected: No output (success)

**Step 6: Verify Caddy status**

```bash
sudo systemctl status caddy --no-pager
```

Expected: `Active: active (running)`

---

### Task 5: Verify complete deployment

**Files:**
- N/A (verification only)

**Step 1: Test Landing Page root endpoint**

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/
```

Expected: `200` or `302` (redirect to home)

**Step 2: Test Landing Page health endpoint**

```bash
curl -s http://localhost:5000/health
```

Expected: `{"status":"healthy"}`

**Step 3: Test Mini App endpoint still works**

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/miniapp/entry
```

Expected: `200`

**Step 4: Check systemd service logs**

```bash
sudo journalctl -u usipipo-landing --no-pager -n 20
```

Expected: Recent logs showing successful startup

**Step 5: Check Caddy logs**

```bash
sudo tail -20 /var/log/caddy/usipipo.log
```

Expected: JSON formatted access logs

**Step 6: Verify both services are running**

```bash
systemctl is-active usipipo-landing && systemctl is-active caddy
```

Expected: `active` (twice)

**Step 7: Final summary**

```bash
echo "=== Deployment Summary ==="
echo "Landing Page: http://localhost:5000"
echo "Mini App: http://localhost:8000/miniapp/"
echo "Caddy routing: usipipo.duckdns.org"
systemctl status usipipo-landing --no-pager | grep -E "Active|Main PID"
systemctl status caddy --no-pager | grep -E "Active|Main PID"
```

---

## Rollback Instructions

If something goes wrong:

### Rollback Caddy configuration:
```bash
# Find most recent backup
ls -lt /etc/caddy/Caddyfile.backup.* | head -1
# Restore
sudo cp /etc/caddy/Caddyfile.backup.YYYYMMDD-HHMMSS /etc/caddy/Caddyfile
sudo systemctl reload caddy
```

### Stop Landing service:
```bash
sudo systemctl stop usipipo-landing
sudo systemctl disable usipipo-landing
sudo rm /etc/systemd/system/usipipo-landing.service
sudo systemctl daemon-reload
```

---

## Success Criteria

- ✅ `curl http://localhost:5000/health` returns `{"status":"healthy"}`
- ✅ `systemctl status usipipo-landing` shows `active (running)`
- ✅ `systemctl status caddy` shows `active (running)`
- ✅ Landing Page accessible at `https://usipipo.duckdns.org/`
- ✅ Mini App accessible at `https://usipipo.duckdns.org/miniapp/entry`
- ✅ Both services restart automatically on failure
