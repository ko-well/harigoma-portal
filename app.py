import streamlit as st
import base64
import os

# --- ページ設定（正しい関数名に修正しました） ---
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
    background-color: #FCFAFA; 
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E");
    background-attachment: fixed;
}

/* 3. アニメーションの定義 */
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
    opacity: 0;
    animation: fadeInUp 0.8s ease-out forwards;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 12px 25px rgba(0,0,0,0.08) !important;
    background-color: rgba(255, 255, 255, 1) !important;
}

/* ヘッダーテキスト */
.header-title { 
    font-size: 2.8rem; 
    font-weight: 700; 
    color: #3D2D2E; 
    letter-spacing: 0.05em; 
    text-shadow: 0px 2px 4px rgba(255,255,255,1); 
}
.header-subtitle { 
    font-size: 1.25rem; 
    color: #5C4B4D; 
    margin-top: 1.2rem; 
    line-height: 1.8; 
    font-weight: 600;
    text-shadow: 0px 2px 4px rgba(255,255,255,1); 
}

/* カテゴリ見出し */
.category-header {
    border-left: 5px solid #DB90A0; 
    padding-left: 15px;
    margin-top: 4rem;
    margin-bottom: 2rem;
    font-size: 1.6rem;
    font-weight: 600;
    color: #4A3B3D;
    border-bottom: 1px solid #EAE1E3;
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
    background-color: #DB90A0 !important; 
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 2.5rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(219, 144, 160, 0.2) !important; 
    letter-spacing: 0.05em;
}
[data-testid="stLinkButton"] a *,
[data-testid="stLinkButton"] button * {
    color: #ffffff !important;
}
[data-testid="stLinkButton"] a:hover,
[data-testid="stLinkButton"] button:hover {
    background-color: #C27082 !important; 
    box-shadow: 0 6px 12px rgba(194, 112, 130, 0.3) !important;
    transform: translateY(-3px); 
}

/* テキスト色調整 */
h3 { color: #4A3B3D !important; }
p { font-size: 1.05rem; color: #5C4B4D; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)

# --- トップ画面ヘッダー ---
st.markdown('''
<div class="header-box">
    <div class="header-overlay"></div>
    <div class="header-content">
        <div class="header-title">C.HARIGOMA キャリア支援ポータル</div>
        <div class="header-subtitle">新潟でキャリアを切り拓くあなたへ。<br>自己理解から応募書類の作成、面接対策、メンタルケアまでを一貫してサポートする統合プラットフォームです。</div>
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
# 【面接対策関連】
# ==================================================
st.markdown('<div class="category-header">【面接対策関連】</div>', unsafe_allow_html=True)

col9, col10 = st.columns(2)
with col9:
    with st.container(border=True):
        st.subheader("🗣️ AI面接練習アシスタント")
        st.write("面接官のタイプや特訓したいテーマに合わせ、スマートフォンやPCのマイクを使って本番さながらの音声面接練習を行います。")
        st.link_button("アプリを開く", "https://harigoma-interview-app.streamlit.app/")
with col10:
    st.write("") 


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
