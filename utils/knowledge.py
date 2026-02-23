BITTENSOR_KNOWLEDGE = """
=== BITTENSOR ECOSYSTEM KNOWLEDGE BASE ===

## Core Concepts

**Bittensor** is an open-source decentralized network where participants produce digital commodities (AI inference, compute, storage, etc.) and are rewarded with TAO tokens.

**TAO** is the native token of Bittensor. Max supply is 21 million (like Bitcoin). TAO is used for staking, registration, and value transfer.

**Subnets** are independent sub-networks within Bittensor. Each subnet defines a specific task or commodity (e.g., AI text generation, image generation, data storage). There can be 100+ active subnets. Each subnet has its own alpha token for staking.

**Miners** perform the actual work on a subnet (e.g., running AI models, providing compute). They earn rewards based on the quality of their output as judged by validators.

**Validators** evaluate miner output, assign scores/weights, and serve as gateways for users to query the subnet. They earn rewards based on staking and Vtrust.

**Yuma Consensus** is Bittensor's consensus mechanism that combines validator weights to determine miner rewards. It ensures fair distribution of emissions based on collective validator assessments.

## Tokenomics & Staking

**Emission** is the rate at which new TAO is created and distributed. Currently ~1 TAO per block (12 seconds per block). Emissions flow into subnet pools proportional to each subnet's emission percentage.

**Staking** means locking TAO to support a validator on a subnet. When you stake, your TAO is converted to the subnet's alpha token through the subnet pool. Staking ratio = total staked TAO / total issued TAO.

**Alpha Tokens** are subnet-specific tokens. Each subnet has its own alpha token. When you stake TAO on a subnet, it's converted to that subnet's alpha. The alpha price reflects supply and demand for that subnet.

**Subnet Pools** (liquidity pools) convert between TAO and alpha tokens using a constant product formula (like Uniswap). Each pool contains TAO and alpha. Price = TAO_in_pool / Alpha_in_pool.

**dTao (Dynamic TAO)** launched February 2025, introduced individual subnet tokens (alpha) and subnet pools, replacing the old flat delegation model.

## Key Metrics Explained

**TAO Flow** measures net TAO moving in/out of a subnet pool. Positive flow = investors buying alpha (bullish). Negative flow = investors selling alpha (bearish). This is the key signal for fund allocation decisions.

**Emission %** is the percentage of total network emissions directed to a subnet. Higher emission = more TAO flowing into that subnet's pool = more rewards for participants.

**Market Cap** for a subnet = circulating alpha supply × alpha price in TAO × TAO price in USD.

**Staking Ratio** shows what percentage of total TAO is staked vs free/liquid. Higher ratio = more network security and confidence, but less liquidity.

**Validators count** indicates decentralization. More validators = more decentralized evaluation of miners.

**Active Miners** shows how many nodes are performing work. More miners generally means more competition and potentially better output quality.

## Subnet Economics

**Registration Cost** is the TAO required to register a new subnet. It fluctuates based on demand. Part goes to the subnet pool, part is recycled (burned).

**Subnet Deregistration** was reintroduced September 2025. The subnet with the lowest EMA (exponential moving average) price gets deregistered when a new subnet registers. All alpha is liquidated and holders receive proportional TAO.

**Immunity Period** is 4 months from registration. During this time, a subnet cannot be deregistered regardless of price.

**Owner Rewards** are 18% of subnet emissions, going to the subnet creator/owner.

**Miner Rewards** are 41% of subnet emissions, distributed based on incentive scores.

**Validator Rewards** are 41% of subnet emissions, distributed based on stake weight and Vtrust.

## Investment Signals for Funds

- **Rising TAO Flow** into a subnet signals growing investor confidence
- **High emission + high TAO flow** = strong fundamentals and market demand
- **Developer activity** (GitHub commits) indicates active development
- **Validator count** stability indicates network health
- **Staking ratio trends** show overall network confidence
- **Subnet registration cost** trends show demand for new subnet slots
- **Negative TAO flow** may indicate profit-taking or loss of confidence
"""