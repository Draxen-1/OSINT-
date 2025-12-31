from .social import PLATFORMS as SOCIAL
from .dev import PLATFORMS as DEV
from .gaming import PLATFORMS as GAMING
from .forums import PLATFORMS as FORUMS
from .crypto import PLATFORMS as CRYPTO

PLATFORMS = {}
for group in (SOCIAL, DEV, GAMING, FORUMS, CRYPTO):
    PLATFORMS.update(group)
