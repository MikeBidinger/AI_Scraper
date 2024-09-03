from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {html_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_desc}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3")


def ollama_parse(html_batches: list, parse_desc: str):
    print("Parsing the HTML batches...")
    # Setup the LLM
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    # Parse the html batches with the LLM
    parsed_results = []
    for i, batch in enumerate(html_batches, start=1):
        response = chain.invoke({"html_content": batch, "parse_desc": parse_desc})
        print(f"Parsed batch {i} of {len(html_batches)}.")
        parsed_results.append(response)
    # Return the total result of parsed html batches
    return "\n".join(parsed_results)
