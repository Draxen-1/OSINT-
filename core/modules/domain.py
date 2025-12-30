import socket

class Module:
    name = "Domain OSINT"

    async def run(self, domain):
        try:
            ip = socket.gethostbyname(domain)
            return {"ip": ip}
        except:
            return "Domain not resolvable"
