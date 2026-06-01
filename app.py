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
        margin-bottom: 3rem; /* 余白を広げてゆったりと */
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08); /* 影を少しリッチに */
        animation: fadeInDown 1s ease-out forwards; /* 上からフワッと降りてくるアニメーション */
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
        background: linear-gradient(to bottom, rgba(255,255,255,0.3), rgba(255,255,255,0.7)); /* グラデーションで下部を読みやすく */
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

# --- カスタムCSS（壁紙・アニメーション・明朝体） ---
st.markdown("""
<style>
/* 1. フォントの設定（游明朝） */
html, body, p, div, span, a, button, h1, h2, h3, h4, h5, h6 {
    font-family: 'Yu Mincho', '游明朝', 'YuMincho', 'Hiragino Mincho ProN', 'HGS明朝E', serif !important;
}

/* 2. ページ全体の壁紙（おすすめ：淡いグラデーション） */
.stApp {
    background: linear-gradient(135deg, #ffffff 0%, #f4f7f6 100%);
    background-attachment: fixed; /* スクロールしても背景を固定 */
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
    background-color: rgba(255, 255, 255, 0.85) !important; /* 壁紙から浮き立たせるための半透明の白 */
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    backdrop-filter: blur(10px); /* すりガラス効果で高級感を */
    border-radius: 12px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
    padding: 10px !important;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important; /* 滑らかな動き */
    
    /* 初期表示時の浮き上がりアニメーション */
    opacity: 0;
    animation: fadeInUp 0.8s ease-out forwards;
}
/* ホバー（マウスオーバー）時の動き */
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 12px 25px rgba(0,0,0,0.1) !important;
    background-color: rgba(255, 255, 255, 1) !important;
}

/* カードのアニメーションのタイミングを少しずつずらす（順番に現れる効果） */
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(1) { animation-delay: 0.1s; }
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(2) { animation-delay: 0.2s; }
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(3) { animation-delay: 0.3s; }
[data-testid="stVerticalBlockBorderWrapper"]:nth-child(4) { animation-delay: 0.4s; }


/* ヘッダーテキスト */
.header-title { 
    font-size: 2.8rem; 
    font-weight: 700; 
    color: #1a202c; 
    letter-spacing: 0.05em; 
    text-shadow: 0px 2px 4px rgba(255,255,255,1); 
}
.header-subtitle { 
    font-size: 1.25rem; 
    color: #2d3748; 
    margin-top: 1.2rem; 
    line-height: 1.8; 
    font-weight: 600;
    text-shadow: 0px 2px 4px rgba(255,255,255,1); 
}

/* カテゴリ見出し */
.category-header {
    border-left: 5px solid #2980B9;
    padding-left: 15px;
    margin-top: 4rem;
    margin-bottom: 2rem;
    font-size: 1.6rem;
    font-weight: 600;
    color: #2c3e50;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 10px;
    opacity: 0;
    animation: fadeInUp 0.8s ease-out forwards;
}

/* ボタンのデザイン */
[data-testid="stLinkButton"] {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
}
[data-testid="stLinkButton"] a,
[data-testid="stLinkButton"] button {
    background-color: #2c3e50 !important; /* 少しシックなネイビーに変更 */
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 2.5rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    letter-spacing: 0.05em;
}
[data-testid="stLinkButton"] a *,
[data-testid="stLinkButton"] button * {
    color: #ffffff !important;
}
[data-testid="stLinkButton"] a:hover,
[data-testid="stLinkButton"] button:hover {
    background-color: #34495e !important;
    box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
    transform: translateY(-2px);
}

/* テキスト色調整 */
h3 { color: #2d3748 !important; }
p { font-size: 1.05rem; color: #4a5568; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)

# --- トップ画面ヘッダー ---
st.markdown('''
<div class="header-box">
    <div class="header-overlay"></div>
    <div class="header-content">
        <div class="header-title">C.HARIGOMA キャリア支援ポータル</div>
        <div class="header-subtitle">新潟でキャリアを切り拓くあなたへ。<br>自己理解から応募書類の作成、メンタルケアまでを一貫してサポートする統合プラットフォームです。</div>
    </div>
</div>
''', unsafe_allow_html=True)

# ==================================================
# 【応募書類関連】
# ==================================================
st.markdown('<div class="category-header">【応募書類関連】</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("📝 志望動機添削アシスタント")
        st.write("ご自身で書いた志望動機を、求人情報と照らし合わせてプロの視点で添削・ブラッシュアップします。")
        st.link_button("アプリを開く", "https://career-shibou-app.streamlit.app/")
with col2:
    with st.container(border=True):
        st.subheader("🌱 ゼロから育てる！志望動機作成アシスタント")
        st.write("AIとの対話を通じてあなたの中にある強みを引き出し、納得のいく志望動機をゼロから一緒に作ります。")
        st.link_button("アプリを開く", "https://harigoma-motivation.streamlit.app/")

col3, col4 = st.columns(2)
with col3:
    with st.container(border=True):
        st.subheader("🛠️ 自己PR作成ステップ1：キャリアの棚卸し")
        st.write("職務経歴から「役割・行動・結果」を整理し、自己PRの基礎となる素材（棚卸しシート）を作ります。")
        st.link_button("アプリを開く", "https://harigoma-inventory.streamlit.app/")
with col4:
    with st.container(border=True):
        st.subheader("🧩 自己PR作成ステップ2：キャリア・アンカー診断 ＆ 設計")
        st.write("40の質問から仕事の軸を特定し、ステップ1の素材と組み合わせて自己PRを完成させます。")
        st.link_button("アプリを開く", "https://harigoma-anchor.streamlit.app/")


# ==================================================
# 【自己理解・仕事理解関連】
# ==================================================
st.markdown('<div class="category-header">【自己理解・仕事理解関連】</div>', unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    with st.container(border=True):
        st.subheader("✨ 自己資源・強み発見アシスタント")
        st.write("これまでの何気ない経験から、ビジネスで通用する「強み」や「ポータブルスキル」を見つけ出します。")
        st.link_button("アプリを開く", "https://skills-translation-app.streamlit.app/")
with col6:
    with st.container(border=True):
        st.subheader("🧩 自己理解から仕事理解へ：わたしに合う働き方発見アシスタント")
        st.write("職種名の先入観を外し、あなたが本当に安心できる働き方（環境）をAIと一緒に見つけます。")
        st.link_button("アプリを開く", "https://harigoma-job-style.streamlit.app/")


# ==================================================
# 【メンタル】
# ==================================================
st.markdown('<div class="category-header">【メンタル】</div>', unsafe_allow_html=True)

col7, col8 = st.columns(2)
with col7:
    with st.container(border=True):
        st.subheader("💡 心のモヤモヤ解消・ストレスケアアシスタント")
        st.write("就活や仕事でのストレスを吐き出し、気持ちが軽くなる「新しい捉え方」を一緒に見つけます。")
        st.link_button("アプリを開く", "https://abcde-support-app.streamlit.app/")

with col8:
    st.write("") 

st.markdown("---")
st.caption("© C.HARIGOMA Career Support")
