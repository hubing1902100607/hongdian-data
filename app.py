import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. 强制页面全局设置 ---
st.set_page_config(page_title="红点数据 · 大师选品台", layout="wide", initial_sidebar_state="expanded")

# --- 2. 核心 CSS 注入：这是还原你图片的“灵魂” ---
st.markdown("""
    <style>
    /* 全局背景与字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    .stApp { background-color: #060608; color: #ffffff; font-family: 'Inter', sans-serif; }
    header {visibility: hidden;} /* 隐藏 Streamlit 默认顶部栏 */

    /* 侧边栏美化 */
    [data-testid="stSidebar"] { background-color: #0f0f13; border-right: 1px solid #1e1e24; }
    
    /* 功能卡片布局 (6格) */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-top: 40px;
    }
    .feature-card {
        background: #111118;
        border: 1px solid #1e1e24;
        border-radius: 16px;
        padding: 24px;
        transition: all 0.3s ease;
    }
    .feature-card:hover { border-color: #ff2d55; transform: translateY(-5px); }
    .icon { font-size: 24px; margin-bottom: 15px; }
    .feature-title { font-size: 18px; font-weight: 700; margin-bottom: 10px; color: #fff; }
    .feature-desc { font-size: 14px; color: #80808b; line-height: 1.6; }
    .tag { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; margin-top: 15px; }
    .tag-red { background: rgba(255,45,85,0.1); color: #ff2d55; }
    .tag-teal { background: rgba(0,201,167,0.1); color: #00c9a7; }
    .tag-gold { background: rgba(255,214,10,0.1); color: #ffd60a; }

    /* 价格方案 (3列) */
    .price-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        margin-top: 80px;
        padding-bottom: 50px;
    }
    .price-card {
        background: #111118;
        border: 1px solid #1e1e24;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        position: relative;
    }
    .price-card.featured { border: 2px solid #ff2d55; }
    .price-badge {
        position: absolute; top: -15px; left: 50%; transform: translateX(-50%);
        background: linear-gradient(90deg, #ff2d55, #fb7185);
        color: white; padding: 4px 15px; border-radius: 20px; font-size: 12px;
    }
    .price-val { font-size: 48px; font-weight: 800; margin: 20px 0; }
    .price-val span { font-size: 20px; margin-right: 5px; }
    
    /* 底部横条样式 */
    .status-bar {
        background: #111118;
        border-radius: 12px;
        padding: 15px 30px;
        display: flex;
        justify-content: center;
        gap: 40px;
        margin: 40px 0;
        font-size: 14px;
        color: #80808b;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 侧边栏菜单 ---
with st.sidebar:
    st.image("https://hubing1902100607.github.io/hongdian-data/wechat_qr.png", width=180)
    st.markdown("<h2 style='text-align:center;'>红点数据中心</h2>", unsafe_allow_html=True)
    st.markdown("---")
    access_code = st.text_input("🔑 输入激活码解锁数据", type="password")
    st.markdown("""
        <div style='background:rgba(255,255,255,0.05); padding:15px; border-radius:10px; margin-top:20px;'>
            <p style='color:#ff2d55; font-size:14px;'>💪 <b>大师复盘</b></p>
            <p style='color:#80808b; font-size:13px;'>盯紧“低粉爆品”，这是普通人逆袭的唯一路径。数据不会骗人，逻辑才是核心。</p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. 主界面：判断是否已解锁 ---
if access_code == "8888": # 你可以自定义这个测试码
    # [这里是你之前的数据面板代码，保持不变，仅在解锁后显示]
    st.success("✅ 激活成功！正在加载深度选品数据...")
    raw_df = pd.read_csv("红点数据_导入模版.csv")
    # ... (省略数据分析逻辑，实际运行会保留)
    st.dataframe(raw_df)

else:
    # --- 像素级还原：展示你截图里的设计稿 ---
    st.markdown("<h4 style='text-align:center; color:#80808b;'>专为电商卖家开发的选品数据工具，帮你提前发现爆款信号，少踩坑、多出单。</h4>", unsafe_allow_html=True)
    
    # 6 个功能卡片
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="icon">💥</div>
            <div class="feature-title">识别低粉高销爆款</div>
            <div class="feature-desc">帮你找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</div>
            <div class="tag tag-red">低粉爆品标签</div>
        </div>
        <div class="feature-card">
            <div class="icon">📈</div>
            <div class="feature-title">销量趋势一目了然</div>
            <div class="feature-desc">每个商品都有周维度趋势图，哪个品在爆发、哪个在退热，一眼看出。</div>
            <div class="tag tag-teal">趋势图表</div>
        </div>
        <div class="feature-card">
            <div class="icon">🛒</div>
            <div class="feature-title">加购信号比销量更早</div>
            <div class="feature-desc">24小时加购数据是销量的先行指标，加购高但还没爆的，就是你的机会。</div>
            <div class="tag tag-gold">潜力预警</div>
        </div>
        <div class="feature-card">
            <div class="icon">🌱</div>
            <div class="feature-title">发现隐藏潜力品</div>
            <div class="feature-desc">低粉丝、低加购、但24小时购买人数高——用户看到就下单的冲动消费爆款。</div>
            <div class="tag tag-teal">隐藏潜力</div>
        </div>
        <div class="feature-card">
            <div class="icon">🔍</div>
            <div class="feature-title">多维筛选快速选品</div>
            <div class="feature-desc">按类目、销量、加购、价格自由筛选，收藏感兴趣的商品随时回看。</div>
            <div class="tag tag-teal">智能筛选</div>
        </div>
        <div class="feature-card">
            <div class="icon">📊</div>
            <div class="feature-title">一键导出数据表格</div>
            <div class="feature-desc">全部数据支持导出为 Excel，方便整理与团队共享选品方案。</div>
            <div class="tag tag-teal">导出 Excel</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 状态栏
    st.markdown("""
    <div class="status-bar">
        <span>● 覆盖食品、日化、百货、宠物、虚拟、服装等热门类目</span>
        <span>● 数据持续更新</span>
        <span>● 激活码绑定设备，数据安全独享</span>
    </div>
    """, unsafe_allow_html=True)

    # 价格表
    st.markdown("""
    <div class="price-grid">
        <div class="price-card">
            <div style="color:#80808b">月度版</div>
            <div class="price-val"><span>¥</span>59.9</div>
            <div style="color:#4b4b5a">有效期 30 天</div>
        </div>
        <div class="price-card featured">
            <div class="price-badge">🔥 最多人选</div>
            <div style="color:#80808b">季度版</div>
            <div class="price-val"><span>¥</span>135</div>
            <div style="color:#4b4b5a">有效期 90 天</div>
        </div>
        <div class="price-card">
            <div style="color:#80808b">年度版</div>
            <div class="price-val"><span>¥</span>365</div>
            <div style="color:#4b4b5a">有效期 365 天</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
