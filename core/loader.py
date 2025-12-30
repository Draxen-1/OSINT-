import importlib
import os

def load_modules(specific=None):
    modules = []

    for file in os.listdir("modules"):
        if file.endswith(".py") and not file.startswith("__"):
            name = file[:-3]
            if specific and name != specific:
                continue
            mod = importlib.import_module(f"modules.{name}")
            modules.append(mod.Module())

    return modules
