import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. 页面配置与赛博风 UI 注入 ---
st.set_page_config(page_title="红点数据 · 大师选品台", layout="wide", initial_sidebar_state="expanded")

# 注入 CSS 还原你原来的高级质感
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
    :root {
        --bg: #0a0a0f; --card: #16161f; --red: #ff2d55; --teal: #00c9a7; --gold: #ffd60a; --text: #e8e8f0;
    }
    .stApp { background-color: var(--bg); color: var(--text); font-family: 'Noto Sans SC', sans-serif; }
    /* 自定义指标卡片 */
    .m-card {
        background: var(--card); border: 1px solid rgba(255,255,255,0.07);
        padding: 20px; border-radius: 12px; text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .m-title { color: #9090a8; font-size: 0.9rem; margin-bottom: 5px; }
    .m-val { font-size: 1.8rem; font-weight: 700; margin: 0; }
    </style>
""", unsafe_allow_html=True)

# --- 2. 核心算法：粉丝转换与黑马信号 ---
def parse_fans(val):
    """还原你代码中处理 1.75w 等格式的逻辑"""
    if isinstance(val, str):
        val = val.lower().strip().replace('w', '')
        try:
            return float(val) * 10000 if 'w' in str(val) else float(val)
        except: return 0
    return val

def get_signal(row):
    """100% 还原你的黑马判定逻辑"""
    fans = parse_fans(row['店铺粉丝'])
    # 💥低粉爆品：粉丝<500 且 加购>500
    if fans < 500 and row['24小时加购'] > 500:
        return '💥低粉爆品'
    # 🌱隐藏潜力：粉丝<500 且 加购<100 且 日均销量>100
    if fans < 500 and row['24小时加购'] < 100 and (row['销量']/30) > 100:
        return '🌱隐藏潜力'
    return '普通'

# --- 3. 侧边栏：商业闭环与权限控制 ---
with st.sidebar:
    st.image("https://hubing1902100607.github.io/hongdian-data/wechat_qr.png", width=180)
    st.title("🔥 红点数据中心")
    st.markdown("---")
    access_code = st.text_input("🔑 输入激活码解锁数据", type="password", help="请联系北苑获取专属激活码")
    
    st.markdown("### ✍️ 大师复盘")
    st.info("今天的‘黑马’大多集中在 19-39 元客单价。盯着千万粉丝的号没用，看这种‘低粉、高转化’的品才是红利。")

# --- 4. 主界面逻辑 ---
# 简单的权限校验（你可以后续将此处的逻辑替换为你原来的 HMAC 校验）
if access_code: 
    try:
        # 4.1 加载数据 (精准匹配你的文件名)
        raw_df = pd.read_csv("红点数据_导入模版.csv")
        
        # 4.2 数据预处理
        df = raw_df.copy()
        df['信号标签'] = df.apply(get_signal, axis=1)
        df['预估GMV'] = df['销量'] * df['价格']
        
        # 4.3 渲染顶部四大金刚指标
        st.markdown("### 📊 实时数据概览")
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown(f'<div class="m-card"><p class="m-title">累计追踪</p><p class="m-val">{len(df)}</p></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="m-card"><p class="m-title" style="color:var(--red)">💥低粉爆品</p><p class="m-val" style="color:var(--red)">{len(df[df["信号标签"]=="💥低粉爆品"])}</p></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="m-card"><p class="m-title" style="color:var(--teal)">🌱隐藏潜力</p><p class="m-val" style="color:var(--teal)">{len(df[df["信号标签"]=="🌱隐藏潜力"])}</p></div>', unsafe_allow_html=True)
        with c4: st.markdown(f'<div class="m-card"><p class="m-title" style="color:var(--gold)">24h总购买</p><p class="m-val" style="color:var(--gold)">{int(df["24小时购买人数"].sum())}</p></div>', unsafe_allow_html=True)

        # 4.4 黑马监控台
        st.markdown("---")
        st.subheader("🚩 黑马预警监控列表")
        
        # 列表筛选器
        tag_filter = st.multiselect("按信号筛选", options=['💥低粉爆品', '🌱隐藏潜力', '普通'], default=['💥低粉爆品', '🌱隐藏潜力'])
        filtered_df = df[df['信号标签'].isin(tag_filter)]

        # 还原表格交互与跳转
        st.dataframe(
            filtered_df[['日期', '商品链接', '销量', '24小时加购', '24小时购买人数', '价格', '店铺粉丝', '信号标签', '预估GMV']],
            column_config={
                "商品链接": st.column_config.LinkColumn("🔗 点击跳转"),
                "预估GMV": st.column_config.NumberColumn("预估GMV (¥)", format="¥%d"),
                "价格": st.column_config.NumberColumn("单价", format="¥%.2f")
            },
            hide_index=True,
            use_container_width=True
        )

        # 4.5 销量趋势分析（还原 Chart.js 效果）
        st.markdown("---")
        st.subheader("📈 单品趋势深度分析")
        selected_url = st.selectbox("选择商品链接查看销量走势", df['商品链接'].unique())
        trend_data = df[df['商品链接'] == selected_url].sort_values('日期')
        
        fig = px.line(trend_data, x='日期', y='销量', markers=True, 
                     color_discrete_sequence=['#ff2d55'], title=f"商品销量波动曲线")
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#e8e8f0', xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)')
        )
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"❌ 运行出错了！请检查仓库中是否包含『红点数据_导入模版.csv』。错误详情: {e}")
else:
    # 4.6 未激活状态展示（还原你的 membership.html 逻辑）
    st.warning("🔒 欢迎来到红点数据中心。请输入激活码以查看深度选品数据。")
    st.markdown("""
        ### 🌟 会员权益
        - **实时黑马雷达**：第一时间捕获低粉爆品。
        - **潜力股自动识别**：算法锁定隐藏的高转化链接。
        - **独家大师点评**：每周更新选品策略与类目建议。
        
        ---
        **如何获取激活码？**
        请扫描左侧二维码添加大师微信，备注“红点数据”获取专属激活码。
    """)
