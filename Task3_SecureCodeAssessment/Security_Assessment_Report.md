# Security Assessment Report - vulnerable_app.py

## 1. SQL Injection (Login Function)
**Location:** `/login` route
**Issue:** User input (`username`, `password`) is directly concatenated into an SQL query without sanitization, allowing attackers to manipulate the query (e.g., `' OR '1'='1`).
**Risk:** High — Attackers can bypass authentication or extract/modify database data.
**Fix:** Use parameterized queries.
```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor = conn.execute(query, (username, password))
```

## 2. Cross-Site Scripting (XSS) (Search Function)
**Location:** `/search` route
**Issue:** User input (`q`) is directly reflected into the HTML response without sanitization or escaping.
**Risk:** Medium-High — Attackers can inject malicious scripts to steal cookies/sessions.
**Fix:** Escape user input before rendering, or use a templating engine with auto-escaping (e.g., Jinja2 `render_template`).

## 3. Path Traversal (Download Function)
**Location:** `/download` route
**Issue:** The `filename` parameter is used directly in a file path without validation, allowing access to files outside the intended directory (e.g., `../../etc/passwd`).
**Risk:** High — Can expose sensitive server files.
**Fix:** Validate/sanitize filenames and restrict access to a specific safe directory.
```python
import os
safe_path = os.path.join("files", os.path.basename(filename))
```

## 4. Command Injection (Run Function)
**Location:** `/run` route
**Issue:** User input (`cmd`) is passed directly to `os.popen()`, allowing arbitrary command execution on the server.
**Risk:** Critical — Full server compromise possible.
**Fix:** Never execute user-supplied input as system commands. Remove this functionality entirely, or use a strict allow-list of permitted commands with no direct user input.

## 5. Hardcoded Credentials
**Location:** Top of file (`DB_PASSWORD`, `SECRET_KEY`)
**Issue:** Sensitive credentials are hardcoded in source code.
**Risk:** Medium — Credentials can be exposed if code is leaked or pushed to public repos.
**Fix:** Store secrets in environment variables or a secure secrets manager.
```python
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
```

## 6. Debug Mode Enabled
**Location:** `app.debug = True`
**Issue:** Debug mode exposes detailed error messages and an interactive debugger to end users.
**Risk:** Medium — Can leak internal application details to attackers.
**Fix:** Disable debug mode in production.
```python
app.debug = False
```

## Summary Table

| Vulnerability | Severity | OWASP Category |
|---|---|---|
| SQL Injection | High | A03: Injection |
| XSS | Medium-High | A03: Injection |
| Path Traversal | High | A01: Broken Access Control |
| Command Injection | Critical | A03: Injection |
| Hardcoded Credentials | Medium | A02: Cryptographic Failures |
| Debug Mode Enabled | Medium | A05: Security Misconfiguration |

## Recommendations
- Always use parameterized queries for database operations.
- Sanitize and escape all user input before rendering or executing.
- Never expose file system operations directly to user input.
- Store secrets using environment variables, not hardcoded values.
- Disable debug mode before deployment.
- Adopt a secure coding checklist (e.g., OWASP Top 10) during development.
