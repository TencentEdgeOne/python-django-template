"""
Python Cloud Function - Django Framework
A serverless function using the Django web framework.
"""
import os
import sys
import json
import time
import datetime

# Configure Django settings before importing Django modules
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Minimal Django settings
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY='your-secret-key-here-change-in-production',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        MIDDLEWARE=[],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
        ],
    )

import django
django.setup()

from django.http import JsonResponse, HttpResponse
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# ============ View Functions ============

def index(request):
    """Root endpoint."""
    return JsonResponse({
        "message": "Hello from Django Cloud Function!",
        "framework": "Django",
        "timestamp": time.time()
    })


def health(request):
    """Health check endpoint."""
    return JsonResponse({
        "status": "healthy",
        "timestamp": time.time(),
        "type": "django_function"
    })


def info(request):
    """Function information endpoint."""
    return JsonResponse({
        "name": "Django Cloud Function",
        "framework": "Django",
        "description": "A serverless function using the Django web framework",
        "features": [
            "Django ORM (when configured)",
            "URL routing",
            "Middleware support",
            "Template engine",
            "Admin interface (when configured)",
            "Battle-tested and mature"
        ]
    })


def get_time(request):
    """Return current server time."""
    now = datetime.datetime.now()
    return JsonResponse({
        "timestamp": time.time(),
        "iso": now.isoformat(),
        "formatted": now.strftime("%Y-%m-%d %H:%M:%S"),
    })


@csrf_exempt
@require_http_methods(["GET", "POST"])
def echo(request):
    """Echo request information."""
    body = request.body.decode('utf-8') if request.body else None
    return JsonResponse({
        "method": request.method,
        "query": dict(request.GET),
        "headers_count": len(dict(request.headers)),
        "body": body[:500] if body else None,
        "timestamp": time.time()
    })


@csrf_exempt
@require_http_methods(["POST"])
def handle_json(request):
    """Handle JSON request body."""
    try:
        data = json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    
    return JsonResponse({
        "message": "JSON received and parsed",
        "received": data,
        "keys": list(data.keys()) if isinstance(data, dict) else [],
        "size": len(request.body) if request.body else 0
    })


def get_user(request, user_id):
    """Get user by ID."""
    try:
        uid = int(user_id)
        if uid < 0:
            raise ValueError("Invalid user ID")
    except (ValueError, TypeError):
        return JsonResponse({"error": "Invalid user ID"}, status=400)
    
    return JsonResponse({
        "user_id": uid,
        "username": f"user_{uid}",
        "email": f"user{uid}@example.com",
        "source": "django_function"
    })


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    """Create a new user."""
    try:
        data = json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    
    if 'username' not in data:
        return JsonResponse({"error": "Username is required"}, status=400)
    
    return JsonResponse({
        "message": "User created",
        "user": {
            "id": 12345,
            "username": data['username'],
            "email": data.get('email', ''),
        }
    }, status=201)


def search(request):
    """Search functionality with query parameters."""
    q = request.GET.get('q', '')
    limit = int(request.GET.get('limit', 10))
    offset = int(request.GET.get('offset', 0))
    
    if not q:
        return JsonResponse({"error": "Query parameter 'q' is required"}, status=400)
    
    results = [
        {"id": i, "name": f"Result {i}", "score": round(0.95 - i * 0.08, 2)}
        for i in range(offset, offset + min(limit, 10))
    ]
    
    return JsonResponse({
        "query": q,
        "limit": limit,
        "offset": offset,
        "count": len(results),
        "results": results
    })


# ============ URL Patterns ============

urlpatterns = [
    path('', index, name='index'),
    path('health', health, name='health'),
    path('info', info, name='info'),
    path('time', get_time, name='time'),
    path('echo', echo, name='echo'),
    path('json', handle_json, name='json'),
    path('users', create_user, name='create_user'),
    re_path(r'^users/(?P<user_id>\d+)$', get_user, name='get_user'),
    path('search', search, name='search'),
]


# ============ WSGI Application ============

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
