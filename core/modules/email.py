import re

class Module:
    name = "Email OSINT"

    async def run(self, email):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        valid = re.match(pattern, email)
        domain = email.split("@")[-1] if valid else None

        return {
            "valid_format": bool(valid),
            "domain": domain
        }
