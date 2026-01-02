from .social import PLATFORMS as SOCIAL
from .dev import PLATFORMS as DEV
from .gaming import PLATFORMS as GAMING
from .forums import PLATFORMS as FORUMS
from .commerce import PLATFORMS as COMMERCE
from .streaming import PLATFORMS as STREAMING
from .crypto import PLATFORMS as CRYPTO
from .misc import PLATFORMS as MISC

PLATFORMS = {
    **SOCIAL,
    **DEV,
    **GAMING,
    **FORUMS,
    **COMMERCE,
    **STREAMING,
    **CRYPTO,
    **MISC
}

