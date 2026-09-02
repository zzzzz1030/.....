import streamlit as st
import re

st.set_page_config(page_title="Nostalgia YouTube Media Streamer", page_icon="📼", layout="centered")

st.markdown("""
<style>
.main {
    background-color: #0f1117;
    color: #ffffff;
}
.stTextInput input {
    background-color: #1e2229;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("📼 Nostalgic Audio & Visual Streamer")
st.write("Ứng dụng phát âm thanh và tái hiện không gian hình ảnh hoài niệm từ liên kết YouTube.")

youtube_url = st.text_input("🔗 Dán link YouTube vào đây:", placeholder="https://www.youtube.com/watch?v=...")

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

if youtube_url:
    video_id = extract_video_id(youtube_url)
    
    if video_id:
        st.success("Đã tải thành công liên kết không gian hoài niệm!")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("### 🎥 Trình phát YouTube")
            st.video(youtube_url)
            
        with col2:
            st.markdown("### 🌀 Không gian ảo ảnh hoài niệm")
            # Chèn hình ảnh mang phong cách không gian ảo ảnh/backrooms nghệ thuật
            st.image(
                "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80",
                caption="Không gian tĩnh lặng & hoài niệm",
                width="stretch"
            )
            st.markdown("""
            <div style="background: #1a1a2e; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #16213e; margin-top: 10px;">
                <p style="font-size: 12px; color: #a0a0a0;">Mỗi liên kết mang lại một chiều không gian âm thanh và thị giác riêng biệt.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Liên kết YouTube không hợp lệ. Vui lòng kiểm tra lại đường dẫn!")
