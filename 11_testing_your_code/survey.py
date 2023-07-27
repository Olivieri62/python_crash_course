class AnonymousSurvey:
    """Collect anonymous answers to a question"""

    def __init__(self, question):
        """ Store a question, and prepare to store reponses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """"Show the survey question"""
        print(self.question)

    def store_reponse(self,new_reponse):
        """Store a single response to the survey"""
        self.responses.append(new_reponse)

    def show_results (self):
        """Show all the responses that habe been given"""
        print("Survey results:")
        for response in self.responses :
            print(f" - {response}")
       