import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.account"
    label = "pinax_account"
    verbose_name = _("Pinax Account")

