# uSipipo Landing - Systemd Deployment Guide

Production-ready systemd service configuration for deploying the uSipipo VPN Landing Page on Linux servers.

## 📋 Prerequisites

Before deploying, ensure you have:

- **Python 3.13+** installed
- **Virtual environment** created and dependencies installed
- **`.env` file** configured with all required environment variables
- **Gunicorn** installed (for production WSGI server)

## 🚀 Quick Start

```bash
# 1. Navigate to deploy directory
cd /path/to/usipipo-landing/deploy

# 2. Copy service file to systemd directory
sudo cp usipipo-landing.service /etc/systemd/system/usipipo-landing.service

# 3. Edit the service file (replace placeholders)
sudo nano /etc/systemd/system/usipipo-landing.service

# 4. Create logs directory
sudo mkdir -p /path/to/usipipo-landing/logs
sudo chown <USER>:<GROUP> /path/to/usipipo-landing/logs

# 5. Reload systemd and enable service
sudo systemctl daemon-reload
sudo systemctl enable usipipo-landing
sudo systemctl start usipipo-landing

# 6. Verify status
sudo systemctl status usipipo-landing
```

## ⚙️ Configuration

### Required Placeholders

Open the service file and replace these placeholders:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `<SYSTEM_USER>` | Linux user to run the service | `mowgli`, `usipipo`, `www-data` |
| `<SYSTEM_GROUP>` | Linux group for the service | `mowgli`, `usipipo`, `www-data` |
| `<PATH_TO_USISIPO_LANDING>` | Absolute path to landing directory | `/home/mowgli/usipipo/usipipo-landing` |

### Finding Your User/Group

```bash
# Get current user info
id

# Output example:
# uid=1000(mowgli) gid=1000(mowgli) groups=1000(mowgli),...
# Use: User=mowgli Group=mowgli
```

### Environment Variables

The service loads environment variables from the `.env` file. Ensure these are set:

```bash
# Minimum required variables
FLASK_ENV=production
FLASK_DEBUG=false
SECRET_KEY=your-secret-key-here
APP_ENV=production
DEBUG=false
LOG_LEVEL=INFO
SITE_URL=https://usipipo.duckdns.org
```

See `example.env` in the root directory for all available options.

## 📖 Service Management Commands

### Basic Operations

```bash
# Start service
sudo systemctl start usipipo-landing

# Stop service
sudo systemctl stop usipipo-landing

# Restart service
sudo systemctl restart usipipo-landing

# Reload configuration
sudo systemctl reload usipipo-landing

# Check status
sudo systemctl status usipipo-landing
```

### Enable/Disable on Boot

```bash
# Enable automatic start on boot
sudo systemctl enable usipipo-landing

# Disable automatic start on boot
sudo systemctl disable usipipo-landing
```

### Viewing Logs

```bash
# View all logs (paged)
sudo journalctl -u usipipo-landing

# View logs in real-time (follow mode)
sudo journalctl -u usipipo-landing -f

# View logs from last hour
sudo journalctl -u usipipo-landing --since "1 hour ago"

# View logs with timestamps
sudo journalctl -u usipipo-landing -o short-precise

# View only errors
sudo journalctl -u usipipo-landing -p err

# View last N lines
sudo journalctl -u usipipo-landing -n 100
```

## 🔒 Security Hardening

This service file includes production-ready security configurations:

| Setting | Purpose |
|---------|---------|
| `ProtectSystem=strict` | Makes filesystem read-only except `ReadWritePaths` |
| `ProtectHome=false` | Allows access to home directory (required for `/home/` deployments) |
| `PrivateTmp=true` | Isolates `/tmp` from other processes |
| `NoNewPrivileges=true` | Prevents privilege escalation |
| `ReadWritePaths` | Restricts write access to logs directory only |
| `LimitNOFILE=65536` | Sets file descriptor limit |
| `LimitNPROC=4096` | Sets process limit |

## 🔧 Troubleshooting

### Service Won't Start

