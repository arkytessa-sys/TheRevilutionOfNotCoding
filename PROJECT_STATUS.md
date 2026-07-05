# MainStage — Project Status

**Last Updated:** 2026-07-05  
**Current Phase:** 1 — Authentication (✓ Complete)

---

## Overview

MainStage is a small-scale, educational social media platform inspired by Facebook's feed and Telegram's chat. Built with Django 5.2, it is for coursework/portfolio use only — not for public or commercial deployment.

**Tech Stack:**
- Backend: Python 3.12, Django 5.2 (LTS)
- Frontend: HTML, CSS, JavaScript (no framework)
- Database: SQLite with WAL mode
- Images: Pillow

---

## Phase 1: Authentication — ✓ COMPLETE

### Completed
- [x] Custom `User` model extending `AbstractUser`
  - `role` field: GUEST (default) / ADMIN, indexed for Phase 2
  - `profile_picture` field with 2MB size validation
- [x] Registration form with email required + validation
- [x] Auto-login after successful registration
- [x] Login view with username/password
- [x] Logout view (POST only for security)
- [x] Project structure with accounts & core apps
- [x] SQLite configuration with WAL mode and IMMEDIATE transactions
- [x] Base template with responsive navigation
- [x] Authentication templates (register, login)
- [x] Home page placeholder with roadmap
- [x] All Django checks passing
- [x] Database migrations ready to apply

### Files Added
```
mainstage/
  settings.py           # SQLite WAL config, AUTH_USER_MODEL set
  urls.py              # Main router
  wsgi.py              # WSGI application
  __init__.py

accounts/
  models.py            # Custom User model
  forms.py             # Registration & login forms
  views.py             # register, login, logout views
  urls.py              # accounts routing (app_name='accounts')
  admin.py             # User admin interface
  apps.py
  __init__.py
  migrations/

core/
  models.py            # Placeholder for Phase 3
  views.py             # Home view (login_required)
  urls.py              # core routing (app_name='core')
  admin.py             # Placeholder
  apps.py
  __init__.py
  migrations/

templates/
  base.html            # Main layout with navigation
  accounts/
    register.html
    login.html
  core/
    home.html

static/
  (placeholder for CSS/JS in future phases)

manage.py
requirements.txt
.gitignore
```

---

## Phase 2: Admin Dashboard (Next)

### To Do
- [ ] Admin-only dashboard view
- [ ] List all users (paginated, select_related for efficiency)
- [ ] View single user details
- [ ] Promote/demote users between GUEST and ADMIN
- [ ] Delete users (with soft-delete consideration)
- [ ] Dashboard template with user table
- [ ] URL routing for admin section
- [ ] Access control decorator (`@admin_only`)

### Rationale
Admin dashboard depends on Phase 1's `role` field being indexed (✓ already done). Filters will run efficiently on the admin list view.

---

## Phase 3: Post/Feed System

### To Do
- [ ] `Post` model: text, optional Markdown, optional image/video/audio
- [ ] Image/video validation & size limits
- [ ] `Comment` model (foreign key to Post)
- [ ] `Like` model (ManyToMany or separate model)
- [ ] `Share` model
- [ ] Post create/edit/delete views
- [ ] Feed view with paginated posts (select_related + prefetch_related)
- [ ] Post templates
- [ ] Like/comment/share AJAX endpoints

---

## Phase 4: Real-time Chat

### To Do
- [ ] Install Django Channels + channels_redis
- [ ] `Message` model (user-to-user, optional media)
- [ ] WebSocket consumers for real-time chat
- [ ] Chat room/conversation routing
- [ ] Chat templates + JavaScript
- [ ] Message history (pagination)

### Notes
- Requires `ASGI` application setup
- In-memory channel layer for dev; Redis for production
- Async consumers + routing — significant architectural shift

---

## Phase 5: Account Deletion

### To Do
- [ ] Deletion view with confirmation
- [ ] Cascade delete posts, comments, likes, shares, messages
- [ ] Soft-delete option or permanent removal decision

---

## Known Issues & Blockers

### None at this time.

---

## Setup Instructions

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create migrations (User model already set as AUTH_USER_MODEL)
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional for Phase 2 onwards)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**URL Routes:**
- Admin: http://localhost:8000/admin
- Register: http://localhost:8000/accounts/register/
- Login: http://localhost:8000/accounts/login/
- Home (login required): http://localhost:8000/

---

## Next Steps (Approved by User)

1. **Phase 2:** Build admin dashboard + user management
2. Repeat approval cycle for each subsequent phase
3. Keep this file and TODO.md in sync after each session

