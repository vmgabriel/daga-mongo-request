"""Implementing data Api base for health"""

# Develop vmgabriel

# Libraries
from flask import Blueprint, jsonify

mod = Blueprint('api', __name__)


# Define Route Base
@mod.route('/')
def health_check():
    """Verify health check"""
    return jsonify({
        'code': 200, 'mesage': 'Daga User Service'
    }), 200


@mod.route('/aboutme')
def about_me():
    """Definition for about de rest api"""
    return jsonify({
        'code': 200, 'message': 'created for vmgabriel, dbgroldan'
    }), 200
