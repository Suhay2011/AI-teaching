import streamlit as st
from openai import OpenAI

API_KEY=""

client=OpenAI(api_key=API_KEY,base_url="https://api.groq.com/openai/v1")

Model = "openai/gpt-oss-20b"
def generate(prompt):
  try:
    response = client.chat.completions.create(
        model=Model,
        messages=[
         {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1024
    )

    return response.choices[0].message.content

  except Exception as e:
    return "Error: "+ str(e)

st.set_page_config(page_title="AI Learning Assistant ", layout="centered")
st.title("Ai teaching Assistant")
st.write("Ask me anything about various subjects. ")
if "history" not in st.session_state:
  st.session_state.history=[]
question=st.text_input("Enter your question: ")
if st.button("ask"):
  if question.strip():
    with st.spinner("generating response"):
      answer=generate(question)
    st.session_state.history.insert(0,{"question":question, "answer":answer})
    
  else:
    st.warning("Pewase enter a question: ")
if st.session_state.history:
  st.markdown("### Conversation History")
  for i,chat in enumerate(st.session_state.history,1):
    st.markdown(f"q{i}:{chat['question']}")
    st.write(chat["answer"])
    st.divider()

if st.button("clear conversation"):
  st.session_state.history=[]
  st.rerun()