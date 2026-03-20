import streamlit as st
import pandas as pd

# --- 1. 强制页面全局设置（彻底抹除 Streamlit 痕迹） ---
st.set_page_config(page_title="红点数据", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* 1. 强制纯黑背景与字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* 2. 隐藏所有 Streamlit 顶部装饰、页脚、工具栏 */
    header, footer, [data-testid="stToolbar"], [data-testid="stHeader"] { visibility: hidden; display: none; }
    [data-testid="stSidebar"] { display: none; } /* 彻底移除侧边栏 */

    /* 3. 页面容器：对齐你 GitHub 的紧凑感 */
    .main-wrap { max-width: 1000px; margin: 0 auto; padding: 40px 20px; text-align: center; }
    
    /* 4. 顶部 Badge：🔥 标签 */
    .hero-badge {
        display: inline-block; background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        border: 1px solid rgba(255, 45, 85, 0.3); padding: 4px 14px;
        border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 25px;
    }
    
    /* 5. 标题：加大加粗，特定词标红 */
    .hero-title { font-size: 46px; font-weight: 800; line-height: 1.1; margin-bottom: 25px; color: #ffffff; letter-spacing: -1px; }
    .hero-title span { color: #ff2d55; }
    .hero-subtitle { color: #80808b; font-size: 17px; margin-bottom: 60px; line-height: 1.6; max-width: 700px; margin-left: auto; margin-right: auto; }

    /* 6. 功能卡片：3列极简黑框 */
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 80px; text-align: left; }
    .feature-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 16px;
        padding: 35px 25px; transition: all 0.3s ease;
    }
    .feature-card:hover { border-color: #ff2d55; }
    .feature-card h4 { font-size: 19px; font-weight: 700; margin: 15px 0 10px 0; color: #ffffff; }
    .feature-card p { color: #80808b; font-size: 14px; line-height: 1.6; }

    /* 7. 价格卡片：对齐你的图 1 设计 */
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-bottom: 80px; }
    .price-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 20px;
        padding: 50px 20px; position: relative; transition: 0.3s;
    }
    .price-card.featured { border: 1.5px solid #ff2d55; background: #0c0c14; transform: scale(1.02); }
    .best-badge {
        position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        background: #ff2d55; color: white; padding: 3px 14px; border-radius: 20px;
        font-size: 12px; font-weight: bold;
    }
    .price-val { font-size: 56px; font-weight: 800; margin: 20px 0; color: #ffffff; letter-spacing: -2px; }
    .price-val span { font-size: 26px; margin-right: 4px; }
    .price-sub { color: #4b4b5a; font-size: 14px; }

    /* 8. 激活步骤：还原底部 1-2-3-4 */
    .step-section { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 50px 40px; }
    .step-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-top: 40px; }
    .step-item { text-align: center; }
    .step-circle {
        width: 36px; height: 36px; background: #ff2d55; border-radius: 50%;
        line-height: 36px; margin: 0 auto 15px; font-weight: 800; font-size: 16px; color: white;
    }
    .step-label { font-size: 14px; color: #ffffff; font-weight: 500; }
    
    /* 9. 输入框美化：使其融入黑金风格 */
    div[data-baseweb="input"] { background-color: #111118 !important; border: 1px solid #1e1e24 !important; border-radius: 8px !important; }
    input { color: #ffffff !important; text-align: center !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. 状态逻辑 ---
if 'locked' not in st.session_state:
    st.session_state['locked'] = True

# --- 3. 页面内容渲染 ---

if st.session_state['locked']:
    # 完全还原图 1 的 Landing Page
    st.markdown("""
    <div class="main-wrap">
        <div class="hero-badge">🔥 小红书爆款选品情报</div>
        <div class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></div>
        <p class="hero-subtitle">专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</p>
        
        <div class="feature-grid">
            <div class="feature-card">
                <span style="font-size:24px;">💥</span>
                <h4>识别低粉高销爆款</h4>
                <p>帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</p>
            </div>
            <div class="feature-card">
                <span style="font-size:24px;">📈</span>
                <h4>销量趋势一目了然</h4>
                <p>每个商品都有周维度趋势图，哪个在爆发、哪个在退热，一眼看出。</p>
            </div>
            <div class="feature-card">
                <span style="font-size:24px;">🛒</span>
                <h4>加购信号比销量更早</h4>
                <p>24小时加购数据是销量的先行指标，加购高但还没爆的，就是你的机会。</p>
            </div>
        </div>

        <div class="price-grid">
            <div class="price-card">
                <div style="color:#80808b; font-size:15px;">月度版</div>
                <div class="price-val"><span>¥</span>59.9</div>
                <div class="price-sub">有效期 30 天</div>
            </div>
            <div class="price-card featured">
                <div class="best-badge">🔥 最多人选</div>
                <div style="color:#ff2d55; font-weight:700; font-size:15px;">季度版</div>
                <div class="price-val"><span>¥</span>135</div>
                <div class="price-sub">有效期 90 天</div>
            </div>
            <div class="price-card">
                <div style="color:#80808b; font-size:15px;">年度版</div>
                <div class="price-val"><span>¥</span>365</div>
                <div class="price-sub">有效期 365 天</div>
            </div>
        </div>

        <div class="step-section">
            <h3 style="font-size:24px; font-weight:800; color:#ffffff; margin:0;">如何激活会员</h3>
            <p style="color:#80808b; font-size:15px; margin-top:12px;">联系微信 <b style="color:#ffffff;">beiyuanbitan01</b> 完成支付，我将发送激活码给你。</p>
            <div class="step-grid">
                <div class="step-item"><div class="step-circle">1</div><div class="step-label">复制产品信息码</div></div>
                <div class="step-item"><div class="step-circle">2</div><div class="step-label">联系微信支付</div></div>
                <div class="step-item"><div class="step-circle">3</div><div class="step-label">收到激活码</div></div>
                <div class="step-item"><div class="step-circle">4</div><div class="step-label">填入下方解锁</div></div>
            </div>
