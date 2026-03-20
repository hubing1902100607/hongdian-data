import streamlit as st
import pandas as pd

# --- 1. 基础配置 ---
st.set_page_config(page_title="红点数据 · 大师选品台", layout="wide", initial_sidebar_state="expanded")

# --- 2. 核心 CSS 注入：1比1还原视觉灵魂 ---
st.markdown("""
    <style>
    /* 全局背景与字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    .stApp { background-color: #060608; color: #ffffff; font-family: 'Inter', sans-serif; }
    header { visibility: hidden; } /* 隐藏原生顶部 */
    [data-testid="stSidebar"] { background-color: #0f0f13; border-right: 1px solid #1e1e24; width: 280px !important; }
    
    /* 标题部分 */
    .hero-badge {
        background: rgba(255, 45, 85, 0.1); color: #ff2d55;
        padding: 4px 12px; border-radius: 20px; font-size: 13px;
        display: inline-block; margin-bottom: 20px;
    }
    .hero-title { font-size: 42px; font-weight: 800; line-height: 1.2; margin-bottom: 20px; }
    .hero-title span { color: #ff2d55; }
    .hero-subtitle { color: #80808b; font-size: 16px; max-width: 600px; margin: 0 auto 50px; }

    /* 功能卡片布局 (2x3) */
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 40px auto; max-width: 1200px; }
    .feature-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 16px; padding: 24px;
        transition: all 0.3s; text-align: left;
    }
    .feature-card:hover { border-color: #ff2d55; transform: translateY(-5px); }
    .card-icon { font-size: 24px; margin-bottom: 15px; }
    .card-title { font-size: 18px; font-weight: 700; margin-bottom: 10px; }
    .card-desc { font-size: 14px; color: #80808b; line-height: 1.6; min-height: 60px; }
    .card-tag { 
        display: inline-block; padding: 3px 10px; border-radius: 6px; font-size: 11px; margin-top: 15px;
        background: rgba(255,255,255,0.05); color: #80808b;
    }
    .tag-red { background: rgba(255,45,85,0.1); color: #ff2d55; }
    .tag-teal { background: rgba(0,201,167,0.1); color: #00c9a7; }
    .tag-gold { background: rgba(255,214,10,0.1); color: #ffd60a; }

    /* 价格方案 (3列) */
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin: 60px auto; max-width: 1100px; }
    .price-card {
        background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 40px 30px;
        text-align: center; position: relative;
    }
    .price-card.featured { border: 2px solid #ff2d55; }
    .price-top-badge {
        position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        background: linear-gradient(90deg, #ff2d55, #fb7185); color: white;
        padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;
    }
    .price-unit { font-size: 14px; color: #80808b; margin-bottom: 10px; }
    .price-value { font-size: 56px; font-weight: 800; margin: 10px 0; }
    .price-value span { font-size: 24px; margin-right: 4px; }
    .price-duration { color: #4b4b5a; font-size: 14px; margin-bottom: 20px; }
    .price-sub-tag {
        display: inline-block; background: rgba(255,45,85,0.1); color: #ff2d55;
        padding: 2px 10px; border-radius: 4px; font-size: 12px; margin-bottom: 30px;
    }

    /* 常见问题 */
    .faq-section { max-width: 800px; margin: 100px auto 50px; text-align: left; }
    .faq-item { border-bottom: 1px solid #1e1e24; padding: 25px 0; }
    .faq-q { font-size: 16px; font-weight: 600; margin-bottom: 10px; }
    .faq-a { font-size: 14px; color: #80808b; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 侧边栏：1比1还原二维码和大师点评 ---
with st.sidebar:
    # 顶部二维码
    st.image("https://hubing1902100607.github.io/hongdian-data/wechat_qr.png", width=200)
    st.markdown("<h3 style='text-align:center;'>🔥 红点数据中心</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 激活码输入
    access_code = st.text_input("🔑 输入激活码解锁数据", type="password", help="请扫描上方二维码获取")
    
    # 大师复盘模块
    st.markdown("""
        <div style='background:rgba(255,45,85,0.05); padding:15px; border-radius:12px; border:1px solid rgba(255,45,85,0.1); margin-top:30px;'>
            <p style='color:#ff2d55; font-size:14px; margin-bottom:8px;'>✍️ <b>大师复盘</b></p>
            <p style='color:#b0b0bc; font-size:13px; line-height:1.6;'>
                今天的‘黑马’大多集中在 19-39 元客单价。盯紧千万粉丝的号没用，看这种‘低粉、高转化’的品才是红利。
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. 主界面逻辑 ---
if access_code == "8888":
    # 解锁后的专业数据面板
    st.markdown("## 📊 实时选品看板")
    df = pd.read_csv("红点数据_导入模版.csv")
    st.dataframe(df, use_container_width=True)
else:
    # --- 像素级还原：Landing Page ---
    st.markdown("<div style='text-align:center; padding-top:60px;'>", unsafe_allow_html=True)
    st.markdown("<div class='hero-badge'>🔥 小红书爆款选品情报</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>每月精选爆款数据<br>让你的带货<span>少走弯路</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</p>", unsafe_allow_html=True)
    
    # 6个功能卡片渲染
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="card-icon">💥</div>
            <div class="card-title">识别低粉高销爆款</div>
            <div class="card-desc">帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</div>
            <div class="card-tag tag-red">低粉爆品标签</div>
        </div>
        <div class="feature-card">
            <div class="card-icon">📈</div>
            <div class="card-title">销量趋势一目了然</div>
            <div class="card-desc">每个商品都有周维度趋势图，哪个品在爆发、哪个在退热，一眼看出。</div>
            <div class="card-tag tag-teal">趋势图表</div>
        </div>
        <div class="feature-card">
            <div class="card-icon">🛒</div>
            <div class="card-title">加购信号比销量更早</div>
            <div class="card-desc">24小时加购数据是销量的先行指标，加购高但还没爆的，就是你的机会。</div>
            <div class="card-tag tag-gold">潜力预警</div>
        </div>
        <div class="feature-card">
            <div class="card-icon">🌱</div>
            <div class="card-title">发现隐藏潜力品</div>
            <div class="card-desc">低粉丝、低加购、但24小时购买人数高——用户看到就下单的冲动消费爆款。</div>
            <div class="card-tag" style="color:#a855f7; background:rgba(168,85,247,0.1)">隐藏潜力</div>
        </div>
        <div class="feature-card">
            <div class="icon">🔍</div>
            <div class="card-title">多维筛选快速选品</div>
            <div class="card-desc">按类目、销量、加购、价格自由筛选，收藏感兴趣的商品随时回看。</div>
            <div class="card-tag tag-teal">智能筛选</div>
        </div>
        <div class="feature-card">
            <div class="icon">📊</div>
            <div class="card-title">一键导出数据表格</div>
            <div class="card-desc">全部数据支持导出为 Excel，方便整理与团队共享选品方案。</div>
            <div class="card-tag tag-teal">导出 Excel</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 价格表渲染
    st.markdown("""
    <div class="price-grid">
        <div class="price-card">
            <div class="price-unit">月度版</div>
            <div class="price-value"><span>¥</span>59.9</div>
            <div class="price-duration">有效期 30 天</div>
            <div class="price-sub-tag">月均 ¥59.9</div>
        </div>
        <div class="price-card featured">
            <div class="price-top-badge">👍 最多人选</div>
            <div class="price-unit">季度版</div>
            <div class="price-value"><span>¥</span>135</div>
            <div class="price-duration">有效期 90 天</div>
            <div class="price-sub-tag">月均 ¥45 · 比月度省 25%</div>
        </div>
        <div class="price-card">
            <div class="price-unit">年度版</div>
            <div class="price-value"><span>¥</span>365</div>
            <div class="price-duration">有效期 365 天</div>
            <div class="price-sub-tag">月均 ¥30.4 · 比月度省 49%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # FAQ 常见问题渲染
    st.markdown("""
    <div class="faq-section">
        <h3>常见问题</h3>
        <div class="faq-item">
            <div class="faq-q">付款后多久能收到激活码？</div>
            <div class="faq-a">添加微信并转账后，10分钟内回复专属激活码。</div>
        </div>
        <div class="faq-item">
            <div class="faq-q">兑换码可以换设备使用吗？</div>
            <div class="faq-a">不可以。兑换码一经激活绑定当前设备，不支持更换。</div>
        </div>
        <div class="faq-item">
            <div class="faq-q">到期后数据还能看吗？</div>
            <div class="faq-a">到期后登录会提示兑换码已过期，续费后即可继续使用。</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
