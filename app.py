import streamlit as st
import pandas as pd

# --- 1. 全局配置：强制深色模式 & 隐藏 Streamlit 干扰 ---
st.set_page_config(page_title="红点数据", layout="wide")

st.markdown("""
    <style>
    /* 彻底重塑背景与字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    header, footer { visibility: hidden; }
    
    /* 1:1 还原 Landing Page 容器 */
    .main-wrap { max-width: 1000px; margin: 0 auto; padding: 60px 20px; text-align: center; }
    
    /* 顶部 Badge */
    .hero-badge {
        display: inline-block; background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        border: 1px solid rgba(255, 45, 85, 0.3); padding: 5px 15px;
        border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 25px;
    }
    
    /* 主标题 */
    .hero-title { font-size: 44px; font-weight: 800; line-height: 1.2; margin-bottom: 25px; }
    .hero-title span { color: #ff2d55; }
    .hero-subtitle { color: #80808b; font-size: 16px; margin-bottom: 60px; }

    /* 功能卡片布局 (3列) */
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 80px; }
    .feature-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 16px;
        padding: 30px 20px; text-align: left;
    }
    .feature-icon { font-size: 24px; margin-bottom: 15px; display: block; }
    .feature-card h4 { font-size: 18px; margin-bottom: 12px; }
    .feature-card p { color: #80808b; font-size: 14px; line-height: 1.6; }

    /* 价格卡片布局 (3列) */
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-bottom: 80px; }
    .price-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 20px;
        padding: 40px 20px; position: relative;
    }
    .price-card.featured { border: 2px solid #ff2d55; background: #0c0c14; }
    .best-badge {
        position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        background: #ff2d55; color: white; padding: 3px 12px; border-radius: 20px;
        font-size: 12px; font-weight: bold;
    }
    .price-val { font-size: 48px; font-weight: 800; margin: 20px 0; }
    .price-val span { font-size: 22px; margin-right: 4px; }
    .price-sub { color: #4b4b5a; font-size: 13px; }

    /* 激活步骤区 */
    .step-section { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 40px; margin-bottom: 60px; }
    .step-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-top: 35px; }
    .step-item { text-align: center; }
    .step-circle {
        width: 34px; height: 34px; background: #ff2d55; border-radius: 50%;
        line-height: 34px; margin: 0 auto 15px; font-weight: 800; font-size: 16px;
    }
    .step-text { font-size: 14px; color: #ffffff; }

    /* 底部声明 */
    .disclaimer { color: #4b4b5a; font-size: 12px; border-top: 1px solid #1e1e24; padding-top: 40px; text-align: left; }
    </style>
""", unsafe_allow_html=True)

# --- 2. 权限状态管理 ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- 3. 页面渲染逻辑 ---
if not st.session_state['authenticated']:
    # --- 未解锁：展示和你 GitHub 图片一模一样的 Landing Page ---
    st.markdown("""
    <div class="main-wrap">
        <div class="hero-badge">🔥 小红书爆款选品情报</div>
        <div class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></div>
        <p class="hero-subtitle">专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</p>
        
        <div class="feature-grid">
            <div class="feature-card">
                <span class="feature-icon">💥</span>
                <h4>识别低粉高销爆款</h4>
                <p>帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📈</span>
                <h4>销量趋势一目了然</h4>
                <p>每个商品都有周维度趋势图，哪个在爆发、哪个在退热，一眼看出。</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🛒</span>
                <h4>加购信号比销量更早</h4>
                <p>24小时加购数据是销量的先行指标，加购高但还没爆的，就是你的机会。</p>
            </div>
        </div>

        <div class="price-grid">
            <div class="price-card">
                <div style="color:#80808b">月度版</div>
                <div class="price-val"><span>¥</span>59.9</div>
                <div class="price-sub">有效期 30 天</div>
            </div>
            <div class="price-card featured">
                <div class="best-badge">🔥 最多人选</div>
                <div style="color:#ff2d55; font-weight:bold;">季度版</div>
                <div class="price-val"><span>¥</span>135</div>
                <div class="price-sub">有效期 90 天</div>
            </div>
            <div class="price-card">
                <div style="color:#80808b">年度版</div>
                <div class="price-val"><span>¥</span>365</div>
                <div class="price-sub">有效期 365 天</div>
            </div>
        </div>

        <div class="step-section">
            <h3 style="font-size:22px; font-weight:800;">如何激活会员</h3>
            <p style="color:#80808b; font-size:14px; margin-top:10px;">联系微信 <b>beiyuanbitan01</b> 完成支付，我将发送激活码给你。</p>
            <div class="step-grid">
                <div class="step-item"><div class="step-circle">1</div><div class="step-text">复制产品信息码</div></div>
                <div class="step-item"><div class="step-circle">2</div><div class="step-text">联系微信支付</div></div>
                <div class="step-item"><div class="step-circle">3</div><div class="step-text">收到激活码</div></div>
                <div class="step-item"><div class="step-circle">4</div><div class="step-text">填入下方解锁</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 激活码输入框（放在 steps 下方，居中布局）
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        pwd = st.text_input("🔑 请输入激活码解锁数据", type="password")
        if pwd == "8888": # 填入你的激活码
            st.session_state['authenticated'] = True
            st.rerun()

    st.markdown("""
    <div class="main-wrap">
        <div class="disclaimer">
            免责声明：本平台提供的全部数据均来源于小红书公开信息，仅作为达人选品参考使用。本平台不对因参考本数据产生的任何直接或间接损失承担责任。
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    # --- 已解锁：展示纯净的数据表格 ---
    st.markdown("<div style='padding:20px;'>", unsafe_allow_html=True)
    st.markdown("### 📊 实时数据中心")
    if st.button("退出登录"):
        st.session_state['authenticated'] = False
        st.rerun()
    
    try:
        df = pd.read_csv("红点数据_导入模版.csv")
        st.dataframe(df, use_container_width=True, height=800)
    except:
        st.error("未找到数据文件，请确保 CSV 已上传至仓库。")
    st.markdown("</div>", unsafe_allow_html=True)
