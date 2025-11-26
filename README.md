# Meta-Cell Chip Designer

A Windows desktop app for designing meta-learning, cell-like semiconductor circuits.
- GUI: PySide6
- Simulation: simple DC/AC pseudo-solver + SPICE export
- Meta-learning: supervised meta-engine optimizing circuit parameters for task objectives
- C++: pybind11-accelerated operations

## Setup
1. Install Python 3.10+
2. `pip install -r requirements.txt`
3. Build C++: `tools/build_cpp.bat`
4. Run: `python -m app.main`

## Windows packaging
- `tools/package_windows.bat` (PyInstaller)
