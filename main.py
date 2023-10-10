import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_chat import message
import openai
from streamlit_tags import st_tags 

#hi
st.markdown(
    """
    <style>
    .block-container {
        text-align: center;

    }

    .title {
        align-self: flex-start;  
     </style>
    """,
    unsafe_allow_html=True
)

 

selected_page = option_menu(
    menu_title=None,
    options=["Home", "Chatbot", "Option 2", "Option 3"],
    icons=["map", "person-circle", "info", "geo"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)




if selected_page == "Home":
    

     
    def main():
        st.header("Mental Health Web App")

        page = option_menu(
            menu_title=None,
            options=["Part 1", "Part 2"],
            icons=["map", "person-circle"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            key="nav_bar"
)
        st.markdown("<br>", unsafe_allow_html=True)  # Add a line break



    if __name__ == '__main__':
        main()
 

  
 
elif selected_page == "Chatbot":
    openai.api_key = "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"

    def generate_response(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        generated_text = response.choices[0].message.content

        return generated_text
    
    st.header("Chatbot - Your AI Mental Therapist")

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state: 
        st.session_state['past'] = []
    
    def get_text():
        input_text = st.text_input("You: ", "How can I cope with criplling depression?", key="input")
        return input_text
    
    user_input = get_text()

    if user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
    
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
            


elif selected_page == "Option 3":
    st.title("Option 3")

 
        
    
   
 
    

     
elif selected_page == "Option 3":
    # Render the Stock Market Predictions Tool page
    st.title("Option 3")

     
