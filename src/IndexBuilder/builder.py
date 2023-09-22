from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI

#1 token is approximately 4 characters or 0.75 words for English text.

class Builder:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def build_index(self):
        max_input_size = 4096
        num_outputs = 2000
        max_chunk_overlap = 20
        chunk_size_limit = 600

        prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))

        documents = SimpleDirectoryReader(self.directory_path).load_data()
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
        index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

        index.save_to_disk('index.json')
        return index