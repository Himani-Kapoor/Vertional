#!/usr/bin/env python
import os
import runpy
import sys
from pathlib import Path

project_dir = Path(__file__).resolve().parent / "vertionalhead"
manage_py = project_dir / "manage.py"

if not manage_py.exists():
    raise SystemExit(f"Could not find Django project manager at {manage_py}")

os.chdir(project_dir)
sys.path.insert(0, str(project_dir))
runpy.run_path(str(manage_py), run_name="__main__")
