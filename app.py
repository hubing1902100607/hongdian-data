import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib
from datetime import datetime

# --- 1. 100% 还原你的产品设计逻辑 ---
st.set_page_config(page_title="红点数据 · 大师选品台", layout="wide")

# 注入你原有的 CSS 视觉灵魂
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
    :root {
        --bg: #0a0a0f; --card: #16161f; --red: #ff2d55; --teal: #00c9a7; --gold: #ffd60a;
    }
    .stApp { background-color: var(--bg); color: #e8e8f0; font-family: 'Noto Sans SC', sans-serif; }
    .metric-card {
        background: var(--card); border: 1px solid rgba(255,255,255,0.07);
        padding: 20px; border-radius: 12px; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. 核心算法：黑马与单位转换 ---
def parse_fans(val):
    if isinstance(val, str):
        val = val.lower().replace('w', '')
        try: return float(val) * 10000 if 'w' in str(val) else float(val)
        except: return 0
    return val

def get_signal(row):
    fans = parse_fans(row['店铺粉丝'])
    # 💥低粉爆品逻辑
    if fans < 500 and row['24小时加购'] > 500: return '💥低粉爆品'
    # 🌱隐藏潜力逻辑
    if fans < 500 and row['24小时加购'] < 100 and (row['销量']/30) > 100: return '🌱隐藏潜力'
    return '无'

# --- 3. 激活码校验逻辑 (HMAC 算法平移) ---
def check_license(code):
    # 这里为了演示先设为 True，后续可接入你 html 里的具体 djb2 算法
    if not code: return False
    return True 

# --- 4. 侧边栏：商业闭环 ---
with st.sidebar:
    st.image("https://hubing1902100607.github.io/hongdian-data/wechat_qr.png", width=150)
    st.title("🔐 会员激活")
    license_key = st.text_input("输入激活码访问", type="password")
    st.markdown("---")
    st.markdown("💡 **大师点评**：数据只是表象，逻辑才是财富。关注低粉爆品，避开大号内卷。")

# --- 5. 主界面逻辑 ---
if check_license(license_key):
    try:
        # 读取你仓库里的那个 CSV
        df = pd.read_csv("红点数据_导入模版 (2).csv")
        df['信号标签'] = df.apply(get_signal, axis=1)
        df['预估GMV'] = df['销量'] * df['价格']
        
        # 顶部指标卡
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="metric-card"><p>累计追踪</p><h3>{}</h3></div>'.format(len(df)), unsafe_allow_html=True)
        with c2: st.markdown('<div class="metric-card" style="color:var(--red)"><p>💥低粉爆品</p><h3>{}</h3></div>'.format(len(df[df['信号标签']=='💥低粉爆品'])), unsafe_allow_html=True)
        with c3: st.markdown('<div class="metric-card" style="color:var(--teal)"><p>🌱隐藏潜力</p><h3>{}</h3></div>'.format(len(df[df['信号标签']=='🌱隐藏潜力'])), unsafe_allow_html=True)
        with c4: st.markdown('<div class="metric-card" style="color:var(--gold)"><p>24h总加购</p><h3>{}</h3></div>'.format(df['24小时加购'].sum()), unsafe_allow_html=True)

        st.markdown("### 🚀 黑马监控列表")
        
        # 数据过滤与展示
        display_df = df[['日期', '商品链接', '销量', '24小时加购', '24小时购买人数', '价格', '店铺粉丝', '信号标签', '预估GMV']]
        
        # 100% 还原点击跳转
        st.dataframe(
            display_df,
            column_config={
                "商品链接": st.column_config.LinkColumn("🔗 点击跳转"),
                "预估GMV": st.column_config.NumberColumn("预估GMV (¥)", format="¥ %d")
            },
            hide_index=True,
            use_container_width=True
        )

        # 趋势图表：还原你的 Chart.js
        st.markdown("### 📈 销量趋势分析")
        target_item = st.selectbox("选择要分析的商品", df['商品链接'].unique())
        item_data = df[df['商品链接'] == target_item]
        fig = px.line(item_data, x='日期', y='销量', markers=True, color_discrete_sequence=['#ff2d55'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#e8e8f0')
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"数据读取失败，请确保仓库中存在『红点数据_导入模版 (2).csv』。详情: {e}")
else:
    st.warning("⚠️ 请在左侧输入有效的激活码以解锁深度数据。")
    st.info("未获得激活码？请扫描上方二维码联系大师。")
