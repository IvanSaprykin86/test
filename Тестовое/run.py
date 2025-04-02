from litestar_granian import GranianPlugin

from app.main import app

app.plugins.append(GranianPlugin(host="0.0.0.0", port=8000))
