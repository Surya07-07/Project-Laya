from core.automation.manager import AutomationManager

automation = AutomationManager()

print(automation.handle("open notepad"))

print(automation.handle("open calculator"))

print(automation.handle("open google.com"))
