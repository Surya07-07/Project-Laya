from rapidfuzz import fuzz


class AppMatcher:

    def __init__(self, database):

        self.database = database

    def find(self, query):

        query = query.lower().strip()

        aliases = {

            "browser": [
                "google chrome",
                "chrome",
                "brave",
                "edge",
                "firefox"
            ],

            "editor": [
                "visual studio code",
                "vscode",
                "code",
                "pycharm",
                "notepad++"
            ],

            "music": [
                "spotify",
                "itunes",
                "vlc"
            ],

            "video": [
                "vlc",
                "movies & tv"
            ],

            "terminal": [
                "windows terminal",
                "cmd",
                "powershell"
            ]
        }

        for category in aliases:

            if query == category:

                for candidate in aliases[category]:

                    path = self.database.search(candidate)

                    if path:

                        return path

        best_score = 0
        best_match = None

        for app in self.database.apps:

            score = fuzz.ratio(query, app)

            if score > best_score:

                best_score = score

                best_match = app

        if best_score >= 70:

            return self.database.apps[best_match]

        return None
