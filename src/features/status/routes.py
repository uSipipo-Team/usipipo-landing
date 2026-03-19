"""Status routes."""

from flask import Blueprint, render_template

status_bp = Blueprint("status", __name__)


@status_bp.route("/status")
def index():
    """Página de estado del servicio."""
    return render_template("status/index.html")
