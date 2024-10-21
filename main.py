from dotenv import load_dotenv
import openai
import os
from colorama import Fore
import sys
import datetime
import streamlit as st
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    st.title("Humour AI")
    with st.form("user_form", clear_on_submit=True):
        user_input = st.text_input("Type Something...")
        submit_buttom = st.form_submit_button(label="Send")

    if submit_buttom:
        response = openai.chat.completions.create(

            model = 'gpt-3.5-turbo',
            messages = [

                {"role": "system", "content": "act extremely funny"},
                {"role": "user", "content" : user_input}
            ],
                    
            temperature=1
        )
        st.write(response.choices[0].message.content.strip())
        promptTokens = response.usage.prompt_tokens
        completionTokens = response.usage.completion_tokens
        totalTokens = response.usage.total_tokens
        print(Fore.GREEN + "A:", response.choices[0].message.content.strip(), Fore.RESET)
        print()
        print(Fore.LIGHTBLACK_EX + "Tokens Used for Prompt:", promptTokens)
        print("Tokens Used for Output:", completionTokens)
        print("Total Tokens Used:", totalTokens)
        cost = (0.0000015 * promptTokens) + (0.000002 * completionTokens)
        print("Total Money Spent: $" + str(cost))
        print(datetime.datetime.now())
    

    
