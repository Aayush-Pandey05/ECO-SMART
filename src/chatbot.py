import google.generativeai as genai
from google.generativeai import GenerativeModel
import gradio as gr

messages = [{"role": "system", "content":"You are a virtual assistant for a waste management website. Provide informative and helpful advice based on the user's query. Consider factors like sleep patterns, age, and health conditions. Avoid giving medical advice. Do not generate asterisks (*) or hashtags (#) in the output."
}]




def chat(user_input):
    messages.append({"role": "user", "content": user_input})

    model = GenerativeModel('gemini-1.5-flash')
    
    genai.configure(api_key=Your API key)
    response = model.generate_content(user_input)
    return response.text



iface = gr.Interface(fn=chat, inputs="text", outputs="text", title="Chat bot")
iface.launch(share=True)
