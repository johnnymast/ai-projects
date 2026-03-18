import gradio as gr
from ai_client import generate_ai_response

def chat(message, history):
    """
    Main chat handler for Gradio.
    `history` is a list of [user, assistant] message pairs.
    """
    response = generate_ai_response(message, history)
    return response

with gr.Blocks(title="AI Chatbot") as demo:
    gr.Markdown("# 💬 AI Chatbot\nA simple, extensible AI-powered chatbot.")

    gr.ChatInterface(
        fn=chat,
        chatbot=gr.Chatbot(height=400),
        textbox=gr.Textbox(placeholder="Type your message...", container=True),
        title="AI Chatbot",
        description="A minimal Gradio-based chatbot using an LLM backend."
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

