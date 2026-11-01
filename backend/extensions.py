from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
 
# As extensões são criadas aqui, sem app, e ligadas ao app em create_app()
# usando extensao.init_app(app). Isso evita importações circulares.
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
 
# Para onde redirecionar quando alguém tenta acessar uma página protegida
login_manager.login_view = "auth.login"
login_manager.login_message = "Faça login para acessar esta página."
login_manager.login_message_category = "warning"