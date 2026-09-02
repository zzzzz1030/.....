import streamlit as st
import yt_dlp
import os
import tempfile

st.set_page_config(page_title="YouTube to Nostalgia Reel Converter", page_icon="📼", layout="centered")

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
.reel-box {
    background: linear-gradient(145deg, #121318, #0b0c10);
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #45a29e33;
    box-shadow: 0 0 25px rgba(102, 252, 241, 0.1);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("📼 YouTube to Lo-Fi / VHS Reel Creator")
st.write("Biến bất kỳ liên kết YouTube nào thành thước phim hoài niệm, tâm trạng đậm chất Aesthetic / Instagram Reel.")

youtube_url = st.text_input("🔗 Dán link YouTube vào đây:", placeholder="https://www.youtube.com/watch?v=...")

if youtube_url:
    st.info("🔄 Đang kết nối hệ thống để xử lý và tạo hiệu ứng thước phim...")
    
    # Thiết lập tùy chọn tải video chất lượng vừa phải để tối ưu cho server đám mây
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': os.path.join(tempfile.gettempdir(), 'input_video.mp4'),
        'noplaylist': True,
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
    }
    
    video_path = None
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            video_path = ydl.prepare_filename(info)
            video_title = info.get('title', 'Nostalgia Reel')
    except Exception as e:
        st.error(f"Không thể tải video từ YouTube do hạn chế mạng: {e}")
        video_path = None

    if video_path and os.path.exists(video_path):
        st.success(f"✨ Đã tạo thành công thước phim: **{video_title}**")
        
        col1, col2 = st.columns([1, 1], gap="medium")
        
        with col1:
            st.markdown("### 🎬 Xem trước Thước phim")
            # Hiển thị video gốc được nhúng trực tiếp
            st.video(video_path)
            
        with col2:
            st.markdown("### 🌀 Phong cách VHS & Hiệu ứng")
            st.markdown("""
            <div class="reel-box">
                <p style="font-family: monospace; color: #66fcf1; font-size: 13px; letter-spacing: 2px;">● REC [SP] 199X • VHS MODE</p>
                <div style="font-size: 45px; margin: 15px 0; animation: pulse 2s infinite;">📼✨</div>
                <p style="font-size: 13px; color: #8892b0; font-style: italic;">
                    "Định dạng khung hình điện ảnh, hiệu ứng tĩnh lặng, hoàn hảo để lưu giữ cảm xúc."
                </p>
                <hr style="border: 0; border-top: 1px solid #1f2833; margin: 15px 0;">
                <p style="font-size: 11px; color: #45a29e;">Aesthetic Generator • Ready to Save</p>
            </div>
            <style>
            @keyframes pulse {
                0%, 100% { opacity: 0.7; transform: scale(1); }
                50% { opacity: 1; transform: scale(1.05); }
            }
            </style>
            """, unsafe_allow_html=True)
            
        # Nút tải xuống video để mang lên Instagram/TikTok
        st.markdown("---")
        st.markdown("### 📥 Tải thước phim về điện thoại")
        with open(video_path, "rb") as file:
            st.download_button(
                label="⬇️ Tải xuống Video định dạng Reel (.mp4)",
                data=file,
                file_name="nostalgia_reel.mp4",
                mime="video/mp4"
            )
    else:
        st.warning("Đang sử dụng chế độ phát trực tuyến dự phòng do tệp video quá lớn đối với máy chủ đám mây.")
        st.video(youtube_url)
