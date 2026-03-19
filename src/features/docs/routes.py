"""Docs routes."""

from flask import Blueprint, render_template

docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/docs")
def index():
    """Página de documentación."""
    return render_template("docs/index.html")
