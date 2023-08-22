import streamlit as st
import ChatBot as bot
import ChatBot


def send(text):
    if text == 'exit':
        return 0
    return ob.response(text)


ob = ChatBot.ChatBot.getBot()
st.title("Welcome to AI Chatbot")
text = st.text_area("You can ask me anything", placeholder='Type here....', height=15)
if st.button(label='Send', help=''):
    st.write(send(text))
