import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get the response from LLaMA model
def get_llama_response(input_text, no_words, blog_style):
    try:
        # Load the model
        llm = CTransformers(
            model=r'model\llama-2-7b-chat.ggmlv3.q8_0.bin',
            model_type='llama',
            config={
                'max_new_tokens': int(no_words) + 50,  # Allow flexibility around word limit
                'temperature': 0.05  # Increase creativity slightly
            }
        )

        # Prompt template
        template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """

        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )

        # Generate response
        response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        return response
    
    except Exception as e:
        return f"Error generating the blog: {str(e)}"

# Streamlit app configuration
st.set_page_config(
    page_title="AI Blog Generator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# App Header
st.header("AI Blog Generator")
st.write("Generate high-quality blog posts tailored for your audience using LLaMA!")

# User Inputs
input_text = st.text_input("Enter the Blog Topic", placeholder="e.g., The Future of AI in Healthcare")

col1, col2 = st.columns(2)

with col1:
    no_words = st.number_input('Number of Words', min_value=100, max_value=1000, value=300, step=50)

with col2:
    blog_style = st.selectbox(
        'Target Audience',
        ('Researchers', 'Data Scientists', 'Common People'),
        index=0
    )

# Submit Button
submit = st.button("Generate Blog")

# Handle Submit
if submit:
    if not input_text:
        st.warning("Please enter a blog topic to proceed.")
    else:
        with st.spinner("Generating your blog..."):
            response = get_llama_response(input_text, no_words, blog_style)
            if response:
                st.subheader("Your Generated Blog:")
                st.write(response)
            else:
                st.error("Failed to generate blog. Please try again.")



















