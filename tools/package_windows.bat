@echo off
pyinstaller -F -n MetaCellDesigner app\main.py --add-data "cpp\fast_ops.pyd;."
