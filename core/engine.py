import asyncio

class Engine:
    async def run(self, target, modules):
        tasks = [module.run(target) for module in modules]
        return await asyncio.gather(*tasks, return_exceptions=True)
