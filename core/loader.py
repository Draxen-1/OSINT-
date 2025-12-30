import os
import importlib.util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")

def load_modules(selected_module=None):
    loaded_modules = []

    if not os.path.isdir(MODULES_DIR):
        raise FileNotFoundError(f"Dossier modules introuvable : {MODULES_DIR}")

    for file in os.listdir(MODULES_DIR):
        if not file.endswith(".py") or file.startswith("__"):
            continue

        module_name = file[:-3]

        if selected_module and module_name != selected_module:
            continue

        module_path = os.path.join(MODULES_DIR, file)

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, "run"):
            raise AttributeError(f"Le module {module_name} n'a pas de fonction run()")

        loaded_modules.append(module)

    return loaded_modules

