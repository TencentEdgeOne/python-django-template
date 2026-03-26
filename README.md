# Python Cloud Functions - Django | EdgeOne Pages

A demonstration website showcasing how to deploy Django applications as serverless functions on EdgeOne Pages.

## 🚀 Features

- **Django Framework**: The web framework for perfectionists with deadlines
- **Battle-Tested**: Mature framework powering millions of websites
- **Batteries Included**: ORM, auth, admin, templates, and more built-in
- **Security First**: CSRF, XSS, SQL injection protection by default
- **URL Routing**: Django's powerful URL dispatcher

## 🛠️ Tech Stack

### Frontend
- **Next.js 15** - React full-stack framework
- **React 19** - User interface library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS 4** - Utility-first CSS framework

### Backend
- **Django** - Python web framework
- **Cloud Functions** - EdgeOne Pages serverless functions

## 📁 Project Structure

```
python-django-template/
├── src/                    # Next.js frontend
├── cloud-functions/        # Python cloud functions
│   ├── api/
│   │   └── [[default]].py # Django application
│   └── requirements.txt   # Python dependencies
├── public/                # Static assets
└── package.json          # Project configuration
```

## 🚀 Quick Start

### Requirements

- Node.js 18+ 
- Python 3.9+
- EdgeOne CLI

### Install Dependencies

```bash
npm install
```

### Development Mode

```bash
edgeone pages dev
```

Visit [http://localhost:8088](http://localhost:8088) to view the application.

## 🎯 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/ | Root endpoint |
| GET | /api/health | Health check |
| GET | /api/info | Function information |
| GET | /api/time | Current server time |
| GET/POST | /api/echo | Echo request info |
| POST | /api/json | Handle JSON body |
| GET | /api/users/{user_id} | Get user by ID |
| POST | /api/users | Create new user |
| GET | /api/search | Search with query params |

## 📚 Documentation

- **Django Documentation**: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- **EdgeOne Pages Docs**: [https://pages.edgeone.ai/document/cloud-functions/python](https://pages.edgeone.ai/document/cloud-functions/python)

## Deploy

[![Deploy with EdgeOne Pages](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://edgeone.ai/pages/new?from=github&template=python-django-template)

## 📄 License

This project is licensed under the MIT License.
