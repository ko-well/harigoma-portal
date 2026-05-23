import streamlit as st

# --- ページ設定 ---
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

# 1. 【新登場】ゼロから育てる！志望動機作成アシスタント
with st.container(border=True):
    st.subheader("🌱 ゼロから育てる！志望動機作成アシスタント")
    st.write("AIが答えを出すのではなく，対話を通じてあなたの中にある本音や強みを引き出します。AIからの質問に答えながら，何度もやり取りを重ねて，もっとも納得できるあなただけの志望動機を少しずつ育てていきます。")
    # 先ほど完成したURLをバッチリ設定しています！
    st.link_button("👉 このアプリを開く", "https://harigoma-motivation.streamlit.app/")

st.write("") 

# 2. ポータブルスキル（強み）発見アプリ
with st.container(border=True):
    st.subheader("✨ 自己資源・強み発見アシスタント")
    st.write("「なんでもない」と思っている経験から，ビジネスで通用する立派な「強み」をAIと見つけ出します。自己PRのネタ探しや，自分の価値を再発見したい時におすすめです。")
    # ⚠️ 実際の強み発見アプリのURLが分かりましたら、ここを書き換えてください
    st.link_button("👉 このアプリを開く", "https://[強み発見アプリのURL]")

st.write("") 

# 3. 自己PR作成ステップ1：キャリアの棚卸し
with st.container(border=True):
    st.subheader("🛠️ 自己PR作成ステップ1：キャリアの棚卸し")
    st.write("ジョブカードの職務内容をコピペするだけで，AIが「役割・行動・結果」をきれいに整理します。AIからの優しい質問に答えるだけで，あなただけの『棚卸し完了シート（資料1）』が完成します。")
    st.link_button("👉 このアプリを開く", "https://harigoma-inventory.streamlit.app/")

st.write("") 

# 4. 自己PR作成ステップ2：キャリア・アンカー診断
with st.container(border=True):
    st.subheader("🧩 自己PR作成ステップ2：キャリア・アンカー診断 ＆ 設計")
    st.write("40の質問から，仕事で絶対に譲れない軸（キャリア・アンカー）を自動集計して特定します。ステップ1で集めた素材と組み合わせて，実際の就職活動で使える『自己PR設計図（資料2）』を作り上げます。")
    st.link_button("👉 このアプリを開く", "https://harigoma-anchor.streamlit.app/")

st.write("") 

# 5. 心のモヤモヤ解消・ストレスケアアシスタント
with st.container(border=True):
    st.subheader("💡 心のモヤモヤ解消・ストレスケアアシスタント")
    st.write("就職活動や仕事の中で感じるストレス，対人関係のモヤモヤした出来事を書き出すことで，AIがあなたの心に寄り添いながら，気持ちが軽くなる『新しい捉え方』を一緒に見つけます。AIとの対話で納得いくまで相談できます。")
    st.link_button("👉 このアプリを開く", "https://abcde-support-app.streamlit.app/")

st.markdown("---")
st.caption("© C.HARIGOMA Career Support")
