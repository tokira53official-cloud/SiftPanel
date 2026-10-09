import os
import secrets
from datetime import datetime, timezone

from flask import Flask, request, redirect, url_for, render_template_string, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SIFTPANEL_SECRET_KEY") or secrets.token_hex(32)

ADMIN_USER = os.environ.get("SIFTPANEL_ADMIN_USER", "admin")
ADMIN_PASSWORD_HASH = os.environ.get("SIFTPANEL_ADMIN_PASSWORD_HASH")

if not ADMIN_PASSWORD_HASH:
    raise RuntimeError(
        "Set SIFTPANEL_ADMIN_PASSWORD_HASH before starting SiftPanel. "
        "Do not use a public default password."
    )

STYLE = """
*{box-sizing:border-box}
body{margin:0;background:#090b14;color:#f5f6ff;font-family:Arial,sans-serif}
.wrap{max-width:1000px;margin:50px auto;padding:20px}
.card{background:#141827;border:1px solid #303750;border-radius:18px;padding:25px;margin-bottom:20px}
h1{color:#a78bfa}p{color:#aab1c9}
input,button{width:100%;padding:13px;margin:8px 0;border-radius:9px;border:1px solid #414967}
input{background:#0c1020;color:white}
button{background:#8b5cf6;color:white;border:0;font-weight:bold}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px}
.small{font-size:13px;color:#aab1c9}
a{color:#c4b5fd}
"""

LOGIN_PAGE = """
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SiftPanel Login</title><style>""" + STYLE + """</style></head>
<body><div class="wrap"><div class="card">
<h1>SiftPanel</h1><p>Your Ultimate IT & Hosting Partner</p>
<h2>Welcome back</h2>
{% if error %}<p style="color:#f87171">{{ error }}</p>{% endif %}
<form method="post">
<input name="username" placeholder="Username" required autocomplete="username">
<input name="password" type="password" placeholder="Password" required autocomplete="current-password">
<button type="submit">Sign In</button>
</form><p class="small">Secure server management • SiftNodes</p>
</div></div></body></html>
"""

DASHBOARD = """
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SiftPanel Dashboard</title><style>""" + STYLE + """</style></head>
<body><div class="wrap">
<div class="card"><h1>SiftPanel</h1>
<p>Your Ultimate IT & Hosting Partner</p>
<p>Welcome, {{ username }}!</p>
<form action="{{ url_for('logout') }}" method="post">
<button type="submit">Log Out</button></form></div>
<div class="grid">
<div class="card"><h2>🖥️ Servers</h2><p>Server management will be connected in a later step.</p></div>
<div class="card"><h2>📊 Resources</h2><p>CPU and RAM monitoring will be added with the node agent.</p></div>
<div class="card"><h2>⚙️ Settings</h2><p>Panel configuration will be added in a later step.</p></div>
</div>
<p class="small">SiftNodes · SiftPanel</p>
</div></body></html>
"""

@app.after_request
def security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("dashboard"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if (
            secrets.compare_digest(username, ADMIN_USER)
            and check_password_hash(ADMIN_PASSWORD_HASH, password)
        ):
            session.clear()
            session["logged_in"] = True
            session["username"] = username
            session.permanent = True
            return redirect(url_for("dashboard"))

        error = "Incorrect username or password."

    return render_template_string(LOGIN_PAGE, error=error)

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template_string(
        DASHBOARD, username=session.get("username", "admin")
    )

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.get("/health")
def health():
    return {"status": "ok", "panel": "SiftPanel"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
