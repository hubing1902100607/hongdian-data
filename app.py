import streamlit as st
import pandas as pd

# --- 1. 页面配置 ---
st.set_page_config(page_title="红点数据中心", layout="wide", initial_sidebar_state="expanded")

# --- 2. 核心样式表（修复了引号报错，并针对数据页进行了美化） ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+SC:wght@400;700&display=swap');
    
    .stApp { background-color: #060608; color: #ffffff; font-family: 'Inter', 'Noto Sans SC', sans-serif; }
    header { visibility: hidden; }
    
    /* 侧边栏：大师专业范儿 */
    [data-testid="stSidebar"] { background-color: #0f0f13; border-right: 1px solid #1e1e24; }
    .sidebar-title { font-size: 20px; font-weight: 800; color: #ff2d55; margin-bottom: 20px; text-align: center; }
    
    /* 数据表格美化 */
    .stDataFrame { border: 1px solid #1e1e24; border-radius: 12px; overflow: hidden; }
    
    /* 大师点评卡片 */
    .master-note {
        background: rgba(255, 45, 85, 0.05); border-left: 4px solid #ff2d55;
        padding: 15px; border-radius: 8px; margin: 20px 0;
    }

    /* 之前的 Landing Page 样式（保留用于未登录状态） */
    .hero-title { font-size: 42px; font-weight: 800; text-align: center; margin: 40px 0; }
    .hero-title span { color: #ff2d55; }
    .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 20px; }
    .feature-card { background: #111118; border: 1px solid #1e1e24; border-radius: 15px; padding: 25px; }
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin: 50px 0; }
    .price-card { background: #111118; border: 1px solid #1e1e24; border-radius: 20px; padding: 40px 20px; text-align: center; }
    .price-card.featured { border: 2px solid #ff2d55; background: #13131c; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 侧边栏交互 ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">🍎 红点数据中心</div>', unsafe_allow_html=True)
    st.image("https://hubing1902100607.github.io/hongdian-data/wechat_qr.png", use_container_width=True)
    
    access_code = st.text_input("🔑 输入激活码解锁黑马数据", type="password")
    
    st.markdown("---")
    st.markdown("""
        <div class='master-note'>
            <p style='color:#ff2d55; font-weight:bold; margin-bottom:5px;'>💡 大师今日复盘</p>
            <p style='font-size:13px; color:#80808b; line-height:1.6;'>
                今天的“黑马”大多集中在 19-39 元客单价。盯着千万粉丝的号没用，看这种“低粉、高转化”的品才是红利。
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. 主界面逻辑 ---
if access_code == "8888": # 你的正式激活码逻辑
    st.markdown("### 📊 实时黑马选品监控台")
    
    # 这里是 Streamlit 的优势：可以加过滤器
    col1, col2, col3 = st.columns(3)
    with col1:
        category = st.selectbox("选择类目", ["全部", "美妆", "穿搭", "家居", "数码"])
    with col2:
        min_sales = st.slider("最低销量", 0, 1000, 100)
    with col3:
        sort_by = st.radio("排序规则", ["加购率", "增长速度"], horizontal=True)

    # 模拟数据加载
    try:
        # 如果你仓库里有数据，这里读取
        df = pd.read_csv("红点数据_导入模版.csv")
        st.dataframe(df, use_container_width=True, height=600)
    except:
        st.info("👋 欢迎回来！系统已就绪，请在仓库中上传最新的‘红点数据_导入模版.csv’文件。")
        
else:
    # 未登录时展示的 Landing Page（1:1 还原你 GitHub 的设计）
    st.markdown("""
    <div class="hero-title">每月精选爆款数据<br>让你的带货<span>少走弯路</span></div>
    
    <div class="feature-grid">
        <div class="feature-card">
            <h4>💥 识别低粉高销爆款</h4>
            <p style="color:#80808b; font-size:14px;">帮找到粉丝少但销量高的黑马商品，跟播风险低、复购稳。</p>
        </div>
        <div class="feature-card">
            <h4>📈 销量趋势一目了然</h4>
            <p style="color:#80808b; font-size:14px;">每个商品都有周维度趋势图，哪个在爆发一眼看出。</p>
        </div>
        <div class="feature-card">
            <h4>🛒 加购信号比销量更早</h4>
            <p style="color:#80808b; font-size:14px;">24小时加购数据是销量的先行指标，加购高就是你的机会。</p>
        </div>
    </div>

    <div class="price-grid">
        <div class="price-card">
            <div style="font-size:14px; color:#80808b;">月度版</div>
            <div style="font-size:40px; font-weight:800; margin:15px 0;">¥59.9</div>
            <div style="font-size:12px; color:#4b4b5a;">适合短期体验</div>
        </div>
        <div class="price-card featured">
            <div style="font-size:14px; color:#ff2d55; font-weight:bold;">季度版（最多人选）</div>
            <div style="font-size:40px; font-weight:800; margin:15px 0;">¥135</div>
            <div style="font-size:12px; color:#4b4b5a;">比月度省 25%</div>
        </div>
        <div class="price-card">
            <div style="font-size:14px; color:#80808b;">年度版</div>
            <div style="font-size:40px; font-weight:800; margin:15px 0;">¥365</div>
            <div style="font-size:12px; color:#4b4b5a;">月均 ¥30.4</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
