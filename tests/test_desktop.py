from core.desktop.controller import DesktopController

desktop = DesktopController()

print(desktop.open_folder("downloads"))

desktop.search_google("Project Laya")

desktop.search_youtube("Python AI")

desktop.open_github()

print(desktop.screenshot())
