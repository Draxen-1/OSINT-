import importlib.util
import os

BASE_DIR = os.path.dirname(__file__)

def load_modules(name):
    path = os.path.join(BASE_DIR, "modules", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
