import json
import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
huggingfacehub_api_token = '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'
from llama_index import GPTListIndex, LLMPredictor
from langchain import OpenAI
from llama_index.composability import ComposableGraph

login(token=huggingfacehub_api_token)



API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
headers = {"Authorization": f"Bearer hf_XXXXXXXXXXXXXXXX",
        "Content-Type": "application/json",}
def query(payload):
    data = json.dumps({"inputs": payload})
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("Can you please let us know more details about your ")
print(data)

llm = HuggingFaceHub(repo_id='meta-llama/Llama-2-7b', huggingfacehub_api_token=huggingfacehub_api_token)
input = "Hi, Whats your name?"
output = llm.invoke(input)
print(output)


model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1", device_map="auto", load_in_4bit=True, huggingfacehub_api_token=huggingfacehub_api_token
)

from transformers import pipeline
import torch

instruct_pipeline = pipeline(model="databricks/dolly-v2-12b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
print(instruct_pipeline("Explain to me the difference between nuclear fission and fusion."))



model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

inputs = tokenizer("Hi! What is your name?")
outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)


from huggingface_hub import InferenceClient
import json
repo_id = "deepset/roberta-base-squad2"
llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
)



def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},
            "task": "text-summarization",
        },
    )
    return json.loads(response.decode())[0]["generated_text"]
response=call_llm(llm_client, "sec-10k analysis for AAPL")
print (response)


from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print(tokenizer)


# Load indices from disk
index_set = {}
for year in range(2002,2024):
    cur_index = GPTSimpleVectorIndex.load_from_disk(f'index_{year}.json', service_context=service_context)
    index_set[year] = cur_index


    response = index_set[2020].query(f"What were some of the biggest risk factors in year?", similarity_top_k=3)


risk_query_str = (
    "Describe the current risk factors. If the year is provided in the information, "
    "provide that as well. If the context contains risk factors for multiple years, "
    "explicitly provide the following:\n"
    "- A description of the risk factors for each year\n"
    "- A summary of how these risk factors are changing across years"
)