# promptapp.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OpenAI_API_Key")
print(openai_api_key)

client = OpenAI(api_key=openai_api_key)


def gen_resp(user_input):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a helpful assistant.
             You know a lot.
             """,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )
    return response.choices[0].message.content


def main():
    print("Welcome to ai-chatbot! (Type 'exit' to quit), enter your queries")
    while True:
        user_input_prompt = input("Ask here: ")
        if user_input_prompt.lower() == "exit":
            print("ai-chatbot: Thank you - bye bye! Have a great day.")
            break
        response = gen_resp(user_input_prompt)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()

