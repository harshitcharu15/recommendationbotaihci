import streamlit as st
from interactrecommend import get_recommendation

st.set_page_config(page_title="Travel Recommender", layout="centered")

st.title("🌍 AI Travel Recommendation Bot")

st.markdown("Tell me what kind of vacation you're looking for:")

user_input = st.text_area("Your travel preferences", placeholder="e.g. I want a sunny beach in Europe with great food...")

if st.button("Get Recommendations"):
    with st.spinner("Thinking..."):
        recommendation = get_recommendation(user_input)
        st.success("Here's a recommendation for you!")
        st.write(recommendation)
