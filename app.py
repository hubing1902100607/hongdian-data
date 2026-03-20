import streamlit as st
import pandas as pd

# --- 1. 页面配置 ---
st.set_page_config(page_title="红点数据", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    header, footer { visibility: hidden; }
    .main-wrap { max-width: 1000px; margin: 0 auto; padding: 40px 20px; text-align: center; }
    .hero-badge {
        display: inline-block; background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        border: 1px solid rgba(255, 45, 85, 0.3); padding: 5px 15px;
        border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 25px;
    }
    .hero-title { font-size: 44px; font-weight: 800; line-height: 1.2; margin-bottom: 25px; }
    .hero-title span { color: #ff2d55; }
    .hero-subtitle { color: #80808b; font-size: 16px; margin-bottom: 60px; }
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 80px; }
    .feature-card { background: #111118; border: 1px solid #1e1e24; border-radius: 16px; padding: 30px 20px; text-align: left; }
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-bottom: 80px; }
    .price-card { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 40px 20px; position: relative; }
    .price-card.featured { border: 2px solid #ff2d55; }
    .price-val { font-size: 48px; font-weight: 800; margin: 20px 0; }
    .price-val span { font-size: 22px; }
    </style>
""", unsafe_allow_html=True)

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    # 1:1 还原 Landing Page
    st.markdown("""
    <div class="main-wrap">
        <div class="hero-badge">🔥 小红书爆款选品情报</div>
        <div class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></div>
        <div class="feature-grid">
            <div class="feature-card"><h4>💥 识别低粉高销爆款</h4><p>帮你找到粉丝少但销量高的黑马商品。</p></div>
            <div class="feature-card"><h4>📈 销量趋势一目了然</h4><p>每个商品都有周维度趋势图。</p></div>
            <div class="feature-card"><h4>🛒 加购信号预警</h4><p>24小时加购数据是销量的先行指标。</p></div>
        </div>
        <div class="price-grid">
            <div class="price-card"><div>月度版</div><div class="price-val"><span>¥</span>59.9</div></div>
            <div class="price-card featured"><div style="color:#ff2d55">季度版</div><div class="price-val"><span>¥</span>135</div></div>
            <div class="price-card"><div>年度版</div><div class="price-val"><span>¥</span>365</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        pwd = st.text_input("🔑 请输入激活码解锁数据", type="password")
        if pwd == "8888":
            st.session_state['authenticated'] = True
            st.rerun()
else:
    # --- 进入数据中心 ---
    st.markdown("### 📊 实时数据中心")
    
    # 针对你截图中的文件名进行精准读取
    # 自动识别是 .csv 还是 .xlsx
    target_file = "红点数据_导入模板.csv"
    
    try:
        df = pd.read_csv(target_file)
        st.dataframe(df, use_container_width=True, height=800)
    except FileNotFoundError:
        # 如果你上传的是 Excel 格式，尝试用 Excel 方式读取
        try:
            df = pd.read_excel("红点数据_导入模板.csv") # 有时候文件名叫csv其实是excel
            st.dataframe(df, use_container_width=True)
        except:
            st.error(f"未找到文件：{target_file}，请确保文件名完全一致（注意'板'和'板'的区别）。")
