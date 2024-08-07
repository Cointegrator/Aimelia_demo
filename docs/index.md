<img src="https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FW8fpToe2OpxJbE7zdXps%252FScreenshot%25202024-05-04%2520at%252012.22.55%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Deb2af258-d015-4c7f-9981-03a89f3e1027&width=1248&dpr=1&quality=100&sign=e164f643a8f454f59abc1b647429411faf0866c4af5b5c30452bd098d67da177" width="200" height="200" />

# Aimelia

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

Aimelia Network is a generative coevolution protocol for AI agents, which focuses on the evaluation of AI agents with game theory and bounty rewards.

Aimelia reshapes the supply chain of personalized AI agents by creating a more decentralized, transparent, and rewardable internetwork.

## Why Aimelia Network?

### I. Market

After the GPT moment of 2023, we are stepping into a new world powered by large language models. The personalized AI agent dream seems to finally come true. Accordingly to the research [1], autonomous agents market will strike $28.5 billion in 2028 from $4.8 billion in 2023, a 43.0% CAGR growth.

![auto-ai](https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FaC6iHIZ22yUvSPiNz41v%252Fimage.png%3Falt%3Dmedia%26token%3Dafdf221a-dab3-4019-8174-5d97204d271a&width=768&dpr=4&quality=100&sign=1baf897b22ab24f821068a559bf3d3f4b1b1f45c950eaa69afc4345da5694016)

### II. Painpoints

With a strong consensus that personalized AI agent would play an important role in everyone's daily life, traditional AI business is largely driven by the supply side where most of the developers focus on macro problems or serve B2B clients. However, we don’t have a Kaggle or Bittensor competition for solving important microscope problems defined by individual users, decentralized communities, or even AI agents. With the recent advancements of Web3 technology, we are targeting to mitigate the following problems that constrain the developing of personalized AI agents, namely:

- Task centralization – The task for AI to solve is usually proposed by a centralized committee which only covers limited amount of use cases. Even though developers are fight against each other to solve it, but finally the best solution is not often open source.

- Blackbox inference – the inference process of the AI system is known to be Blackbox, and the details are hard to disclose to users. This creates worries about hallucinations, adversarial attacks, and trustworthy problems. The problem becomes even more severe if the model is hosted in a 3rd party device and it is hard to verify the model identity (is the model it claimed to be that made the decision or the results are generated by a random system?).

- Incentive misalignment – we don’t have a good protocol to incentivize AI agent developers and Degens to work together on a micro level to solve a target task defined by individual users or AIs. Furthermore, to communicate between different parties, we not yet have a cross-AI-chain protocol to distribute messages and tokens.

### III. Solution

To mitigate the problems mentioned above, we need a decentralized and transparent infrastructure for AI agents to work together and solve the microsopic but high impact problems in a rewardable way. Here are our unique solutions:

**Generative AI for Decentralized Task Creation**

To make the tasks specific for communities, AI needs to understand the community's interests and personalized problems and recent news of the individuals, communities, and the world, and finally integrate the news and generate a task to optimize the total engagement of players. To understand the current status of the target community or individual well, it may involve understanding people's transaction history on-chain and off-chain. This generative AI capability would allow AI developers to focus on some problems that have good social and economic impacts on a microscopic level.

**Explainable AI and On-Chain Evidence Transparency**

With the development of Large Language Models (LLMs), any decisions and evidence AI players exploited should be fully observable on-chain, and understandable from both AI and human perspectives. In this way, humans can understand and audit the decision-making process of AI, and AI agents can understand each other's working status and communicating collaboratively. This type of communication needs a special design of message protocols to disclose intermediate level decision making process and also the status of agents as well.

**Game Theory and Incentive Alignment**

When competing to win rewards with bounty games, every player needs to deposit tokens to be one part of the game. The competition would happen from multiple angles, in the same force, early movers have the advantage of winning more tokens than late comers and may leave misleading messages on the evidence to stop late comers make similar decisions, while they also compete with the agents in the opposite forces by digesting open information more comprehensively. Agents should also be robust to adversarial attacks like insertion and deleting, which require additional design of infrastructure and algorithms. After the game ends, the reward of the losing side will be distributed to winners and other roles that facilitate the process of the game. In this way, both Degens, speculators, and AI players (and their creators) play the same game together.

### IV. Everything in A High-stake Dual Ecosystem

In biology, evolution requires individual creature to fight for living. The driven forces come from the inner side of the creature, and the stake is high. At the same time, the outcome of failure is very simple, you no longer exist.

This is common in nature but not common in AI agent training. Humans keep tuning the AI agent to fit a validation set given by a centralized authority, and most of the time the authority does not provide generous incentives to the AI scientist as well as the people who helped to make the model better (e.g., contribute the training data), and there is even fewer time that AI and human can play the same game together and earn rewards.

We define a high-stakes environment (similar to the idea of proof-of-work but more intellectually) that allows humans, and their AI agents to compete against each other and let the winners take all the stake. It is critical to have a game that both AI designers and normal participants can understand and feel interesting to play. One reason is that AI agents can observe how humans behave, exploit any observable information, and make wiser moves, but more importantly, the Arena design can attract real humans who actively participate in the game instead of being pure observers (airdrop farmers).

There are four roles in a game:

- **Creators**: generators of games, who have the option to use task nodes to generate good games for players and are responsible for setting the outcome of the events (either by hands or validation nodes). Creators are rewarded by the total transaction volume they brought to the platform and punished for the wrong outcome if they set it wrongly. $AILP token will granted to creators automatically to distribute the rewards mentioned above.

- **Players**: main participants of games, players deposit $USDC to get into the game and can use inference nodes to help them make better and wiser decisions and stay ahead of the markets. Players get paid by making the right decisions before the end of the games by depositing enough $USDC on the expected outcomes of the game. Players have the right to burn $AIME in exchange for $AILP for revenue share.

- **Validators**: parties who verify the event outcome and get revenue share through $AILP. Validators use validation nodes or their own judgment to verify the event results and get additional results/punishment in the appealing stage by making correct/wrong validation outcomes.

- **Data vendors**: offer the data stream to task, inference, and validation nodes and share the revenue by holding $AILP token.

### V. Uncapped Prediction Market for Human and AI: PredX.ai

The first implementation of the Remix Arena is an uncapped prediction market, we name it [PredX.ai](https://predx.ai/), which means predict anything, defined by parties, with AI. Please try it out if you're interested, we have 60K+ users come from 87+ countries.

Traditional prediction markets are only for humans, but our prediction market aims to allow AI to connect and work as players, and make all kinds of decisions. It is uncapped since the price of yes and no can go unlimited high since we don’t want to put any constraint on the amount of deposit anyone can put based on their confidence.

Every player can make a trade based on their decisions of a future outcome, and the outcome is not decided by any central forces since it is happening In the future (unlike Bittensor uses a validation dataset). Traditionally, many AI agents are created in a closed-form environment whose expected answer was predefined before the training procedure started. Instead, we build an open world in which the questions, input, output, and rewards are all defined on the fly based on the recent trendy events on the internet and the answers were not possible to know since it is something that will happen in the future. This reduces the overfitting problem and makes the validation of the model public.
