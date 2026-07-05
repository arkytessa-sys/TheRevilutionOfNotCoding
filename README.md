# MainStage

A small-scale, educational social media platform inspired by Facebook's feed and Telegram's chat. Built with Django 5.2 for coursework/portfolio use only — **not for public or commercial deployment**.

---

## Quick Start

### 1. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit http://localhost:8000 in your browser.

---

## Tech Stack

- **Backend:** Python 3.12, Django 5.2 (LTS)
- **Frontend:** HTML, CSS, JavaScript (no framework)
- **Database:** SQLite (WAL mode for concurrency)
- **Images:** Pillow

---

## Project Structure

```
mainstage/              # Django project config
  settings.py          # SQLite WAL, AUTH_USER_MODEL
  urls.py              # Main router
  wsgi.py              # WSGI entry point

accounts/              # Authentication & user management
  models.py            # Custom User model (role, profile_picture)
  forms.py             # Registration & login forms
  views.py             # Auth views
  urls.py              # Auth routing (namespace: accounts)
  admin.py             # Admin interface

core/                  # Home page (Phase 1) → Feed (Phase 3)
  models.py            # Placeholder for Post, Comment, Like, Share
  views.py             # Home view
  urls.py              # Core routing (namespace: core)
  admin.py             # Placeholder

templates/             # Project-level templates
  base.html            # Main layout + navigation
  accounts/
    register.html
    login.html
  core/
    home.html

manage.py              # Django CLI
requirements.txt       # Python dependencies
```

---

## Features by Phase

### ✅ Phase 1: Authentication
- Custom User model with role-based access (GUEST/ADMIN)
- Registration (email required) with auto-login
- Login/logout
- Profile picture uploads (2MB limit)

### 🚧 Phase 2: Admin Dashboard
- User list/view/manage
- Promote/demote users
- Delete users

### ⏳ Phase 3: Post/Feed System
- Create posts (text, images, video, audio)
- Comments, likes, shares
- Main feed with pagination

### ⏳ Phase 4: Real-time Chat
- Django Channels + WebSockets
- Direct messages (Telegram-style)
- Media sharing

### ⏳ Phase 5: Account Deletion
- User account deletion with cascading data removal

---

## URL Routes

| Route | Purpose |
|-------|---------|
| `/` | Home (login required) |
| `/accounts/register/` | User registration |
| `/accounts/login/` | User login |
| `/accounts/logout/` | User logout |
| `/admin/` | Django admin |

---

## Database Notes

**SQLite Configuration:**
- Uses **WAL mode** to prevent "database is locked" errors during concurrent writes
- **IMMEDIATE transaction mode** grabs write locks at the start of a transaction
- Added to `.gitignore`: `db.sqlite3`, `db.sqlite3-wal`, `db.sqlite3-shm`

---

## Development Workflow

1. **Before making changes:** Read `PROJECT_STATUS.md` and `TODO.md`
2. **Run checks:** `python manage.py check`
3. **Create migrations:** `python manage.py makemigrations`
4. **Apply migrations:** `python manage.py migrate`
5. **Update docs:** `PROJECT_STATUS.md`, `CHANGELOG.md`, `TODO.md` after each phase

---

## Documentation

- **`PROJECT_STATUS.md`** — Current phase, completed work, next steps
- **`CHANGELOG.md`** — All changes by phase
- **`TODO.md`** — Detailed to-do list for each phase
- **`MODULE_REFERENCE.md`** — Installed packages and their purpose
- **`AI_AGENT_PROMPT.md`** — Full project spec & workflow rules

---

## Key Design Decisions

1. **Custom User Model Early** — Set `AUTH_USER_MODEL` before first migration to avoid painful swaps later
2. **SQLite WAL Mode** — Prevents database lock errors in concurrent scenarios
3. **Image Validation at Model Layer** — Prevents storage bloat before upload
4. **Role-Based Access** — `role` field indexed for efficient admin filtering (Phase 2)
5. **Project-Level Templates** — Shared `base.html` for consistent navigation

---

## Deployment Notes

**This is an educational project.** Before deploying to production:

- ⚠️ Set `DEBUG = False` in settings
- ⚠️ Use a secure `SECRET_KEY` (not the dev fallback)
- ⚠️ Switch from SQLite to PostgreSQL for concurrent users
- ⚠️ Serve static/media files via a CDN or web server (not Django)
- ⚠️ Configure allowed hosts and CORS
- ⚠️ Set up HTTPS/SSL
- ⚠️ Use environment variables for sensitive config
- ⚠️ Add logging and monitoring
- ⚠️ Implement rate limiting and security headers

---

## Contributing

This is a solo educational project. For coursework/portfolio use only.

---

## License

Personal project — not licensed for redistribution or commercial use.

