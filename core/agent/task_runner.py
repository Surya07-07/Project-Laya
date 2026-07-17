class TaskRunner:


    def __init__(self, executor):

        self.executor = executor



    def run(self, steps):


        results = []


        for step in steps:


            result = self.executor.execute(
                step["tool"],
                step["data"]
            )


            results.append({

                "step": step,

                "result": result

            })


        return results
