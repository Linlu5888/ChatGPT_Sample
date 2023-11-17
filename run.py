import openai

# 输入你的OpenAI API密钥
api_key = input('请输入你的API-Key：')
openai.api_key = api_key

def generate_response(user_input):
    prompt = 'The following is a conversation with an AI assistant. The assistant helps with various tasks. User: ' + user_input + ' AI:'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

if __name__ == '__main__':
    user_input = '这是一个测试'
    response = generate_response(user_input)
    print('ChatGPT：' + response)