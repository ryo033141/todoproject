from pathlib import Path
import os
import dj_database_url

# ---------------------------------------
# Base Directory
# ---------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------
# Security
# ---------------------------------------
# Railway では SECRET_KEY を環境変数に入れておく
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

# DEBUG は環境変数 DEBUG=True で ON にできる
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Railway ではドメインが変わるため全許可でOK
ALLOWED_HOSTS = ["*"]


# ---------------------------------------
# Installed Apps
# ---------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo.apps.TodoConfig',   # ← あなたのアプリ
]


# ---------------------------------------
# Middleware
# ---------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Whitenoise はここが正解の順番
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ---------------------------------------
# URL Configuration
# ---------------------------------------
ROOT_URLCONF = 'todoproject.urls'


# ---------------------------------------
# Templates
# ---------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # あなたの指定を維持
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ---------------------------------------
# WSGI
# ---------------------------------------
WSGI_APPLICATION = 'todoproject.wsgi.application'


# ---------------------------------------
# Database
# ---------------------------------------
# DEBUG=True は sqlite、そのほかは Railway の Postgres
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default='postgresql://postgres:postgres@localhost:5432/todoproject',
            conn_max_age=600,
            ssl_require=False
        )
    }


# ---------------------------------------
# Password validators
# ---------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ---------------------------------------
# Internationalization
# ---------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ---------------------------------------
# Static files
# ---------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # ← collectstatic の置き場所

# Whitenoise で gzip / brotli 圧縮対応
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ---------------------------------------
# Default primary key field type
# ---------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
