class PlanVerifier:


    def verify(self, result):


        if isinstance(result, dict):


            if result.get(
                "success"
            ):

                return {

                    "verified": True,

                    "message":
                    "Action completed successfully"

                }



        return {

            "verified": False,

            "message":
            "Action failed"

        }



    def should_retry(self, result):


        check = self.verify(
            result
        )


        return not check["verified"]
