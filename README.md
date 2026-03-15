# Bittensor Ecosystem Explorer

**Real-time dashboard for monitoring the Bittensor network: TAO market data, subnet economics, emission flows, and an AI analyst that answers questions against live on-chain data.**

Pulls live data from the Taostats API and renders market overview, subnet rankings by emission, TAO flow tracking, and a conversational AI layer that can query the dashboard data directly — built for fund-level ecosystem analysis.

![Demo Screenshot](assets/demo-screenshot.png)
<!-- Replace with actual screenshot -->

**[View Live →](your-streamlit-url)**

---

## What It Covers

**Market Overview** — TAO price, market cap, 24h volume, staking ratio, 7d/30d price changes, and active subnet count sourced from Taostats.

**Subnet Table** — All active subnets ranked by emission share, showing validator/miner counts and TAO flow (1d/7d/30d). Positive TAO flow signals investor inflows; negative signals selling pressure.

**Emission Charts** — Top 10 subnets by emission percentage visualized via Plotly.

**AI Analyst** — Chat interface backed by Claude Sonnet, injected with live dashboard data and a curated Bittensor knowledge base (dTAO mechanics, subnet economics, Yuma Consensus, investment signals). Responds in 2–3 sentences, Bloomberg-terminal style — no fluff.

## Architecture

```
Taostats API  → Price, network stats, subnet data
GitHub raw    → Subnet name registry
                    ↓
              Streamlit (cached, 5-min TTL)
                    ↓
         ┌─────────┴──────────┐
         │                    │
   Dashboard UI          AI Chat
   (metrics + Plotly)    (Claude + knowledge base + live data)
```

The AI chat layer is the interesting part: it serializes the full dashboard state (price, network stats, subnet table) as JSON and passes it as context alongside a domain knowledge base covering dTAO mechanics, emission economics, and fund-level investment signals.

**Stack:** Streamlit · Taostats API · Claude Sonnet (Anthropic) · Plotly · Pandas

## Project Structure

```
├── app.py                # Main dashboard + AI chat
├── utils/
│   ├── chain_data.py     # Taostats API client (with rate-limit retry)
│   ├── ai_chat.py        # Claude integration with live data injection
│   └── knowledge.py      # Bittensor domain knowledge base
├── test_api.py           # API connectivity test
└── requirements.txt
```

## Quickstart

```bash
git clone https://github.com/your-repo/bittensor-dashboard.git
cd bittensor-dashboard
pip install -r requirements.txt
```

Add secrets to `.streamlit/secrets.toml`:

```toml
TAOSTATS_API_KEY = "your_key"
ANTHROPIC_API_KEY = "your_key"
```

```bash
streamlit run app.py
```

## Built By

**[Karan Rajpal](https://www.linkedin.com/in/krajpal/)** — UC Berkeley Haas MBA '25 · LLM Validation @ Handshake AI (OpenAI/Perplexity) · Former 5th hire at Borderless Capital
