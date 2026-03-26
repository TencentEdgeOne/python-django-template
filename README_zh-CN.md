# Python 云函数 - Django | EdgeOne Pages

演示网站，展示如何在 EdgeOne Pages 上将 Django 应用部署为无服务器函数。

## 🚀 特性

- **Django 框架**：为有截止日期的完美主义者准备的 Web 框架
- **经过实战检验**：成熟的框架，驱动着数百万网站
- **开箱即用**：内置 ORM、认证、管理后台、模板引擎等
- **安全第一**：默认提供 CSRF、XSS、SQL 注入保护
- **URL 路由**：Django 强大的 URL 调度器

## 🛠️ 技术栈

### 前端
- **Next.js 15** - React 全栈框架
- **React 19** - 用户界面库
- **TypeScript** - 类型安全的 JavaScript
- **Tailwind CSS 4** - 实用优先的 CSS 框架

### 后端
- **Django** - Python Web 框架
- **Cloud Functions** - EdgeOne Pages 无服务器函数

## 📁 项目结构

```
python-django-template/
├── src/                    # Next.js 前端
├── cloud-functions/        # Python 云函数
│   ├── api/
│   │   └── [[default]].py # Django 应用
│   └── requirements.txt   # Python 依赖
├── public/                # 静态资源
└── package.json          # 项目配置
```

## 🚀 快速开始

### 环境要求

- Node.js 18+ 
- Python 3.9+
- EdgeOne CLI

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
edgeone pages dev
```

访问 [http://localhost:8088](http://localhost:8088) 查看应用。

## 🎯 API 端点

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/ | 根端点 |
| GET | /api/health | 健康检查 |
| GET | /api/info | 函数信息 |
| GET | /api/time | 当前服务器时间 |
| GET/POST | /api/echo | 回显请求信息 |
| POST | /api/json | 处理 JSON 请求体 |
| GET | /api/users/{user_id} | 根据 ID 获取用户 |
| POST | /api/users | 创建新用户 |
| GET | /api/search | 带查询参数搜索 |

## 📚 文档入口

- **Django 文档**：[https://docs.djangoproject.com](https://docs.djangoproject.com)
- **EdgeOne Pages 文档**：[https://pages.edgeone.ai/document/cloud-functions/python](https://pages.edgeone.ai/document/cloud-functions/python)

## 部署

[![Deploy with EdgeOne Pages](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://console.cloud.tencent.com/edgeone/pages/new?from=github&template=python-django-template)

## 📄 许可证

本项目采用 MIT 许可证。
