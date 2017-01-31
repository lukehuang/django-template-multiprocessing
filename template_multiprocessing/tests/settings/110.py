import os
import glob


if "VIRTUAL_ENV" in os.environ:
    BASE_DIR = os.path.join(
        glob.glob(os.environ["VIRTUAL_ENV"] +  "/lib/*/site-packages")[0],
        "template_multiprocessing"
    )
else:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "SECRET_KEY_PLACEHOLDER"

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS = (
    "template_multiprocessing.tests",
    "template_multiprocessing",
    "django.contrib.auth",
    "django.contrib.contenttypes",
)

ROOT_URLCONF = "template_multiprocessing.tests.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

USE_TZ = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
