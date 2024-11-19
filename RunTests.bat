@echo off

whoami /groups | find "S-1-5-32-544" > nul && echo Running as Admin || echo Not running as Admin

behave --tags=qupos -f html -o Reports/htmlReport/report.html