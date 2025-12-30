import socket

name = "domain"

async def run(target):
    print(f"[DOMAIN] Analyse du domaine : {target}")

    try:
        ip = socket.gethostbyname(target)
        return {"ip": ip}
    except Exception:
        return "Domain not resolvable"

