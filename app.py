import streamlit as st
import os

# إعدادات الصفحة
st.set_page_config(page_title="بوابة الراوي التعليمية", layout="wide")

# العنوان الرئيسي والشعار
st.title("📚 منصة الراوي التعليمية")
st.subheader("بوابة الطلاب للمحاضرات والمواد الدراسية")
st.markdown("---")

# ==========================================
# 1. قسم الفيديو (الجديد)
# ==========================================
st.header("📺 فيديو توضيحي")

# عرض الفيديو الجديد في منتصف الصفحة
st.video("https://www.youtube.com/watch?v=abdlUuObWhA")

st.markdown("---")

# ==========================================
# 2. قسم الموقع الإلكتروني
# ==========================================
st.header("🌐 موقعنا الإلكتروني")

st.info("💡 لمزيد من المعلومات والشروحات التفصيلية، ندعوكم لزيارة موقعنا الرسمي.")

# زر أنيق للانتقال للموقع
st.link_button("زيارة موقع alrawitrucks.nl 🚛", "https://alrawitrucks.nl/")

st.markdown("---")

# ==========================================
# 3. قسم تحميل الملفات (PDF)
# ==========================================
st.header("📂 تحميل المواد الدراسية (PDF)")

# دالة التعامل مع الملفات
folder_path = "files"

if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    # تصفية الملفات لإظهار PDF فقط
    pdf_files = [f for f in files if f.endswith('.pdf')]
    
    if len(pdf_files) == 0:
        st.warning("لا توجد ملفات PDF حالياً في مجلد files.")
    else:
        st.write(f"المواد المتاحة للتحميل ({len(pdf_files)} ملف):")
        
        # عرض الملفات
        for filename in pdf_files:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as f:
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.write(f"📄 **{filename}**")
                with col2:
                    st.download_button(
                        label="📥 تحميل",
                        data=f,
                        file_name=filename,
                        mime="application/pdf",
                        key=filename
                    )
            st.divider() # خط فاصل خفيف بين الملفات
else:
    st.error("⚠️ مجلد 'files' غير موجود! الرجاء إنشاؤه ووضع الملفات داخله.")

# تذييل الصفحة
st.caption("© 2025 Alrawi Trucks - جميع الحقوق محفوظة")
