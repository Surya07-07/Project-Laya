import time


class RetryEngine:

    def __init__(self, max_retry=3):

        self.max_retry = max_retry

    def run(self, function, *args):

        attempts = 0

        while attempts < self.max_retry:

            try:

                result = function(*args)

                if self.is_success(result):

                    return {"success": True, "attempts": attempts + 1, "result": result}

            except Exception as e:

                result = {"success": False, "error": str(e)}

            attempts += 1

            print(f"🔄 Retry {attempts}/{self.max_retry}")

            time.sleep(1)

        return {"success": False, "attempts": attempts, "result": result}

    def is_success(self, result):

        if isinstance(result, dict):

            return result.get("success", False)

        return False
