import streamlit as st
import httpx

API_URL = "http://127.0.0.1:8000/movies"


def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def show_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def format_movie(movie: dict) -> str:
    return (
        f"**{movie.get('title')}** ({movie.get('year')})\n\n"
        f"Genre: {movie.get('genre')}  \n"
        f"Rating: {movie.get('rating')}\n\n"
        f"{movie.get('summary')}"
    )


def ask_backend(prompt: str) -> str:
    try:
        response = httpx.post(API_URL, json={"question": prompt}, timeout=60)
        response.raise_for_status()
        return format_movie(response.json())
    except httpx.HTTPError as error:
        return f"Något gick fel: {error}"


def handle_user_input():
    if prompt := st.chat_input("Find movie"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Letar film..."):
                answer = ask_backend(prompt)
            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})


def layout():
    st.markdown("# Chat with movie finder")
    st.write("Beskriv en film du vill hitta så letar movie finder upp den åt dig")

    init_session()
    show_history()
    handle_user_input()


if __name__ == "__main__":
    layout()