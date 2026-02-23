import streamlit as st
import pandas as pd
import json
import time

st.set_page_config(page_title="Bittensor Explorer", layout="wide")
st.title("🧠 Bittensor Ecosystem Explorer")

API_KEY = st.secrets.get("TAOSTATS_API_KEY", "")

@st.cache_data(ttl=300)
def fetch_all_data(api_key):
    from utils.chain_data import get_stats, get_tao_price, get_subnets
    
    price = get_tao_price(api_key)
    time.sleep(1)
    stats = get_stats(api_key)
    time.sleep(1)
    subnets = get_subnets(api_key)
    time.sleep(1)
    from utils.chain_data import get_subnet_names
    identity = get_subnet_names()
    
    return {
        "price": price,
        "stats": stats,
        "subnets": subnets,
        "identity": identity,
    }

data = fetch_all_data(API_KEY)
price_data = data["price"]
stats_data = data["stats"]
subnet_data = data["subnets"]
identity_data = data["identity"]

# --- TIER 1: Market Overview ---
if price_data and stats_data:
    price = price_data["data"][0]
    stats = stats_data["data"][0]

    issued = int(float(stats["issued"])) / 1e9
    staked = int(float(stats["staked"])) / 1e9
    staking_ratio = (staked / issued) * 100

    st.subheader("📊 Market Overview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("TAO Price", f"${float(price['price']):,.2f}", f"{float(price['percent_change_24h']):.2f}% (24h)")
    c2.metric("Market Cap", f"${float(price['market_cap']):,.0f}")
    c3.metric("24h Volume", f"${float(price['volume_24h']):,.0f}")
    c4.metric("Staking Ratio", f"{staking_ratio:.1f}%")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Subnets", stats["subnets"])
    c6.metric("Accounts", f"{stats['accounts']:,}")
    c7.metric("7d Change", f"{float(price['percent_change_7d']):.2f}%")
    c8.metric("30d Change", f"{float(price['percent_change_30d']):.2f}%")

    st.divider()

# --- Build subnet name lookup ---
name_map = identity_data if identity_data else {}

# --- TIER 2: Subnet Table ---
df = pd.DataFrame()
if subnet_data and "data" in subnet_data:
    st.subheader("🔗 Subnet Overview")

    rows = []
    for s in subnet_data["data"]:
        nid = s.get("netuid", 0)
        emission_raw = float(s.get("emission", 0))
        emission_pct = emission_raw / 1e9 * 100 if emission_raw > 1 else emission_raw * 100

        rows.append({
            "NetUID": nid,
            "Name": name_map.get(nid, f"Subnet {nid}"),
            "Validators": s.get("active_validators", 0),
            "Miners": s.get("active_miners", 0),
            "Emission": round(emission_pct, 3),
            "TAO Flow (1d)": f"{float(s.get('net_flow_1_day', 0)) / 1e9:,.2f} τ",
            "TAO Flow (7d)": f"{float(s.get('net_flow_7_days', 0)) / 1e9:,.2f} τ",
            "TAO Flow (30d)": f"{float(s.get('net_flow_30_days', 0)) / 1e9:,.2f} τ",
        })

    df = pd.DataFrame(rows)
    df = df.sort_values("Emission", ascending=False).reset_index(drop=True)
    st.caption(f"Showing all {len(df)} subnets — scroll to see more ↓")
    st.dataframe(
        df,
        use_container_width=True,
        height=800,
        column_config={
            "Emission": st.column_config.NumberColumn(format="%.3f%%"),
        }
    )
else:
    st.error("Could not fetch subnet data")

# --- AI Chat ---
st.divider()
st.subheader("🤖 Ask Anything About Bittensor")

question = st.chat_input("e.g. Which subnets had the most TAO inflow today?")

if question:
    from utils.ai_chat import get_response

    live_data = {
        "tao_price": price_data["data"][0] if price_data else {},
        "network_stats": stats_data["data"][0] if stats_data else {},
        "subnets": df.to_dict(orient="records") if not df.empty else [],
    }

    ANTHROPIC_KEY = st.secrets.get("ANTHROPIC_API_KEY", "")

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            answer = get_response(question, json.dumps(live_data, default=str), ANTHROPIC_KEY)
            st.write(answer)
