rem pyinstaller --onefile  --noconsole --noupx --icon="app.ico" --hidden-import win32timezone app.py
rem pyinstaller --onefile  --noupx --icon="app.ico" --hidden-import win32timezone app.py

pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py

pause