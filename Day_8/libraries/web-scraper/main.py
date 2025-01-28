from web_scraper.content import ContentScraper
import os
from ollama import chat

def get_url():
    url = input('Enter the url of the website: ')
    return url

def chat_with_data(data):
    initial_prompt = data + """
            Use this above website data to understand its content and answer my queries based on it,
            do not use any markdowns and just output in plain text. For the first response, just let me know that
            you did understand the contents and you are ready to answer queries based on the content,
            and whenever the users used this or is refer to the topic of the website, answer in brief and keep the replies short and consice and again do no use markdowns
        """
    print('\n\nAi: ', end=' ')
    conversation_history = [{'role': 'user', 'content': initial_prompt}]
    stream = chat(
            model='llama3.2',
            messages=conversation_history,
            stream=True,
        )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    
    while True:
        user_input = input("\n\n\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat.")
            break
        user_input = data + user_input
        conversation_history.append({'role': 'user', 'content': user_input})
        print('\n\nAi: ', end=' ')
        stream = chat(
                model='llama3.2',
                messages = conversation_history,
                stream=True,
            )
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        conversation_history.append({'role': 'assistant', 'content': chunk['message']['content']})

def main():
    url = get_url()
    scraper = ContentScraper(url)
    scraper.fetch_content()
    scraper.parse_content()
    html = scraper.get_formated_html()

    file_location = os.path.abspath(__file__)[::-1].partition('\\')[-1][::-1]+'\\index.html'
    print(f"File location: {file_location}")

    with open(file_location, 'w', encoding='utf-8') as f:
        f.write(html)

    data = scraper.get_clean_text()
    # print(data)
    chat_with_data(data)


if __name__ == "__main__":
    main()