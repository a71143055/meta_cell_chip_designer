# Meta-Cell Chip Designer

A minimal, reliable Windows desktop app for designing meta-learning, cell-like semiconductor circuits.

- GUI: PySide6 (Qt)
- Simulation: simple toy DC solver
- Meta-learning: finite-difference parameter tuning
- Packaging: PyInstaller

## Setup

1. Install Python 3.10+ (Windows).
2. In project root: `pip install -r requirements.txt`.

## Run

- From root:
    - `python -m app`
    - or `python -m app.main`
- From app folder:
    - `python main.py`

## Package (Windows exe)

- From root:
    - `tools\package_windows.bat`
- Result: `dist\MetaCellDesigner.exe`

## Notes

- All imports use absolute paths (e.g., `from app.ui.main_window import MainWindow`) to avoid relative-import issues.
- `app/__main__.py` lets you run with `python -m app`.
