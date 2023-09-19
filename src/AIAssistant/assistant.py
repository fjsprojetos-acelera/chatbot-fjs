
from IPython.display import display, HTML


class Assistant:

    def __init__(self, index):
            self.index = index

    def answer_queries(self):
        while True:
            query = input("What do you want to ask? ")
            response = self.index.query(query)
            response_text = response.response
            html_output = HTML(f"Response: <b>{response_text}</b>")
            display(html_output.data)