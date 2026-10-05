
import streamlit as st
 
# 頁面設定
st.set_page_config(page_title="課程回饋表單", page_icon="📝", layout="centered")
 
st.title("課程回饋表單")
st.write("請花一分鐘填寫，您的意見能幫助我們把課程做得更好。")
 
 
# 統一的大字標題，避免每個欄位重複寫 HTML
def field_label(text):
    st.markdown(
        f"<span style='font-size:1.4em; font-weight:600;'>{text}</span>",
        unsafe_allow_html=True,
    )
 
 
# 課程清單（請依實際開課內容修改）
COURSES = [
    "程式設計（一）",
    "資料結構",
    "演算法",
    "計算機組織",
    "電子學",
    "數位邏輯設計",
    "其他",
]
 
# 課程特色標籤
POSITIVE_TAGS = ["授課認真", "準時下課", "互動性佳", "內容實用"]
NEGATIVE_TAGS = ["設備不佳", "缺乏實作", "進度緊湊"]
 
# 使用 st.form 讓所有欄位在按下送出後才一起提交
with st.form("feedback_form", clear_on_submit=False):
    # 1. 姓名
    field_label("姓名")
    name = st.text_input("姓名", placeholder="請輸入您的姓名", label_visibility="collapsed")
 
    # 學號
    field_label("學號")
    student_id = st.text_input("學號", placeholder="請輸入您的學號", label_visibility="collapsed")
 
    # 2. 科系
    field_label("科系")
    department = st.selectbox(
        "科系",
        ["資訊工程系", "電子工程系", "其他"],
        label_visibility="collapsed",
    )
 
    # 課程名稱（預設不選，強制使用者自己挑）
    field_label("課程名稱")
    course = st.selectbox(
        "課程名稱",
        COURSES,
        index=None,
        placeholder="請選擇您要回饋的課程",
        label_visibility="collapsed",
    )
 
    # 3. 課程滿意度（1~5 分）
    field_label("課程滿意度（1 = 非常不滿意，5 = 非常滿意）")
    satisfaction = st.slider(
        "課程滿意度",
        min_value=1,
        max_value=5,
        value=3,
        step=1,
        label_visibility="collapsed",
    )
 
    # 課程特色（可複選）
    field_label("這門課的特色（可複選）")
    st.caption("👍 優點")
    pos_cols = st.columns(len(POSITIVE_TAGS))
    positive_selected = [
        tag for col, tag in zip(pos_cols, POSITIVE_TAGS) if col.checkbox(tag, key=f"pos_{tag}")
    ]
    st.caption("👎 待改進")
    neg_cols = st.columns(len(POSITIVE_TAGS))  # 用相同欄數讓兩列對齊
    negative_selected = [
        tag for col, tag in zip(neg_cols, NEGATIVE_TAGS) if col.checkbox(tag, key=f"neg_{tag}")
    ]
 
    # 4. 意見回饋（拆成兩題，並以淺色範例引導）
    field_label("這門課最有幫助的部分")
    helpful = st.text_area(
        "最有幫助的部分",
        placeholder="例如：老師用實際專案講解迴圈與函式，讓我第一次寫出能動的小程式。",
        height=120,
        label_visibility="collapsed",
    )
 
    field_label("最希望改進的地方")
    improve = st.text_area(
        "最希望改進的地方",
        placeholder="例如：第 8 週後進度太快，希望遞迴的部分能多一堂課練習，或提供課後範例程式碼。",
        height=120,
        label_visibility="collapsed",
    )
 
    # 5. 送出按鈕
    submitted = st.form_submit_button("送出")
 
# 6. 送出後檢查並顯示感謝訊息
if submitted:
    errors = []
    if not name.strip():
        errors.append("姓名")
    if course is None:
        errors.append("課程名稱")
 
    if errors:
        st.warning(f"請先填寫：{'、'.join(errors)}")
    else:
        st.success("感謝您的回饋！")
 
        tags = positive_selected + negative_selected
 
        # 顯示填寫內容摘要（可視需要刪除）
        with st.expander("查看您填寫的內容"):
            st.write(f"**姓名：** {name}")
            st.write(f"**學號：** {student_id if student_id.strip() else '（未填寫）'}")
            st.write(f"**科系：** {department}")
            st.write(f"**課程名稱：** {course}")
            st.write(f"**課程滿意度：** {'⭐' * satisfaction}（{satisfaction} 分）")
            st.write(f"**課程特色：** {'、'.join(tags) if tags else '（未選擇）'}")
            st.write(f"**最有幫助的部分：** {helpful if helpful.strip() else '（未填寫）'}")
            st.write(f"**最希望改進的地方：** {improve if improve.strip() else '（未填寫）'}")