import streamlit as st
import os
from openai import OpenAI
import datetime
import json # json模块

from openai.resources.skills import content
from streamlit.runtime import script_data

#设置页面的配置项
st.set_page_config(
    page_title="AI伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 生成会话标识的函数
def generate_session_id():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


#保存会话信息的函数
def save_session():
    if st.session_state.current_session:
        # 构建新地会话对象
        session_data = {
            "nickname": st.session_state.nickname,
            "personality": st.session_state.personality,
            "messages": st.session_state.messages,
            "current_session": st.session_state.current_session,
        }
        # 如果 sessions 目录不存在,则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w",encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)


#加载所有的会话列表信息
def load_sessions():
    sessions_list = []
    #加载sessions目录下的所有json文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                sessions_list.append(filename[:-5])
    sessions_list.sort(reverse=True)
    return sessions_list


#加载指定的会话信息
def load_session(session_id):
     try:
         if os.path.exists(f"sessions/{session_id}.json"):
             # 读取会话数据
             with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                 session_data = json.load(f)
                 st.session_state.nickname = session_data["nickname"]
                 st.session_state.personality = session_data["personality"]
                 st.session_state.messages = session_data["messages"]
                 st.session_state.current_session = session_data["current_session"]
     except Exception:
        st.error("加载会话失败")

# 删除指定的会话文件
def delete_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")
            #如果删除的会话是当前会话,则需要更新消息记录
            if session_id == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.nickname = ""
                st.session_state.personality = ""
                st.session_state.current_session = generate_session_id()
    except Exception:
        st.error("删除会话失败")



#大标题
st.title("AI伴侣")
#logo
st.logo("🤖")

#系统提示词
system_prompt = "你是%s,性格是%s,你是一个智能伴侣,你可以回答用户的问题"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
#昵称
if "nickname" not in st.session_state:
    st.session_state.nickname = ""
#性格
if "personality" not in st.session_state:
    st.session_state.personality = ""

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_id()

#性格输入框


#展示聊天记录
st.text(f"会话名称:{st.session_state.current_session} ")
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


#左侧侧边栏,用于展示系统提示词
with st.sidebar:#上下文管理器
    #会话标识
    st.subheader("AI控制面板")

    #新建会话
    if st.button("新建会话",width="stretch",icon="🔄"):
        #1.保存当前会话信息
        save_session()
        #2.创建新的会话
        if st.session_state.messages: #如果聊天记录非空,True;否则,False
            st.session_state.messages = []
            st.session_state.nickname = ""
            st.session_state.personality = ""
            st.session_state.current_session = generate_session_id()
            st.rerun()  # 重新运行当前脚本,刷新页面


    #会话历史
    st.text("会话历史:")
    sessions_list = load_sessions()
    for session in sessions_list:
        col1,col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            #三元运算符: 如果条件为真,则执行第一个表达式的值;否则, 执行第二个表达式
            #          --> 语法: 值1 if 条件 else 值2
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()  # 重新运行当前脚本,刷新页面

        with col2:
            #删除会话
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                # 删除会话文件
                delete_session(session)
                st.rerun()

    #分割线
    st.divider()



    #伴侣信息
    st.subheader("伴侣信息")
    nickname = st.text_input("昵称",placeholder="请输入 昵称",key="nickname")
    #性格输入框
    personality = st.text_area("性格",placeholder="请输入性格",key="personality")




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
            {"role": "system", "content": system_prompt % (nickname, personality)},
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

# 保存当前会话信息
    save_session()
