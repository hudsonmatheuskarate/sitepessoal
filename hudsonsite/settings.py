import os
from pathlib import Path
import dj_database_url # Certifique-se de instalar: pip install dj-database-url

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURANÇA: Em produção, o ideal é usar variáveis de ambiente
SECRET_KEY = 'django-insecure-substitua-isso-por-uma-chave-real-em-producao'

# DEBUG deve ser False em produção, mas deixaremos True para você testar o deploy agora
DEBUG = True

# Permitir o domínio do Render
ALLOWED_HOSTS = ['*']

# Definição dos Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main', # Seu app principal
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # SERVE OS ARQUIVOS ESTÁTICOS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hudsonsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hudsonsite.wsgi.application'

# --- BANCO DE DADOS (Configuração para PostgreSQL do Render) ---
DATABASES = {
    'default': dj_database_url.config(
        # Sua URL do banco (O Render preenche isso sozinho se houver a variável DATABASE_URL)
        default='postgresql://admin:m4OoQI2MtAuan5ft4pGqUjgLiXJMHXeC@dpg-d5if2p14tr6s73a5d2fg-a/karater_db',
        conn_max_age=600
    )
}

# --- ARQUIVOS ESTÁTICOS (RESOLVE O ERRO IMPROPERLYCONFIGURED) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Pasta onde o Django reunirá os arquivos para o Render servir
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Armazenamento otimizado com compressão (WhiteNoise)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuração de ID padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'