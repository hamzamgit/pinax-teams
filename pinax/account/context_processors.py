from pinax.account.conf import settings
from pinax.account.models import Account


def account(request):
    ctx = {
        "account": Account.for_request(request),
        "ACCOUNT_OPEN_SIGNUP": settings.ACCOUNT_OPEN_SIGNUP,
    }
    return ctx
