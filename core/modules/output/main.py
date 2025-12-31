import sys
import os

CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)

from loader import load_modules
def main(args):
    module = load_modules(args.module)
    module.main(args.target)

