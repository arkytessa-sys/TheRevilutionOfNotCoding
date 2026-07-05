# MainStage — To-Do List

---

## Phase 1: Authentication — ✅ COMPLETE

- [x] Custom User model with role + profile_picture
- [x] Registration form (email required)
- [x] Auto-login after registration
- [x] Login view
- [x] Logout view
- [x] Base template + navigation
- [x] Auth templates (register, login)
- [x] Home placeholder
- [x] SQLite WAL configuration
- [x] Project scaffolding

---

## Phase 2: Admin Dashboard — 🚧 IN QUEUE

- [ ] Create `dashboard/` app OR extend `accounts/` with admin views
- [ ] `@admin_only` decorator for access control
- [ ] Admin dashboard view
  - [ ] List all users (paginated, 20 per page)
  - [ ] Search by username/email
  - [ ] Filter by role
- [ ] User detail view
  - [ ] Display profile picture, email, role, date joined
  - [ ] Promote to ADMIN button
  - [ ] Demote to GUEST button
  - [ ] Delete user button
- [ ] Delete user confirmation
- [ ] Admin templates
  - [ ] Dashboard/list view
  - [ ] User detail view
- [ ] URL routing for admin section
- [ ] Tests (optional for Phase 2; required by Phase 3)

**Estimated Effort:** 3–4 hours

---

## Phase 3: Post/Feed System — ⏳ UPCOMING

- [ ] Post model
  - [ ] text (TextField)
  - [ ] markdown support
  - [ ] image (optional, PNG/JPEG, size validation)
  - [ ] video (optional, MP4, size validation)
  - [ ] audio (optional, MP3, size validation)
  - [ ] author (ForeignKey to User)
  - [ ] created_at, updated_at (timestamps with db_index=True)
- [ ] Comment model
  - [ ] text
  - [ ] author (ForeignKey to User)
  - [ ] post (ForeignKey to Post)
  - [ ] created_at
- [ ] Like model (or ManyToMany)
  - [ ] user (ForeignKey to User)
  - [ ] post (ForeignKey to Post)
  - [ ] unique_together constraint
- [ ] Share model
  - [ ] user, post, created_at
- [ ] Post create view
- [ ] Post edit view (author only)
- [ ] Post delete view (author + admin)
- [ ] Feed view
  - [ ] Paginated (20 posts per page)
  - [ ] select_related('author') for efficiency
  - [ ] prefetch_related('comments', 'likes') for efficiency
  - [ ] Order by created_at DESC
- [ ] Comment create/delete views
- [ ] Like toggle (AJAX endpoint)
- [ ] Share endpoint
- [ ] Post templates
  - [ ] Feed template
  - [ ] Post card component
  - [ ] Comment list
- [ ] Front-end interactions (like, comment, share buttons)
- [ ] Tests

**Estimated Effort:** 8–10 hours

---

## Phase 4: Real-time Chat — ⏳ UPCOMING

- [ ] Install Django Channels + channels_redis
- [ ] ASGI configuration (`mainstage/asgi.py`)
- [ ] Routing for WebSocket consumers
- [ ] Conversation model
  - [ ] participants (ManyToMany to User)
  - [ ] created_at, updated_at
- [ ] Message model
  - [ ] sender (ForeignKey to User)
  - [ ] conversation (ForeignKey to Conversation)
  - [ ] text
  - [ ] media (optional: image, video, audio with size validation)
  - [ ] created_at
- [ ] WebSocket consumer for chat
  - [ ] Connect/disconnect handlers
  - [ ] Message receive + broadcast
  - [ ] Online/offline status
- [ ] Chat list view (conversations)
- [ ] Chat detail view (message history, paginated)
- [ ] Send message endpoint
- [ ] Chat templates + JS
  - [ ] Conversation list
  - [ ] Chat room template
  - [ ] Message input form
  - [ ] Real-time message appending (WebSocket JS client)
- [ ] Tests

**Estimated Effort:** 10–12 hours

**Note:** This phase requires architectural changes (async consumers, channel layer). Requires separate approval.

---

## Phase 5: Account Deletion — ⏳ UPCOMING

- [ ] Delete account view (confirmation page)
- [ ] Cascade deletion handlers
  - [ ] Delete all user's posts
  - [ ] Delete all comments by user
  - [ ] Delete all likes by user
  - [ ] Delete all shares by user
  - [ ] Delete all messages by/to user
  - [ ] Delete all conversations where user is participant
- [ ] Soft-delete vs. hard-delete decision
- [ ] Template for deletion confirmation
- [ ] Tests

**Estimated Effort:** 2–3 hours

---

## Backlog & Polish

- [ ] Add tests for all phases
- [ ] Email verification on registration (optional)
- [ ] Password reset flow (optional)
- [ ] User profile editing (first/last name, bio, profile picture upload)
- [ ] Search users
- [ ] Follow/follower system
- [ ] Notifications (optional, Phase 4+)
- [ ] Dark mode (optional, CSS)
- [ ] Mobile responsiveness polish
- [ ] Rate limiting on API endpoints
- [ ] Logging & monitoring
- [ ] Production deployment guide

---

## Notes

- Each phase requires user approval before starting
- Keep `CHANGELOG.md` and `PROJECT_STATUS.md` in sync after each session
- If stopping mid-session, record stopping point, completed work, next task, and files mid-edit in a session summary

