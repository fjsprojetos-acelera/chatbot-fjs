

from IndexBuilder.builder import Builder
from AIAssistant.assistant import Assistant
import os
import gradio as gr


def main():
    os.environ["OPENAI_API_KEY"] = "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"
    directory_path = "context_data/data"

# realiza as instâncias do indexBuilder
    index_builder = Builder(directory_path)
    index = index_builder.build_index()

# realiza as instâncias do AIAssistant
    assistant = Assistant(index)
    assistant.answer_queries()


""" demo = gr.Interface(fn=main, inputs="text", outputs="text")
demo.launch()
 """

if __name__ == "__main__":
    main()


