from core.planner.task import Task


class TaskParser:

    def parse(self, command):

        command = command.lower()

        command = command.replace(" then ", " and ")

        parts = command.split(" and ")

        tasks = []

        previous_action = None

        for part in parts:

            part = part.strip()

            if part.startswith("open "):

                previous_action = "open"

                tasks.append(Task("open", part.replace("open ", "").strip()))

                continue

            if part.startswith("launch "):

                previous_action = "open"

                tasks.append(Task("open", part.replace("launch ", "").strip()))

                continue

            if part.startswith("search google for "):

                previous_action = "google"

                tasks.append(Task("google", part.replace("search google for ", "")))

                continue

            if part.startswith("search youtube for "):

                previous_action = "youtube"

                tasks.append(Task("youtube", part.replace("search youtube for ", "")))

                continue

            if previous_action == "open":

                tasks.append(Task("open", part))

        return tasks
