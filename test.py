import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from PIL import Image
import io
import base64

load_dotenv()

st.set_page_config(page_title="Dream Visualizer", page_icon="🚀", layout="centered")

st.title("Dream Visualizer")
st.markdown("""
Upload a photo of yourself and enter your dream goal (e.g., 'I want to be an astronaut'). 
Our AI will create a visualized image of your dream!
""")

if "OPENAI_API_KEY" not in os.environ:
    st.error("Please set the OPENAI_API_KEY in the .env file.")
    st.stop()

client = OpenAI()

uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])

goal = st.text_input("Enter your dream goal", placeholder="e.g., I want to be an astronaut")

generate_button = st.button("Generate Dream Image")

generated_image_placeholder = st.empty()

download_placeholder = st.empty()

if generate_button:
    if not uploaded_file or not goal:
        st.error("Please upload a photo and enter a goal.")
    else:
        with st.spinner("Generating your dream image..."):
            try:
                img = Image.open(uploaded_file)
                buffered = io.BytesIO()
                img.save(buffered, format="PNG")
                img_base64 = base64.b64encode(buffered.getvalue()).decode()

                vision_response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Provide a detailed description of the person in the image, focusing on their physical features (e.g., hair color, body type), clothing, and background setting. Exclude any identifying details like names or specific locations. Emphasize aspects relevant to visualizing them in a new context, such as their attire and posture."
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{img_base64}"
                                    }
                                }
                            ]
                        }
                    ],
                    max_tokens=300
                )
                person_description = vision_response.choices[0].message.content
                print(person_description)

                dalle_prompt = f"""
                Create a visually striking and emotionally resonant portrait of an Indian student who has fully realized their dream: {goal}.
                Seamlessly preserve their physical appearance and emotional essence based on: {person_description}.

                Depict a powerful, life-defining moment captured just after their success — their expression should convey fulfillment, pride, and confidence.
                Their environment, attire, and body language must authentically reflect the dream achieved, grounded in cultural and contextual realism.

                The image should serve as a deeply personal and aspirational vision — one that inspires new students by showing who they could become.
                """

                dalle_response = client.images.generate(
                    model="dall-e-3",
                    prompt=dalle_prompt,
                    n=1,
                    size="1024x1024",
                    quality="hd",
                    response_format="url"
                )
                image_url = dalle_response.data[0].url

                response = requests.get(image_url)
                if response.status_code == 200:
                    generated_img = Image.open(io.BytesIO(response.content))
                    generated_image_placeholder.image(generated_img, caption="Your Dream Visualization", use_container_width=True)

                    img_buffer = io.BytesIO()
                    generated_img.save(img_buffer, format="PNG")
                    img_buffer.seek(0)

                    download_placeholder.download_button(
                        label="Download Image",
                        data=img_buffer,
                        file_name="dream_visualization.png",
                        mime="image/png"
                    )
                else:
                    st.error("Failed to retrieve the generated image.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.markdown("---")
st.markdown("""
### Welcome to Your Future
As you step into our college, we want you to visualize the incredible journey ahead.  
Upload your photo and tell us your dream.  
Our AI will show you — not the dream, but **you after achieving it**.

💡 Powered by advanced AI. Tailored for Indian students. Built to inspire.
""")
st.markdown("Built with ❤️ using Streamlit and OpenAI")