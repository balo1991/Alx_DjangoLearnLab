# Security Enhancements in LibraryProject

This project includes several security improvements following Django best practices.

---

## 1. Secure Django Settings
- `DEBUG = False` for production
- `ALLOWED_HOSTS` configured
- Cookie protections:
  - `CSRF_COOKIE_SECURE = True`
  - `SESSION_COOKIE_SECURE = True`
- Browser security headers:
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `X_FRAME_OPTIONS = "DENY"`
- Optional HSTS settings for HTTPS deployments.

---

## 2. Content Security Policy (CSP)
Implemented via custom middleware:  
`LibraryProject/middleware.py`

This helps mitigate XSS attacks by restricting external scripts and styles.

---

## 3. CSRF Protection
All POST forms include `{% csrf_token %}` to defend against CSRF attacks.

---

## 4. Secure Data Handling
- All user input forms validated with Django Forms (`BookForm`)
- ORM used exclusively (no raw SQL)
- Search queries safely parameterized
- No unsafe `|safe` usage in templates

---

## 5. Permission-Based Access Control
Views protected with:
- `@login_required`
- `@permission_required('bookshelf.can_*', raise_exception=True)`

This enforces secure role-based access control.

---
