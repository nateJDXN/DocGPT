import openai
import requests
import docx2txt
from shutil import which
import os


def get_response(prompt, api_key):
    openai.api_key = api_key.strip()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful document parser that reads through a given file and answers questions about the text."},
        {"role": "user", "content": prompt}
        ], 
        max_tokens=200,
        n=1,
        temperature=0.5,
    )
    message = response.choices[0].message['content'].strip()
    return message


def main():

    api_key = open('data/key.txt', 'r').read()
    print(api_key)

    print("Hello! I am DocGPT, your document reading assistant!")
    print("Type 'quit' to exit the app")
    print()

    if api_key == "":
        print("ERR: No API key found")
        print("You can find your API key at: https://platform.openai.com/account/api-keys")
        api_key = input("Paste your key below:")
        open('data/key.txt', 'w').write(api_key)

        main()

    #convert document to input
    # doc_input = input("Paste the path of your document below")
    # document = os.path.exists(shutil.which(doc_input))
    # text = docx2txt.process()
    # open('data/text.txt', 'w').write(text)


    while True:
        user_input = input("Q: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = get_response(user_input, api_key)
        print("A:", response)


if __name__ == "__main__":
    main()