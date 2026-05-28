import streamlit as st

# --- ページ設定 ---
st.set_page_config(page_title="C.HARIGOMA キャリア支援ポータル", layout="wide")

# --- カスタムCSS（大人向け・プロフェッショナルデザイン） ---
st.markdown("""
<style>
/* 全体のカラースキームとフォント */
:root {
    --primary: #1F2937; /* 深いネイビーグレー */
    --secondary: #3B82F6; /* 落ち着いたブルー */
    --bg-gray: #F9FAFB;
}
h1, h2, h3 { color: var(--primary) !important; font-family: 'Helvetica Neue', Arial, sans-serif; }

/* ヘッダーデザイン */
.header-box {
    text-align: center;
    padding: 3rem 1rem;
    background: linear-gradient(to bottom, #ffffff, #f3f4f6);
    border-bottom: 1px solid #e5e7eb;
    margin-bottom: 2rem;
}
.header-title { font-size: 2.2rem; font-weight: 700; color: #111827; letter-spacing: 0.05em; }
.header-subtitle { font-size: 1.1rem; color: #4B5563; margin-top: 1rem; line-height: 1.6; }

/* カテゴリ見出し */
.category-header {
    border-left: 6px solid #3B82F6;
    padding-left: 15px;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    font-size: 1.4rem;
    font-weight: 600;
    color: #1F2937;
    background-color: #F3F4F6;
    padding-top: 10px;
    padding-bottom: 10px;
}

/* ボタンの大人なデザイン化 */
[data-testid="stLinkButton"] {
    display: flex;
    justify-content: flex-end;
    margin-top: 10px;
}
[data-testid="stLinkButton"] a {
    background-color: #1F2937 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.5rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    transition: background-color 0.3s ease;
    text-align: center;
}
[data-testid="stLinkButton"] a:hover {
    background-color: #374151 !important;
}

/* コンテナ内のテキスト調整 */
p { font-size: 0.95rem; color: #4B5563; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# --- トップ画面ヘッダー ---
st.markdown('''
<div class="header-box">
    <div class="header-title">C.HARIGOMA キャリア支援ポータル</div>
    <div class="header-subtitle">新潟でキャリアを切り拓くあなたへ。<br>自己理解から応募書類の作成、メンタルケアまでを一貫してサポートする統合プラットフォームです。</div>
</div>
''', unsafe_allow_html=True)

# --- 画像の表示 ---
# ※GitHubに「万代橋　桜.jpg」をアップロードすると自動で表示されます。
try:
    st.image("万代橋　桜.jpg", use_container_width=True, caption="新潟市の風景（万代橋と桜）")
except:
    st.info("※ここに「万代橋　桜.jpg」が表示されます。（GitHubに画像をアップロードしてください）")


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


# ==================================================
# 【自己理解・仕事理解関連】
# ==================================================
st.markdown('<div class="category-header">【自己理解・仕事理解関連】</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    with st.container(border=True):
        st.subheader("✨ 自己資源・強み発見アシスタント")
        st.write("これまでの何気ない経験から、ビジネスで通用する「強み」や「ポータブルスキル」を見つけ出します。")
        st.link_button("アプリを開く", "https://skills-translation-app.streamlit.app/")
with col4:
    with st.container(border=True):
        st.subheader("🛠️ 自己PR作成ステップ1：キャリアの棚卸し")
        st.write("職務経歴から「役割・行動・結果」を整理し、自己PRの基礎となる素材（棚卸しシート）を作ります。")
        st.link_button("アプリを開く", "https://harigoma-inventory.streamlit.app/")

col5, col6 = st.columns(2)
with col5:
    with st.container(border=True):
        st.subheader("🧩 自己PR作成ステップ2：キャリア・アンカー診断 ＆ 設計")
        st.write("40の質問から仕事の軸を特定し、ステップ1の素材と組み合わせて自己PRを完成させます。")
        st.link_button("アプリを開く", "https://harigoma-anchor.streamlit.app/")
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

# レイアウト調整用の空カラム
with col8:
    st.write("") 

st.markdown("---")
st.caption("© C.HARIGOMA Career Support")
