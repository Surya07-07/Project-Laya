import os


class FileExecutor:


    def create_folder(self, path):

        if os.path.exists(path):

            return {
                "success": False,
                "message": "Folder already exists"
            }


        os.makedirs(path)

        return {
            "success": True,
            "message": f"Created folder: {path}"
        }


    def list_folder(self, path):

        if not os.path.exists(path):

            return {
                "success": False,
                "message": "Folder not found"
            }


        files = os.listdir(path)

        return {
            "success": True,
            "files": files
        }
