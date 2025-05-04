from flask import Flask, render_template_string, request, abort

app = Flask(__name__)

# Protección básica contra ataques comunes
@app.before_request
def block_bad_requests():
    user_agent = request.headers.get('User-Agent', '').lower()
    if 'sqlmap' in user_agent or 'curl' in user_agent:
        abort(403)

# Página web protegida (solo HTML renderizado, sin datos sensibles)
html_content = ""
( self : <!DOCTYPE html>)
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Web Protegida</title>
    <script>
        // Desactivar clic derecho
        document.addEventListener('contextmenu', event => event.preventDefault());

        // Bloquear teclas comunes para inspección
        document.onkeydown = function(e) {
            if (e.keyCode == 123 || // F12
                (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || // Ctrl+Shift+I / J
                (e.ctrlKey && e.keyCode == 85)) { // Ctrl+U
                return false;
            }
        };
    </script>
</head>
<body>
    <h1>Bienvenido a la página protegida</h1>
    <p>Esta página intenta protegerse contra la inspección del navegador.</p>
</body>
</html>
""

@app.route('/')
def index():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=False)