```bash
# Check detailed status
sudo systemctl status usipipo-landing -l

# Check journal logs
sudo journalctl -u usipipo-landing -n 50 --no-pager

# Validate service file syntax
sudo systemd-analyze verify /etc/systemd/system/usipipo-landing.service

# Test configuration reload
sudo systemctl daemon-reload
```

### Common Issues

#### "Address already in use"

```bash
# Find process using the port
sudo lsof -i :5000
# or
sudo ss -tlnp | grep 5000

# Kill the process
sudo kill <PID>

# Restart service
sudo systemctl restart usipipo-landing
```

#### "Permission denied" errors

```bash
# Verify user/group ownership
ls -la /path/to/usipipo-landing

# Fix ownership
sudo chown -R <USER>:<GROUP> /path/to/usipipo-landing

# Verify .env file permissions (should be 600)
chmod 600 /path/to/usipipo-landing/.env
```

#### Gunicorn not found

```bash
# Install gunicorn in virtual environment
source /path/to/usipipo-landing/.venv/bin/activate
pip install gunicorn

# Or with uv
uv add gunicorn
```

### Service Restarts Continuously

```bash
# Check restart count
sudo systemctl status usipipo-landing | grep "restart"

# View recent crashes
sudo journalctl -u usipipo-landing -n 100 | grep -i "error\|exception"
```

## 📊 Monitoring

### Check Resource Usage

```bash
# Memory and CPU usage
sudo systemctl status usipipo-landing

# Detailed resource usage
sudo systemd-cgtop

# Process tree
ps aux | grep gunicorn
```

### Health Check

```bash
# Test landing page
curl http://localhost:5000

# Check response time
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:5000
```

## 🔄 Updates and Maintenance

### Deploying New Version

```bash
# 1. Stop the service
sudo systemctl stop usipipo-landing

# 2. Update code
cd /path/to/usipipo-landing
git pull

# 3. Update dependencies
source .venv/bin/activate
pip install -U -r requirements.txt
# or with uv
uv sync

# 4. Start the service
sudo systemctl start usipipo-landing

# 5. Verify
sudo systemctl status usipipo-landing
curl http://localhost:5000
```

### Rollback

```bash
# 1. Stop service
sudo systemctl stop usipipo-landing

# 2. Revert code
cd /path/to/usipipo-landing
git revert HEAD

# 3. Restart service
sudo systemctl start usipipo-landing
```

## 📝 Architecture Notes

### Process Model

```
systemd
  └── gunicorn (master process)
      ├── worker 1 (sync worker)
      └── worker 2 (sync worker)
```

The service runs with 2 workers by default. Adjust based on your server capacity:

```ini
# In usipipo-landing.service
# Rule of thumb: (2 x CPU cores) + 1
ExecStart=... --workers 4
```

### Gunicorn vs Flask Development Server

This configuration uses **Gunicorn** (production WSGI server) instead of Flask's built-in server:

| Feature | Gunicorn (Production) | Flask Dev Server |
|---------|----------------------|------------------|
| Performance | ✅ Multi-worker | ❌ Single-threaded |
| Stability | ✅ Production-ready | ❌ Development only |
| Concurrency | ✅ Workers + threads | ❌ Limited |
| Memory | ✅ Efficient | ⚠️ Higher per-request |

For development/testing, you can temporarily switch to Flask's server:

```ini
# Replace ExecStart with:
ExecStart=<PATH_TO_USISIPO_LANDING>/.venv/bin/python -m src
```

### Graceful Shutdown

The service is configured for graceful shutdown:

1. Receives `SIGTERM` signal
2. Stops accepting new connections
3. Waits up to 30 seconds for in-flight requests
4. Terminates workers
5. Exits cleanly

## 📚 References

- [systemd.exec(5) - Service configuration](https://www.freedesktop.org/software/systemd/man/systemd.exec.html)
- [systemd.service(5) - Unit configuration](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Flask Deployment Options](https://flask.palletsprojects.com/en/latest/deploying/)

## 🆘 Support

For issues or questions:

1. Check logs: `sudo journalctl -u usipipo-landing -f`
2. Review documentation: https://github.com/uSipipo-Team/usipipo-landing
3. Open an issue on GitHub
