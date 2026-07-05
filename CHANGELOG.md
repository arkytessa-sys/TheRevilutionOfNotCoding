# MainStage — Changelog

All notable changes to this project will be documented in this file.

---

## [Phase 2] — 2026-07-05

### Added

**Admin Dashboard System**
- `@admin_only` decorator (`accounts/decorators.py`) for access control
  - Restricts views to users with `role == 'admin'`
  - Returns 403 Forbidden for non-admin users
  - Works in conjunction with `@login_required`

- Admin dashboard view (`accounts/views.py`)
  - Lists all users paginated (20 per page)
  - Search by username, email, first/last name
  - Filter by role (GUEST/ADMIN)
  - Displays user table with role badges and join date

- User detail view (`accounts/views.py`)
  - Shows individual user profile
  - Displays profile picture, email, full name, role, join date
  - Prevents admin from editing self (safety check)

- Promote user action
  - Upgrades GUEST to ADMIN
  - POST-only for security
  - Prevents self-promotion

- Demote user action
  - Downgrades ADMIN to GUEST
  - POST-only for security
  - Prevents self-demotion

- Delete user action
  - Two-step deletion (confirmation page + POST)
  - Prevents self-deletion
  - Permanently removes user from database

**URL Routing Updates**
- New admin routes in `accounts/urls.py`
  - `/dashboard/` — User list view (admin only)
  - `/user/<id>/` — User detail view (admin only)
  - `/user/<id>/promote/` — Promote user (admin only, POST)
  - `/user/<id>/demote/` — Demote user (admin only, POST)
  - `/user/<id>/delete/` — Delete user (admin only, GET/POST)

**Templates**
- `templates/accounts/dashboard.html`
  - Admin dashboard with stats, search, filters
  - User table with action links
  - Pagination with query string preservation
  - Responsive grid layout

- `templates/accounts/user_detail.html`
  - User profile card with avatar
  - Detailed user information
  - Action buttons (promote/demote/delete)
  - Self-edit prevention warning

- `templates/accounts/delete_user.html`
  - Deletion confirmation page
  - Warning message with user to delete
  - Cancel/confirm actions

**Base Template Enhancement**
- Updated `templates/base.html`
  - Dashboard link in navigation (visible to admins only)
  - Better message styling (success, error, info, warning)
  - Improved navigation layout with conditional admin link
  - Sticky header for better UX

**Views & Forms Updates**
- Enhanced `accounts/views.py`
  - All views now include success/info messages for UX feedback
  - Better error handling for admin operations
  - Database queries optimized for pagination

### Technical Decisions

1. **@admin_only Decorator**: Reusable access control pattern
   - Can be applied to any view requiring admin role
   - Combines with `@login_required` for complete protection
   - Returns 403 instead of redirecting (clearer intent)

2. **Two-Step Deletion**: Prevents accidental user deletion
   - GET shows confirmation page with warning
   - POST performs actual deletion
   - Admin cannot delete self (safety check)

3. **Pagination**: 20 users per page
   - Prevents loading entire database into memory
   - Scales well as user count grows
   - Query strings preserved for search/filter persistence

4. **Search & Filter**: Multiple search dimensions
   - By username, email, first/last name (OR logic)
   - By role (AND logic after search)
   - Both optional; can be combined

5. **Role Badges**: Visual role indicators
   - Admin: Blue badge (#e3f2fd)
   - Guest: Gray badge (#f5f5f5)
   - Consistent with Material Design principles

### Files Modified/Added

```
accounts/
  decorators.py          # NEW: @admin_only decorator
  views.py               # UPDATED: Added 5 new admin views
  urls.py                # UPDATED: Added 5 new admin routes

templates/accounts/
  dashboard.html         # NEW: Admin dashboard
  user_detail.html       # NEW: User detail page
  delete_user.html       # NEW: Delete confirmation

templates/
  base.html              # UPDATED: Added dashboard link, improved styling
```

### Validation

- ✅ `python manage.py check` passes
- ✅ All views protected by `@admin_only`
- ✅ Pagination works with search/filter
- ✅ Self-modification prevented (safety checks)
- ✅ Database queries optimized (no N+1 problems)
- ✅ All forms POST-only for write operations

### Known Issues / Blockers

None at this time.

---

## [Phase 1] — 2026-07-05

### Added

**Project Scaffolding & Settings**
- Django 5.2 project with LTS support
- SQLite database with WAL mode + IMMEDIATE transactions for concurrent access
- `.gitignore` for Python/Django standards
- `requirements.txt` with core dependencies (Django 5.2, Pillow, python-decouple)

**Authentication System**
- Custom `User` model with role field (GUEST/ADMIN, indexed)
- Profile picture field with 2MB size validation
- Registration form with email validation + uniqueness checks
- Auto-login after registration
- Login/logout views with message feedback
- Django admin integration with role filtering

**Frontend & Templates**
- Base template with responsive navigation
- Auth templates (register, login)
- Home page placeholder with project roadmap

**Project Documentation**
- README, PROJECT_STATUS, CHANGELOG, TODO, MODULE_REFERENCE

---

## [Phase 3] — Pending

- Post/feed system with comments, likes, shares

---

## [Phase 4] — Pending

- Real-time chat via Django Channels + WebSockets

---

## [Phase 5] — Pending

- Account deletion with cascading data removal
