import streamlit as st
import pandas as pd

# --- 1. 基础配置 ---
st.set_page_config(page_title="红点数据", layout="wide", initial_sidebar_state="collapsed")

# --- 2. 暴力破解 Streamlit 布局限制 ---
st.markdown("""
    <style>
    /* 彻底抹除所有默认内边距和外边距 */
    [data-testid="stAppViewContainer"] { background-color: #000000 !important; }
    [data-testid="stMain"] { padding: 0 !important; }
    [data-testid="stMainViewContainer"] { padding: 0 !important; }
    [data-testid="stBlock"] { padding: 0 !important; }
    .main .block-container { 
        max-width: 100% !important; 
        padding-top: 0 !important; 
        padding-bottom: 0 !important; 
        padding-left: 0 !important; 
        padding-right: 0 !important; 
    }

    /* 彻底隐藏顶部 Header、工具栏、底部 Footer */
    header, footer, [data-testid="stHeader"], [data-testid="stToolbar"] { 
        display: none !important; 
        visibility: hidden !important; 
    }

    /* 页面背景与文字 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }

    /* --- 1:1 还原内容区 --- */
    .full-screen-wrap {
        width: 100%;
        min-height: 100vh;
        background-color: #000000;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 60px; /* 顶部留白对齐原图 */
    }

    .content-box { max-width: 1000px; width: 90%; text-align: center; }

    .hero-badge {
        display: inline-block; background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        border: 1px solid rgba(255, 45, 85, 0.3); padding: 5px 15px;
        border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 25px;
    }
    
    .hero-title { font-size: 48px; font-weight: 800; line-height: 1.1; margin-bottom: 25px; letter-spacing: -1px; }
    .hero-title span { color: #ff2d55; }
    .hero-subtitle { color: #80808b; font-size: 16px; margin-bottom: 60px; line-height: 1.6; }

    /* 功能卡片布局 */
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 80px; text-align: left; }
    .feature-card { background: #111118; border: 1px solid #1e1e24; border-radius: 16px; padding: 35px 25px; }
    .feature-card h4 { font-size: 19px; margin: 15px 0 10px 0; font-weight: 700; }
    .feature-card p { color: #80808b; font-size: 14px; line-height: 1.6; }

    /* 价格卡片布局 */
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-bottom: 80px; }
    .price-card { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 50px 20px; position: relative; }
    .price-card.featured { border: 2px solid #ff2d55; background: #0c0c14; }
    .best-badge {
        position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        background: #ff2d55; color: white; padding: 3px 14px; border-radius: 20px;
        font-size: 12px; font-weight: bold;
    }
    .price-val { font-size: 56px; font-weight: 800; margin: 20px 0; letter-spacing: -2px; }
    
    /* 激活步骤 */
    .step-section { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 50px 40px; width: 100%; margin-top: 40px; }
    .step-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-top: 40px; }
    .step-circle {
        width: 36px; height: 36px; background: #ff2d55; border-radius: 50%;
        line-height: 36px; margin: 0 auto 15px; font-weight: 800; color: white;
    }

    /* 输入框样式修正 */
    div[data-baseweb="input"] { background-color: #111118 !important; border: 1px solid #1e1e24 !important; }
    input { color: #ffffff !important; text-align: center !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 登录逻辑 ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# --- 4. 渲染 ---
if not st.session_state['auth']:
    # 使用自定义的 full-screen-wrap 容器包裹所有内容
    st.markdown("""
    <div class="full-screen-wrap">
        <div class="content-box">
            <div class="hero-badge">🔥 小红书爆款选品情报</div>
            <div class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></div>
            <p class="hero-subtitle">专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</p>
            
            <div class="feature-grid">
                <div class="feature-card"><span>💥</span><h4>识别低粉高销爆款</h4><p>帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</p></div>
                <div class="feature-card"><span>📈</span><h4>销量趋势一目了然</h4><p>每个商品都有周维度趋势图，哪个在爆发、哪个在退热，一眼看出。</p></div>
                <div class="feature-card"><span>🛒</span><h4>加购信号比销量更早</h4><p>24小时加购数据是销量的先行指标，加购高但还没爆的，就是你的机会。</p></div>
            </div>

            <div class="price-grid">
                <div class="price-card"><div>月度版</div><div class="price-val"><span>¥</span>59.9</div></div>
                <div class="price-card featured"><div class="best-badge">🔥 最多人选</div><div style="color:#ff2d55;font-weight:700">季度版</div><div class="price-val"><span>¥</span>135</div></div>
                <div class="price-card"><div>年度版</div><div class="price-val"><span>¥</span>365</div></div>
            </div>

            <div class="step-section">
                <h3 style="font-size:24px; font-weight:800;">如何激活会员</h3>
                <p style="color:#80808b; margin-top:12px;">联系微信 <b>beiyuanbitan01</b> 完成支付，我将发送激活码给你。</p>
                <div class="step-grid">
                    <div class="step-item"><div class="step-circle">1</div><div>复制产品信息码</div></div>
                    <div class="step-item"><div class="step-circle">2</div><div>联系微信支付</div></div>
                    <div class="step-item"><div class="step-circle">3</div><div>收到激活码</div></div>
                    <div class="step-item"><div class="step-circle">4</div><div>填入下方解锁</div></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, col_in, _ = st.columns([1, 1, 1])
    with col_in:
        pwd = st.text_input("PWD", type="password", placeholder="填入激活码解锁数据", label_visibility="collapsed")
        if pwd == "8888":
            st.session_state['auth'] = True
            st.rerun()
else:
    # 已解锁：数据中心
    st.markdown("<div style='padding:40px;'>", unsafe_allow_html=True)
    st.markdown("### 📊 实时数据中心")
    if st.button("退出登录"):
        st.session_state['auth'] = False
        st.rerun()
    
    try:
        df = pd.read_csv("红点数据_导入模板.csv")
        st.dataframe(df, use_container_width=True, height=800)
    except:
        st.error("未找到文件：红点数据_导入模板.csv")
    st.markdown("</div>", unsafe_allow_html=True)
