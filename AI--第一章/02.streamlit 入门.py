import streamlit as st

#设置页面的配置项
st.set_page_config(
    page_title="Streamlit",
    page_icon="🧊",
    layout="centered",
    #边框栏
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)





#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")


#段落文字
st.write("缅因猫（Maine Coon）是美国缅因州的原生品种，"
         "也是北美洲最早自然形成的长毛猫之一，被称为“温柔的巨人”。")

#图片
# st.image("./recources/worldcup.jpg")
st.image("recources/worldcup.jpg")

#音频
# st.audio()

#视频
# st.video()


#logo
st.logo("recources/worldcup.jpg")

#表格
students_data = {
    "name":["qq","ww","kk"],
    "age":[11,22,33]
}
st.table(students_data)


#输入框
name = st.text_input("请输入姓名")
st.write(name)

password = st.text_input("qing输入密码",type="password")
st.write(password)

#按钮
grnder = st.radio("anniu",[1,0])
st.write(grnder)


















