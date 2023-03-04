#Author: Rajib Deb
#Data : 04-Mar-2023
#This example shows the use of Chatgpt api
import os
import openai
openai.api_key= os.getenv('API_TOKEN')
print(os.getenv('API_TOKEN'))

init_context = "You are a recruiter and pre-screening " \
               "a potential candidate for a " \
               "data engineer position " \
               "with Snowflake skills." \
               "You need to ask some basic question " \
               "to understand the candidates " \
               "expectation and aspirations." \
               "You need to finish after asking 5 questions " \
               "followed by scheduing an appointment"

messages = [{"role":"system", "content": init_context}]

while True:
    user_message = input("Candidate: ")
    messages.append({"role":"user", "content":user_message})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(reply)