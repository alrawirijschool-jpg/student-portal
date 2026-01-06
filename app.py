import streamlit as st
import os

# إعدادات الصفحة
st.set_page_config(page_title="بوابة الطلاب التعليمية", layout="wide")

# العنوان الرئيسي
st.title("📚 منصة الرواي التعليمية")
st.subheader("دروس ومحاضرات لطلاب النقل الثقيل")
st.markdown("---")

# ==========================================
# قسم الفيديوهات (YouTube)
# ==========================================
st.header("📺 المحاضرات المرئية")

col1, col2 = st.columns(2)

with col1:
    st.info("📌 الدرس الأول: مقدمة في القيادة")
    # ضع رابط الفيديو الخاص بك هنا
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

with col2:
    st.info("📌 الدرس الثاني: تعليمات السلامة")
    # ضع رابط فيديو آخر هنا
    st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_LINK")

st.markdown("---")

# ==========================================
# قسم تحميل الملفات (PDF)
# ==========================================
st.header("📂 تحميل المواد الدراسية (PDF)")

# دالة لقراءة ملف PDF لكي يتم تحميله
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return data

# التأكد من وجود مجلد الملفات
folder_path = "files"

if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    
    if len(files) == 0:
        st.warning("لا توجد ملفات حالياً.")
    else:
        # عرض الملفات في شكل شبكة
        for filename in files:
            if filename.endswith(".pdf"):
                file_path = os.path.join(folder_path, filename)
                
                # إنشاء زر التحميل
                with open(file_path, "rb") as f:
                    btn = st.download_button(
                        label=f"📥 تحميل: {filename}",
                        data=f,
                        file_name=filename,
                        mime="application/pdf"
                    )
else:
    st.error("مجلد الملفات 'files' غير موجود!")

# تذييل الصفحة
st.markdown("---")
st.caption("© 2025 جميع الحقوق محفوظة - مركز الراوي للتدريب")