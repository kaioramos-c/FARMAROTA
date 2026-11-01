import os
from pathlib import Path
 
from dotenv import load_dotenv
 
BASE_DIR = Path(__file__).resolve().parent


def load_dotenv(path):
    """Load KEY=VALUE entries from a .env file without external dependencies."""
    if not path.is_file():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        if key:
            os.environ.setdefault(key, value)


# Carrega as variáveis do arquivo .env (se existir)
load_dotenv(BASE_DIR / ".env")
 
 
class Config:
    """Configurações comuns a todos os ambientes."""
 
    SECRET_KEY = os.environ.get("SECRET_KEY", "troque-esta-chave-em-producao")
 
    # Banco de dados: SQLite por padrão; troque por PostgreSQL via DATABASE_URL
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'farmarota.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    # Segurança dos cookies de sessão
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
 
    # Paginação padrão das buscas
    ITENS_POR_PAGINA = 10
 
 
class DevelopmentConfig(Config):
    DEBUG = True
 
 
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
 
 
class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True  # exige HTTPS
 
 
config_por_ambiente = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
 