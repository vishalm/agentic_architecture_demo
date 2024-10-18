from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaTokenizerFast,LlamaTokenizer
import json

# Load the model and tokenizer (Mistral, LLaMA, etc.)
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v0.6"  # Or Mistral equivalent model
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token 
tokenizer.pad_token_id = tokenizer.eos_token_id 

model = AutoModelForCausalLM.from_pretrained(model_name)

# Define the functions: add_numbers and subtract_numbers
def add_numbers(a, b):
    return {"result": a + b}

def subtract_numbers(a, b):
    return {"result": a - b}

# Define a list of functions with descriptions
functions = [
    {
        "name": "add_numbers",
        "description": "Add two numbers together",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number to add"},
                "b": {"type": "number", "description": "The second number to add"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "subtract_numbers",
        "description": "Subtract one number from another",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The number to subtract from"},
                "b": {"type": "number", "description": "The number to subtract"}
            },
            "required": ["a", "b"]
        }
    }
]

# Function to call the model and return its output
def call_model(prompt):
    inputs = tokenizer(prompt, return_tensors="pt",padding=True, truncation=True)
    
    attention_mask = [1 if token_id != tokenizer.pad_token_id else 0 for token_id in inputs['input_ids'][0]]
    inputs['attention_mask'] = attention_mask
    
    outputs = model.generate(inputs.input_ids, max_length=1000)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Dynamically execute the chosen function
def execute_function_by_name(function_name, arguments):
    if function_name == "add_numbers":
        return add_numbers(arguments['a'], arguments['b'])
    elif function_name == "subtract_numbers":
        return subtract_numbers(arguments['a'], arguments['b'])
    else:
        raise ValueError(f"Unknown function: {function_name}")

# Function to format the functions metadata and prompt the LLM
def prompt_llm_to_select_function(user_input):
    # Provide the function meta-information in the prompt
    function_descriptions = "\n".join([
        f"Function: {f['name']}\nDescription: {f['description']}\nParameters: {json.dumps(f['parameters'])}"
        for f in functions
    ])
    
    prompt = f"""
    I have the following functions:
    
    {function_descriptions}
    
    User Input: "{user_input}" with values.
    
    Which function should be called, and what are the parameters for that function? Please return in JSON format, specifying the function name and the arguments.
    """

    response = call_model(prompt)

    # prompt = tokenizer(prompt, return_tensors="pt")
    # inputs = tokenizer(prompt, return_tensors="pt")

    # Generate a response
    # outputs = model.generate(**inputs, max_length=1000)
    # response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print (response)
    # function_decision = "add"
    
    # Attempt to parse the response as JSON
    try:
        print(response)
        function_decision = json.loads(response)
        print(response)
    except json.JSONDecodeError:
        return {"error": "Failed to parse the LLM's response as JSON."}
    
    return function_decision

# Main loop to prompt the user and call the model
while True:
    user_input = input("Enter a math problem (e.g., 'What is 5 + 3?') or 'exit' to quit: ")
    if user_input.lower() == "exit":
        break

    # Prompt the LLM to select the function and return parameters
    function_decision = prompt_llm_to_select_function(user_input)
    
    if "error" in function_decision:
        print(function_decision['error'])
    else:
        # Extract function name and arguments
        function_name = function_decision['name']
        arguments = function_decision['arguments']
        
        # Call the selected function
        result = execute_function_by_name(function_name, arguments)
        print(f"Function called: {function_name}, Result: {result['result']}")
