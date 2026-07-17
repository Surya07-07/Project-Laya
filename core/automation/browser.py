import webbrowser


class Browser:

    def open(self, url):

        if not url.startswith("http"):

            url = "https://" + url

        webbrowser.open(url)

        return True
