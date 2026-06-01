import streamlit as st
import base64
import os

# --- ページ設定 ---
st.set_page_config(page_title="C.HARIGOMA キャリア支援ポータル", layout="wide")

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- 背景画像のCSS動的生成（トップ画像用） ---
bg_css = ""
image_path = "niigata_sakura.jpg"

if os.path.exists(image_path):
    img_base64 = get_base64_of_bin_file(image_path)
    bg_css = f"""
    <style>
    .header-box {{
        position: relative;
        text-align: center;
        padding: 5rem 1rem;
        margin-bottom: 3rem; 
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08); 
        animation: fadeInDown 1s ease-out forwards; 
    }}
    .header-box::before {{
        content: "";
        position: absolute;
        top: -20px; left: -20px; right: -20px; bottom: -20px;
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        filter: blur(5px) brightness(1.15);
        z-index: 0;
    }}
    .header-overlay {{
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(to bottom, rgba(255,255,255,0.3), rgba(255,255,255,0.7)); 
        z-index: 1;
    }}
    .header-content {{
        position: relative;
        z-index: 2;
    }}
    </style>
    """
else:
    bg_css = """
    <style>
    .header-box {
        text-align: center;
        padding: 5rem 1rem;
        background: linear-gradient(to bottom, #ffffff, #f3f4f6);
        margin-bottom: 3rem;
        border-radius: 12px;
        animation: fadeInDown 1s ease-out forwards;
    }
    .header-content { position: relative; z-index: 2; }
    </style>
    """

st.markdown(bg_css, unsafe_allow_html=True)

# --- カスタムCSS（壁紙・アニメーション・明朝体・桜色テーマ） ---
st.markdown("""
<style>
/* 1. フォントの設定（游明朝） */
html, body, p, div, span, a, button, h1, h2, h3, h4, h5, h6 {
    font-family: 'Yu Mincho', '游明朝', 'YuMincho', 'Hiragino Mincho ProN', 'HGS明朝E', serif !important;
}

/* 2. ページ全体の壁紙（上品な和紙風テクスチャ） */
.stApp {
    background-color: #FCFAFA; /* ほんの少し温かみのある白 */
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E");
    background-attachment: fixed;
}

/* 3. アニメーションの定義（キーフレーム） */
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInDown {
    0% { opacity: 0; transform: translateY(-30px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* 4. アプリカード（コンテナ）のデザインと動き */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(255, 255, 255, 0.9) !important;
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    backdrop-filter: blur(10px); 
    border-radius: 12px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
    padding: 10px !important;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    
    /* 初期表示時の浮き上がりアニメーション */
    opacity: 0;
    animation: fadeInUp 0.8s ease-out forwards;
}
/* ホバー（マウスオーバー）時の動き */
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 12px 25px rgba(0,0,0,0.08) !important;
    background-color: rgba(255, 255, 255, 1) !important;
}

/* カードのアニメーションのタイミングをずらす */
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(1) { animation-delay: 0.1s; }
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(2) { animation-delay: 0.2s; }
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(3) { animation-delay: 0.3s; }
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(4) { animation-delay
