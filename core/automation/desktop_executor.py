import os


class DesktopExecutor:

    def open_application(self, app):

        try:

            os.startfile(app)

            return {"success": True, "message": f"Opened {app}"}

        except Exception as e:

            return {"success": False, "error": str(e)}
