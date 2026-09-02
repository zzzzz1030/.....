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
    # Trích xuất Video ID từ các định dạng link YouTube khác nhau
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
            st.markdown("### 🌀 Không gian ảo ảnh")
            st.markdown("""
            <div style="background: #1a1a2e; padding: 25px; border-radius: 12px; text-align: center; border: 1px solid #16213e;">
                <p style="color: #e94560; font-weight: bold; font-size: 16px;">✨ Hiệu ứng thị giác hoài niệm</p>
                <div style="animation: pulse 2.5s infinite; font-size: 45px; margin: 10px 0;">👁️‍🗨️</div>
                <p style="font-size: 12px; color: #a0a0a0;">Tái hiện cảm giác không gian tĩnh lặng, âm thanh sâu lắng như video mẫu.</p>
            </div>
            <style>
            @keyframes pulse {
                0% { transform: scale(1); opacity: 0.8; }
                50% { transform: scale(1.08); opacity: 1; filter: drop-shadow(0 0 12px #e94560); }
                100% { transform: scale(1); opacity: 0.8; }
            }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.error("Liên kết YouTube không hợp lệ. Vui lòng kiểm tra lại đường dẫn!") 
        
