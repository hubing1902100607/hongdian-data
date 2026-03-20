import streamlit as st
import pandas as pd

# --- 1. 强制页面全局设置（隐藏所有 Streamlit 默认元素） ---
st.set_page_config(page_title="红点数据中心", layout="wide", initial_sidebar_state="expanded")

# --- 2. 核心 CSS：这是 1:1 还原你网页的精髓 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+SC:wght@400;700&display=swap');
    
    .stApp { background-color: #060608; color: #ffffff; font-family: 'Inter', 'Noto Sans SC', sans-serif; }
    header { visibility: hidden; } /* 隐藏顶部装饰条 */
    
    /* 侧边栏样式 */
    [data-testid="stSidebar"] { background-color: #0f0f13; border-right: 1px solid #1e1e24; width: 280px !important; }
    
    /* Landing Page 容器 */
    .lp-container { max-width: 1100px; margin: 0 auto; padding: 60px 20px; text-align: center; }
    
    /* 顶部 Badge */
    .hero-badge {
        background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        padding: 5px 15px; border-radius: 20px; font-size: 13px; font-weight: 600;
        display: inline-block; margin-bottom: 25px; border: 1px solid rgba(255, 45, 85, 0.2);
    }
    
    /* 主标题与副标题 */
    .hero-title { font-size: 46px; font-weight: 800; line-height: 1.2; margin-bottom: 25px; letter-spacing: -1px; }
    .hero-title span { color: #ff2d55; }
    .hero-subtitle { color: #80808b; font-size: 17px; max-width: 650px; margin: 0 auto 60px; line-height: 1.6; }

    /* 功能卡片网格 (3x2) */
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 80px; }
    .feature-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 18px; padding: 30px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); text-align: left; position: relative;
    }
    .feature-card:hover { border-color: #ff2d55; transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
    .card-icon { font-size: 28px; margin-bottom: 20px; display: block; }
    .card-title { font-size: 20px; font-weight: 700; margin-bottom: 12px; }
    .card-desc { font-size: 14px; color: #80808b; line-height: 1.6; }
    .card-tag { 
        display: inline-block; padding: 4px 12px; border-radius: 8px; font-size: 11px; margin-top: 20px;
        background: rgba(255,255,255,0.05); color: #80808b; font-weight: 600;
    }

    /* 价格方案网格 (3列) */
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-bottom: 100px; }
    .price-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 24px; padding: 50px 30px;
        text-align: center; position: relative; transition: 0.3s;
    }
    .price-card.featured { border: 2.5px solid #ff2d55; transform: scale(1.05); z-index: 10; background: #13131c; }
    .price-top-badge {
        position: absolute; top: -15px; left: 50%; transform: translateX(-50%);
        background: linear-gradient(135deg, #ff2d55, #fb7185); color: white;
        padding: 5px 18px; border-radius: 30px; font-size: 12px; font-weight: 800; box-shadow: 0 5px 15px rgba(255, 45, 85, 0.4);
    }
    .price-unit { font-size: 15px; color: #80808b; margin-bottom: 15px; font-weight: 500; }
    .price-value { font-size: 64px; font-weight: 800; margin: 15px 0; letter-spacing: -2px; }
    .price-value span { font-size: 26px; margin-right: 4px; }
    .price-duration { color: #4b4b5a; font-size: 15px; margin-bottom: 25px; }
    .price-save-tag {
        display: inline-block; background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        padding: 4px 14px; border-radius: 6px; font-size: 13px; font-weight: 600;
    }

    /* FAQ 区域 */
    .faq-container { max-width: 850px; margin: 0 auto; text-align: left; border-top: 1px solid #1e1e24; padding-top: 60px; }
    .faq-item { padding: 30px 0; border-bottom: 1px solid #1e1e24; }
    .faq-q { font-size: 18px; font-weight: 700; margin-bottom: 12px; color: #fff; }
    .faq-a { font-size: 15px; color: #80808b; line-height: 1.7; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 侧边栏：100% 还原商业入口 ---
with st.sidebar:
    st.image("https://hubing1902100607.github.io/hongdian-data/wechat_qr.png", width=220)
    st.markdown("<h2 style='text-align:center; margin-top:10px;'>红点数据中心</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 核心：激活码输入
    access_code = st.text_input("🔑 输入激活码解锁数据", type="password", help="添加上方大师微信获取激活码")
    
    # 大师点评模块
    st.markdown(f"""
        <div style='background:rgba(255,45,85,0.06); padding:20px; border-radius:15px; border:1px solid rgba(255,45,85,0.15); margin-top:40px;'>
            <p style='color:#ff2d55; font-size:14px; font-weight:bold; margin-bottom:10px;'>💪 大师复盘</p>
            <p style='color:#a0a0ab; font-size:13px; line-height:1.7;'>
                现在的选品逻辑已经变了。不要去卷大类目，要在小红书的“低粉、高转化”链接中找机会。这个工具就是为你过滤噪音的。
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. 逻辑切换：解锁前显示 Landing Page，解锁后显示数据后台 ---
if access_code == "8888": # 此处设为你的默认测试码
    st.title("📊 红点选品实时监控台")
    try:
        df = pd.read_csv("红点数据_导入模版.csv")
        st.dataframe(df, use_container_width=True, height=600)
    except:
        st.error("数据加载失败，请检查仓库中的 CSV 文件名。")
else:
    # --- 1:1 还原 Landing Page ---
    st.markdown("""
    <div class="lp-container">
        <div class="hero-badge">🔥 小红书爆款选品情报</div>
        <h1 class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></h1>
        <p class="hero-subtitle">专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</p>
        
        <div class="feature-grid">
            <div class="feature-card">
                <span class="card-icon">💥</span>
                <div class="card-title">识别低粉高销爆款</div>
                <div class="card-desc">帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</div>
                <div class="card-tag" style="background:rgba(255,45,85,0.1); color:#ff2d55;">低粉爆品标签</div>
            </div>
            <div class="feature-card">
                <span class="card-icon">📈</span>
                <div class="card-title">销量趋势一目了然</div>
                <div class="card-desc">每个商品都有周维度趋势图，哪个品在爆发、哪个在退热，
