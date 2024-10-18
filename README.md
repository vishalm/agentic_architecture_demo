# Agentic Architecture Demo - Calculator Operations with LLM and RAG

## Overview

This demo showcases the use of **Agentic Architecture** to select calculator operations using a **Large Language Model (LLM)**. Additionally, it demonstrates **Retrieval-Augmented Generation (RAG)** on the meta-information of calculator functions to provide context-aware insights and suggestions for operation selection.

### Key Components:

1. **LLM-driven Operation Selection**:
   - The user provides a query related to calculator functions.
   - The LLM processes the query and suggests relevant operations (e.g., addition, subtraction, multiplication).
   - The model used for this demo is `TinyLlama/TinyLlama-1.1B-Chat-v0.6` or an equivalent **Mistral** model.
   
2. **RAG for Meta Information**:
   - Meta-information about each calculator function (e.g., function names, parameters, descriptions) is stored in a knowledge base.
   - The demo uses RAG to retrieve relevant information from the knowledge base based on the user's query and the selected operation.

### Architecture

The demo utilizes the following architecture:

1. **Query Input**: 
   - A natural language query (e.g., "Which operation can I use to add two numbers?") is passed to the LLM.
   
2. **LLM Processing**:
   - The LLM (`TinyLlama/TinyLlama-1.1B-Chat-v0.6` or Mistral equivalent) interprets the query and suggests potential calculator operations such as addition, subtraction, multiplication, or division.
   
3. **Meta Information Retrieval (RAG)**:
   - Once an operation is selected, the system performs RAG to retrieve relevant meta-information (such as the formula or parameters) from a pre-indexed knowledge base.
   
4. **Execution or Display**:
   - The selected operation and meta-information are either displayed to the user or executed by the calculator function.

### Key Features

- **Natural Language Interaction**: Users can interact with the system using natural language queries instead of manual operation selection.
- **Dynamic Retrieval**: The demo employs RAG to dynamically retrieve and display relevant metadata about the calculator's functions, enriching the user experience.
- **Enhanced Context**: Meta-information retrieved for each function enhances decision-making, especially for users unfamiliar with specific operations.

### Calculator Functions Included

The demo includes basic calculator operations:
- **Addition** (`add(a, b)`): Adds two numbers.
- **Subtraction** (`subtract(a, b)`): Subtracts the second number from the first.
- **Multiplication** (`multiply(a, b)`): Multiplies two numbers.
- **Division** (`divide(a, b)`): Divides the first number by the second.

Meta-information for each function (description, formula, constraints) is stored in a structured format and accessed via the RAG mechanism.

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/vishalm/agentic_architecture_demo.git
   ```
   
2. Install dependencies:
   ```bash
   cd agentic-architecture-calculator-demo
   pip install -r requirements.txt
   ```
   
3. Run the demo:
   ```bash
   python main.py
   ```

### Example Usage

- **User Query**: "How do I add two numbers?"
- **LLM Response**: "You can use the addition operation."
- **RAG Result**: Displays meta-information about the `add(a, b)` function, such as the function signature and examples.

### Future Enhancements

- Support for more advanced calculator functions (e.g., square root, exponents).
- Integration with a live calculator interface.
- Improved LLM capabilities for more complex mathematical queries.
