import streamlit as st
import re

st.set_page_config(page_title="Nostalgia Ambient Streamer", page_icon="📼", layout="centered")

# CSS tạo phong cách giao diện tối, hoài niệm, viền sáng nghệ thuật giống phong cách Reel lo-fi
st.markdown("""
<style>
.main {
    background-color: #0b0c10;
    color: #c5c6c7;
}
.stTextInput input {
    background-color: #1f2833;
    color: #66fcf1;
    border: 1px solid #45a29e;
    border-radius: 8px;
}
.vhs-container {
    background: linear-gradient(145deg, #121318, #0b0c10);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #45a29e33;
    box-shadow: 0 0 25px rgba(102, 252, 241, 0.08);
    text-align: center;
}
.ambient-title {
    font-family: monospace;
    letter-spacing: 2px;
    color: #66fcf1;
    text-transform: uppercase;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("📼 Lo-Fi & Nostalgia Ambient Streamer")
st.write("Tái hiện không gian thước phim hoài niệm, âm thanh tĩnh lặng và cảm xúc sâu lắng.")

youtube_url = st.text_input("🔗 Dán link YouTube / Nhạc lo-fi vào đây:", placeholder="https://www.youtube.com/watch?v=...")

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

if youtube_url:
    video_id = extract_video_id(youtube_url)
    
    if video_id:
        st.success("Đã kết nối tầng không gian hoài niệm thành công!")
        
        # Bố cục giao diện gọn gàng, đậm chất thẩm mỹ lo-fi/reel
        col1, col2 = st.columns([1, 1], gap="medium")
        
        with col1:
            st.markdown("### 🎬 Khung hình phát")
            # Hiển thị video YouTube trực tiếp
            st.video(youtube_url)
            
        with col2:
            st.markdown("### 🌀 Trạng thái VHS Analog")
            st.markdown("""
            <div class="vhs-container">
                <p class="ambient-title">● REC [SP] 199X</p>
                <div style="font-size: 50px; margin: 15px 0; animation: float 3s ease-in-out infinite;">📼</div>
                <p style="font-size: 13px; color: #8892b0; font-style: italic;">
                    "Đưa tâm trí trở về những ký ức cũ kỹ, nơi thời gian trôi chậm lại qua từng khung ảnh lo-fi."
                </p>
                <hr style="border: 0; border-top: 1px solid #1f2833; margin: 15px 0;">
                <p style="font-size: 11px; color: #45a29e;">Aesthetic Vibes • Ambient Audio</p>
            </div>
            <style>
            @keyframes float {
                0%, 100% { transform: translateY(0); filter: drop-shadow(0 0 5px rgba(102, 252, 241, 0.3)); }
                50% { transform: translateY(-6px); filter: drop-shadow(0 0 15px rgba(102, 252, 241, 0.6)); }
            }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.error("Đường dẫn không hợp lệ. Vui lòng kiểm tra lại link YouTube!")
