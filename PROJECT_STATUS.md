# MainStage — Project Status

**Last Updated:** 2026-07-05  
**Current Phase:** 2 — Admin Dashboard (✓ Complete)  
**Previous Phases:** 1 — Authentication (✓ Complete)

---

## Overview

MainStage is a small-scale, educational social media platform inspired by Facebook's feed and Telegram's chat. Built with Django 5.2, it is for coursework/portfolio use only — not for public or commercial deployment.

**Tech Stack:**
- Backend: Python 3.12, Django 5.2 (LTS)
- Frontend: HTML, CSS, JavaScript (no framework)
- Database: SQLite with WAL mode
- Images: Pillow

---

## Phase 2: Admin Dashboard — ✓ COMPLETE

### Completed
- [x] `@admin_only` decorator for access control
- [x] Admin dashboard view
  - Lists all users (paginated, 20 per page)
  - Search by username, email, first/last name
  - Filter by role (GUEST/ADMIN)
  - Responsive user table with role badges
- [x] User detail view
  - Displays profile picture, email, full name, role, join date
  - Shows admin action buttons
  - Self-edit prevention
- [x] Promote user (GUEST → ADMIN)
  - POST-only for security
  - Self-promotion prevented
- [x] Demote user (ADMIN → GUEST)
  - POST-only for security
  - Self-demotion prevented
- [x] Delete user (two-step confirmation)
  - GET: Shows confirmation page with warning
  - POST: Permanently deletes user
  - Self-deletion prevented
- [x] Updated URL routing
- [x] Dashboard template with search/filter
- [x] User detail template
- [x] Delete confirmation template
- [x] Base template with admin dashboard link
- [x] All user-facing messages (success/error/info)
- [x] Database optimization (no N+1 queries)

### Files Added/Modified
```
accounts/
  decorators.py          # NEW: @admin_only
  views.py               # UPDATED: 5 new admin views
  urls.py                # UPDATED: 5 new admin routes

templates/accounts/
  dashboard.html         # NEW
  user_detail.html       # NEW
  delete_user.html       # NEW

templates/
  base.html              # UPDATED: Dashboard link + styling
```

### Key Features
- ✅ Only admins can access `/accounts/dashboard/`
- ✅ Search works across multiple fields
- ✅ Role-based filtering
- ✅ Pagination preserves search/filter params
- ✅ Promote/demote/delete are one-click (with confirmations)
- ✅ Admins cannot modify themselves
- ✅ Visual role badges (Admin: blue, Guest: gray)

---

## Phase 1: Authentication — ✓ COMPLETE

### Completed
- [x] Custom User model with role field (indexed)
- [x] Registration (email required, auto-login)
- [x] Login/logout
- [x] Profile picture uploads (2MB validation)
- [x] Base templates + navigation
- [x] Home page placeholder
- [x] SQLite WAL configuration

---

## Phase 3: Post/Feed System (Next)

### To Do
- [ ] `Post` model: text, optional Markdown, optional media (image/video/audio)
- [ ] Image/video/audio size validation
- [ ] `Comment` model (FK to Post, text, author, timestamp)
- [ ] `Like` model (ManyToMany or separate, unique together)
- [ ] `Share` model (user, post, created_at)
- [ ] Post create/edit/delete views
- [ ] Feed view (paginated, select_related + prefetch_related)
- [ ] Post templates
- [ ] Like/comment/share endpoints (AJAX)
- [ ] Post detail view with all interactions

### Rationale
Post system depends on Phase 1 & 2 being complete. Feed will be the main page after Phase 3 replaces the home placeholder.

---

## Phase 4: Real-time Chat

### To Do
- [ ] Install Django Channels + channels_redis
- [ ] ASGI configuration (`mainstage/asgi.py`)
- [ ] Routing for WebSocket consumers
- [ ] Conversation model (participants, created_at, updated_at)
- [ ] Message model (user, conversation, text, media, created_at)
- [ ] WebSocket consumer for chat
- [ ] Chat list view (user's conversations)
- [ ] Chat detail view (message history, paginated)
- [ ] Message sending endpoint
- [ ] Chat templates + JavaScript (real-time message append)

### Notes
- Requires `ASGI` application setup
- In-memory channel layer for dev; Redis for production
- Significant architectural shift — requires separate approval

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

## Setup & Testing

### Initial Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Testing Phase 2
1. Create a regular user (GUEST) via registration
2. Log in as superuser (created via `createsuperuser`)
3. Navigate to `/accounts/dashboard/`
4. Test:
   - Search by username/email
   - Filter by role
   - View user details
   - Promote user to ADMIN
   - Demote user to GUEST
   - Delete user (with confirmation)
5. Verify non-admins cannot access `/accounts/dashboard/`

### URL Routes
- Home: http://localhost:8000/ (login required)
- Register: http://localhost:8000/accounts/register/
- Login: http://localhost:8000/accounts/login/
- Dashboard: http://localhost:8000/accounts/dashboard/ (admin only)
- User Detail: http://localhost:8000/accounts/user/<id>/ (admin only)
- Admin: http://localhost:8000/admin/

---

## Next Steps (Approved by User)

1. **Phase 3:** Build Post/Feed system with comments, likes, shares
2. Repeat approval cycle for each subsequent phase
3. Keep this file and TODO.md in sync after each session
