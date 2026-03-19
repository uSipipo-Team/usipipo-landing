"""Home routes."""

from flask import Blueprint, request, render_template

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    """Página de inicio."""
    return render_template("home/index.html")
