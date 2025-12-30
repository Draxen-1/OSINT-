import aiohttp

class Module:
    name = "Username OSINT"

    async def run(self, username):
        sites = {
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "GitLab": f"https://gitlab.com/{username}"
        }

        found = []

        async with aiohttp.ClientSession() as session:
            for site, url in sites.items():
                try:
                    async with session.get(url) as r:
                        if r.status == 200:
                            found.append(site)
                except:
                    pass

        return found if found else "No public presence"
