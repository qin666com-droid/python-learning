import streamlit as st
import os
from openai import OpenAI
from openai.resources.skills import content

#设置页面的配置项
st.set_page_config(
    page_title="AI伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI伴侣")
#logo
st.logo("🤖")

#系统提示词
system_prompt = "你是扶苏,优秀的道教子弟,同时也是我的AI助理"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天记录
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
#创建于AI大模型交互的客户端对象(DEEPSEEK_API_KEY
#  环境变量的名字,值就是deep seek的API_KEY)
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#输入框
prompt =  st.chat_input("请输入你的问题")
if prompt: # 字符串会自动转换为布尔值,如果字符串非空,则为True,否则为False
    st.chat_message("user").write(prompt)
    print("-----------> 调用AI大模型,提示词:", prompt)
#保持用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})
    #与AI大模型进行交互(参数)
    # print({"role": "system", "content": system_prompt}, st.session_state.messages)
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果(非流式输出的解析方式)
    # print("-----------> 大模型返回的结果:", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果(流式输出的解析方式)
    response_message = st.empty() # 创建空的容器,用于存储大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

#保持大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})


