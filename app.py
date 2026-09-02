import streamlit as st
import yt_dlp

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
st.write("Ứng dụng trích xuất âm thanh và tái hiện không gian hình ảnh hoài niệm từ liên kết YouTube.")

youtube_url = st.text_input("🔗 Dán link YouTube vào đây:", placeholder="https://www.youtube.com/watch?v=...")

@st.cache_data
def get_youtube_media(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('url'), info.get('title'), info.get('thumbnail')
    except Exception as e:
        return None, str(e), None

if youtube_url:
    with st.spinner("Đang kết nối và phân tích luồng dữ liệu..."):
        audio_url, title, thumbnail = get_youtube_media(youtube_url)
        
    if audio_url and "http" in str(audio_url):
        st.success(f"Đang phát: **{title}**")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if thumbnail:
                st.image(thumbnail, caption="Ảnh bìa gốc", width=300)
        with col2:
            st.markdown("### 🌀 Không gian ảo ảnh")
            st.markdown("""
            <div style="background: #1a1a2e; padding: 25px; border-radius: 12px; text-align: center; border: 1px solid #16213e;">
                <p style="color: #e94560; font-weight: bold; font-size: 16px;">✨ Hiệu ứng thị giác hoài niệm</p>
                <div style="animation: pulse 2.5s infinite; font-size: 45px; margin: 10px 0;">👁️‍🗨️</div>
                <p style="font-size: 12px; color: #a0a0a0;">Tái hiện cảm giác không gian tĩnh lặng, âm thanh sâu lắng.</p>
            </div>
            <style>
            @keyframes pulse {
                0% { transform: scale(1); opacity: 0.8; }
                50% { transform: scale(1.08); opacity: 1; filter: drop-shadow(0 0 12px #e94560); }
                100% { transform: scale(1); opacity: 0.8; }
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.audio(audio_url, format='audio/mp3')
    else:
        st.error(f"Không thể xử lý liên kết này do hạn chế từ YouTube trên máy chủ đám mây. Chi tiết lỗi: {title}")
