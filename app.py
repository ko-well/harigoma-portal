import streamlit as st

# --- ページ設定 ---
# ページ全体を広く使い，タイトルを設定します
st.set_page_config(page_title="C.HARIGOMA キャリア支援ポータル", layout="centered")

# --- カスタムデザイン（CSS） ---
st.markdown("""
<style>
/* 全体の文字色や見出しの調整 */
h1, h2, h3 { color: #2C3E50 !important; }
/* ボタンのデザイン強化 */
[data-testid="stLinkButton"] { display: flex; justify-content: center; }
[data-testid="stLinkButton"] a { background-color: #3498DB !important; color: white !important; font-size: 18px !important; font-weight: bold !important; padding: 10px 30px !important; border-radius: 8px !important; text-decoration: none !important; width: 100%; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease; }
[data-testid="stLinkButton"] a:hover { background-color: #2980B9 !important; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transform: translateY(2px); }
/* ヘッダー部分の背景 */
.header-box { background-color: #EBF5FB; padding: 20px; border-radius: 10px; margin-bottom: 30px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- トップ画面ヘッダー ---
st.markdown("""
<div class="header-box">
    <h1 style='margin-bottom: 0;'>🚪 キャリア支援ポータル</h1>
    <p style='font-size: 18px; color: #555; margin-top: 10px;'>
        ご自身のペースで，就職活動や自己理解を進めるためのサポートツール集です。<br>
        はじめての方でも使いやすいように設計されています。目的に合わせてご活用ください。
    </p>
</div>
""", unsafe_allow_html=True)

# --- アプリ一覧（カード型デザイン） ---

# 1. 志望動機添削アプリ（枠線で囲んでカードのように見せます）
with st.container(border=True):
    st.subheader("📝 志望動機添削アシスタント")
    st.write("求人情報とあなたの経験を照らし合わせ，プロの視点で志望動機をブラッシュアップします。応募書類の作成に迷ったり，より説得力のある文章に仕上げたい時に活用してください。（※ゼロからの作成もサポートします）")
    # ↓取得済みのURLに書き換えてください
    st.link_button("👉 このアプリを開く", "https://[志望動機アプリのURL]")

st.write("") # 少し隙間を空ける

# 2. ポータブルスキル（強み）発見アプリ
with st.container(border=True):
    st.subheader("🌱 自己資源・強み発見アシスタント")
    st.write("「なんでもない」と思っている経験から，ビジネスで通用する立派な「強み」をAIと見つけ出します。自己PRのネタ探しや，自分の価値を再発見したい時におすすめです。")
    # ↓取得済みのURLに書き換えてください
    st.link_button("👉 このアプリを開く", "https://[強み発見アプリのURL]")

st.write("") 

# 3. ABCDE理論アプリ
with st.container(border=True):
    st.subheader("💡 思考の変換サポート（ABCDE理論）")
    st.write("モヤモヤする出来事やネガティブな感情を整理し，客観的な視点で「合理的な思考」へと変換するサポートを行います。面接前の不安解消や，日々のストレスケアにご活用ください。")
    st.link_button("👉 このアプリを開く", "https://abcde-support-app.streamlit.app/")

st.markdown("---")
st.caption("© C.HARIGOMA Career Support")
