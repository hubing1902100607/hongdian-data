import streamlit as st
import pandas as pd

# --- 1. 基础配置：锁定宽屏 & 强制隐藏侧边栏 ---
st.set_page_config(page_title="红点数据", layout="wide", initial_sidebar_state="collapsed")

# --- 2. 深度 CSS 覆盖：抹除 Streamlit 所有默认布局痕迹 ---
st.markdown("""
    <style>
    /* 彻底重置 Streamlit 页面容器间距 */
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    [data-testid="stMain"] { padding: 0 !important; }
    [data-testid="stMainViewContainer"] { padding: 0 !important; }
    [data-testid="stBlock"] { padding: 0 !important; }
    .main .block-container { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }

    /* 隐藏所有顶部 Header、工具栏和底部 Footer */
    header, footer, [data-testid="stHeader"], [data-testid="stToolbar"] { visibility: hidden; display: none !important; }

    /* 引入字体与全局文字颜色 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .stApp { color: #ffffff; font-family: 'Inter', sans-serif; }

    /* --- 1:1 还原你图片中的 CSS 结构 --- */
    .content-center { 
        max-width: 1000px; margin: 0 auto; padding: 80px 20px; text-align: center; 
    }
    
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
    .feature-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 16px; padding: 35px 25px;
    }
    .feature-card h4 { font-size: 19px; margin: 15px 0 10px 0; font-weight: 700; }
    .feature-card p { color: #80808b; font-size: 14px; line-height: 1.6; }

    /* 价格卡片布局 */
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-bottom: 80px; }
    .price-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 20px;
        padding: 50px 20px; position: relative;
    }
    .price-card.featured { border: 2px solid #ff2d55; background: #0c0c14; }
    .best-badge {
        position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        background: #ff2d55; color: white; padding: 3px 14px; border-radius: 20px;
        font-size: 12px; font-weight: bold;
    }
    .price-val { font-size: 56px; font-weight: 800; margin: 20px 0; letter-spacing: -2px; }
    .price-val span { font-size: 26px; }
    
    /* 激活步骤区 */
    .step-section { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 50px 40px; margin-top: 40px; }
    .step-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-top: 40px; }
    .step-item { text-align: center; }
    .step-circle {
        width: 36px; height: 36px; background: #ff2d55; border-radius: 50%;
        line-height: 36px; margin: 0 auto 15px; font-weight: 800; color: white;
    }

    /* 输入框样式修正 */
    div[data-baseweb="input"] { background-color: #111118 !important; border: 1px solid #1e1e24 !important; }
    input { color: #ffffff !important; text-align: center !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 登录权限判断 ---
if 'auth_status' not in st.session_state:
    st.session_state['auth_status'] = False

# --- 4. 渲染页面 ---
if not st.session_state['auth_status']:
    # 展示还原后的 Landing Page
    st.markdown("""
    <div class="content-center">
        <div class="hero-badge">🔥 小红书爆款选品情报</div>
        <div class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></div>
        <p class="hero-subtitle">专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</p>
        
        <div class="feature-grid">
            <div class="feature-card"><span>💥</span><h4>识别低粉高销爆款</h4><p>帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</p></div>
            <div class="feature-card"><span>📈</span><h4>销量趋势一目了然</h4><p>每个商品都有周维度趋势图，哪个在爆发、哪个在退热，一眼看出。</p></div>
            <div class="feature-card"><span>🛒</span><h4>加购信号比销量更早</h4><p>24小时加购数据是销量的先行指标，加购高但还没爆的，就是你的机会。</p></div>
        </div>

        <div class="price-grid">
            <div class="price-card"><div style="color:#80808b">月度版</div><div class="price-val"><span>¥</span>59.9</div></div>
            <div class="price-card featured"><div class="best-badge">🔥 最多人选</div><div style="color:#ff2d55;font-weight:700">季度版</div><div class="price-val"><span>¥</span>135</div></div>
            <div class="price-card"><div style="color:#80808b">年度版</div><div class="price-val"><span>¥</span>365</div></div>
        </div>

        <div class="step-section">
            <h3 style="font-size:24px; font-weight:800;">如何激活会员</h3>
            <p style="color:#80808b; font-size:15px; margin-top:12px;">联系微信 <b>beiyuanbitan01</b> 完成支付，我将发送激活码给你。</p>
            <div class="step-grid">
                <div class="step-item"><div class="step-circle">1</div><div>复制产品信息码
