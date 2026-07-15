from pathlib import Path
import environ

import Feature_Flag_Platform.apps

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")

# ------------------------------------------------

SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = []

# ------------------------------------------------

DJANGO_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

]

THIRD_PARTY_APPS = [

    "rest_framework",

    "django_filters",

    "drf_spectacular",

]

LOCAL_APPS = [

    "Feature_Flag_Platform.apps.accounts.apps.AccountsConfig",

    # "Feature_Flag_Platform.apps.features.apps.FeaturesConfig",

    # "Feature_Flag_Platform.apps.audit",

    # "Feature_Flag_Platform.apps.common",

]

INSTALLED_APPS = (

    DJANGO_APPS

    + THIRD_PARTY_APPS

    + LOCAL_APPS

)

# ------------------------------------------------

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

# ------------------------------------------------

ROOT_URLCONF = "Feature_Flag_Platform.config.urls"

# ------------------------------------------------

TEMPLATES = [

{
    "BACKEND":"django.template.backends.django.DjangoTemplates",

    "DIRS":[BASE_DIR/"templates"],

    "APP_DIRS":True,

    "OPTIONS":{

        "context_processors":[

            "django.template.context_processors.request",

            "django.contrib.auth.context_processors.auth",

            "django.contrib.messages.context_processors.messages",

        ]

    }

}

]

# ------------------------------------------------

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

# ------------------------------------------------

DATABASES = {

    "default":{

        "ENGINE":"django.db.backends.postgresql",

        "NAME":env("DB_NAME"),

        "USER":env("DB_USER"),

        "PASSWORD":env("DB_PASSWORD"),

        "HOST":env("DB_HOST"),

        "PORT":env("DB_PORT"),

    }

}

# ------------------------------------------------
AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },

    {
        "NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"
    },

    {
        "NAME":"django.contrib.auth.password_validation.CommonPasswordValidator"
    },

    {
        "NAME":"django.contrib.auth.password_validation.NumericPasswordValidator"
    },

]

# ------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# ------------------------------------------------

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [

    BASE_DIR/"static"

]

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR/"media"

# ------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------

REST_FRAMEWORK = {

    "DEFAULT_SCHEMA_CLASS":

    "drf_spectacular.openapi.AutoSchema",

    "DEFAULT_PERMISSION_CLASSES":[

        "rest_framework.permissions.IsAuthenticated"

    ],

    "DEFAULT_FILTER_BACKENDS":[

        "django_filters.rest_framework.DjangoFilterBackend"

    ]

}

# ------------------------------------------------

SPECTACULAR_SETTINGS = {

    "TITLE":"Feature Flag API",

    "DESCRIPTION":"Feature Flag Platform",

    "VERSION":"1.0.0"

}

# ------------------------------------------------

REDIS_URL = env(
    "REDIS_URL"
)

CACHES = {

    "default":{

        "BACKEND":"django.core.cache.backends.redis.RedisCache",

    "LOCATION":REDIS_URL,

}

}

# ------------------------------------------------

CELERY_BROKER_URL = REDIS_URL

CELERY_RESULT_BACKEND = REDIS_URL