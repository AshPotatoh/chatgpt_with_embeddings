import streamlit as st
from streamlit_chat import message

from chatbot import chat_bot



st.title('ChatGPT with custom embeddings')
st.markdown("This is a chatbot that can access your custom embeddings. If you would like to clear the screen. Type 'clear' and press enter. This app currently does not take into account the previous context of the conversation to save on costs.\n\n\n *It will take a second after pressing enter for your response to show. Its thinking. It'll be REALLY obvious if theres an error*")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_request():
    input_text = st.text_input("You: ", value="", key="input")
    return input_text

user_request = get_request()

if user_request:
    if user_request == "clear":
        st.session_state['generated'] = []
        st.session_state['past'] = []
    else:
        output = chat_bot(user_request)
        st.session_state.past.append(user_request)
        st.session_state.generated.append(output)

if st.session_state['generated']:
    for messages in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][messages], key=str(messages))
        message(st.session_state['past'][messages], key=str(messages) + "_user", is_user=True)
