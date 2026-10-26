import streamlit as st
import os
from openai import OpenAI


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
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("-----------> 大模型返回的结果:", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
#保持大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})


