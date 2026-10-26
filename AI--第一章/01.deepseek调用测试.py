# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#创建于AI大模型交互的客户端对象(DEEPSEEK_API_KEY
#  环境变量的名字,值就是deep seek的API_KEY)
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#与AI大模型进行交互(参数)
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是扶苏,优秀的道教子弟,同时也是我的AI助理"},
        {"role": "user", "content": "算下今天的风水"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

#输出大模型返回的结果
print(response.choices[0].message.content)



