# AI-Powered-Blog-Post-Generator-with-LLaMA

## Overview

The **AI Blog Generator** is a Streamlit-based application that leverages the **LLaMA** language model (via the `CTransformers` package) to generate high-quality blog posts tailored to specific topics and target audiences. The application allows users to input a topic, specify a word limit, and select the desired audience style for the blog post. The model then generates a tailored blog post based on these inputs.

## Features

- Generate blog posts for various job profiles and topics using AI.
- Adjustable word count for blog length.
- Choose the target audience for tailored content (e.g., Researchers, Data Scientists, Common People).
- Quick and interactive UI via **Streamlit**.
- Utilizes the **LLaMA** language model for blog generation.
  
## Requirements

To run the AI Blog Generator locally, you need to install the following dependencies:

- Python 3.8 or higher
- Streamlit
- Langchain
- CTransformers
- Sentence-Transformers
- Uvicorn
- Python-Box

You can install the dependencies using `pip`:

```bash
pip install streamlit langchain ctransformers sentence-transformers uvicorn python-box
```

Additionally, ensure that the LLaMA model is properly downloaded to your local system at the specified path.

## How to Run

### 1. Install the dependencies

Install the required packages by running:

```bash
pip install -r requirements.txt
```

### 2. Download the LLaMA model

You need to download the LLaMA model and save it in your local directory. Ensure that the path to the model in the script matches your file location:

```python
llm = CTransformers(
    model=r'model\llama-2-7b-chat.ggmlv3.q8_0.bin',
    model_type='llama',
    config={
        'max_new_tokens': int(no_words) + 50,  # Allow flexibility around word limit
        'temperature': 0.05  # Increase creativity slightly
    }
)
```

### 3. Start the Streamlit app

Run the following command to start the app:

```bash
streamlit run app.py
```

This will open the app in your browser at `http://localhost:8501`.

### 4. Using the App

- **Enter the Blog Topic**: Provide a topic for the blog post (e.g., "The Future of AI in Healthcare").
- **Number of Words**: Select the desired length of the blog post (between 100 and 1000 words).
- **Target Audience**: Choose the target audience from the dropdown (e.g., Researchers, Data Scientists, Common People).
- **Generate Blog**: Click the "Generate Blog" button to generate the blog post. The AI will process the inputs and display the generated blog.

### 5. Output

Once the blog is generated, the application will display the blog post in the main area. If the generation fails or the inputs are invalid, appropriate error messages will be shown.

## Code Structure

### `app.py`

This is the main file that contains the Streamlit app configuration and logic.

- **Imports**: Required libraries like Streamlit, Langchain, and CTransformers.
- **get_llama_response()**: The function that loads the LLaMA model, formats the prompt, and generates a blog based on user inputs.
- **Streamlit UI**: Displays the user interface where users can input data and view the results.

### Dependencies

- **streamlit**: For building the interactive web app.
- **langchain**: For integrating with language models, specifically for creating prompt templates.
- **ctransformers**: For running the LLaMA model and generating responses.
- **sentence-transformers**: Optional, for additional NLP tasks, if needed.
- **uvicorn**: For serving the Streamlit app.
- **python-box**: For handling configuration files, if needed.

## Troubleshooting

- **Model File Missing**: Ensure that the path to the LLaMA model file is correct in the script.
- **Streamlit Error**: If the app doesn't start, try updating Streamlit to the latest version:
  ```bash
  pip install --upgrade streamlit
  ```
- **Other Errors**: If the AI doesn't generate a response, check if the required libraries are installed correctly.
