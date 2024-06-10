# Architecture

To have a complete pipeline of Aimelia.network, we need to have four different nodes connected, namely task node, inference node, validation node, and data node. They serve creators, players, and validators. Each node can be a centralized server or a decentralized AI blockchain that provides a specific type of service.

To let the nodes communicate, a tailored communication protocol is neccessary to support messaging and resource scheduling between nodes. The content encoded in the communication protocol might be different due to the source and target nodes, however, needs to mark down the stage of the system as well as the expected outcome in the payload.

Due to the advance of a large language model and high-performance blockchain, messaging passing cross-chain is possible to be written in plain language with proper implementation (considering the maximum transmission unit of each chain) and highly explainable to humans and AI agents.

## I. Nodes

There are four types of nodes in Aimelia Network:

![architecture](https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252FwfJSkCeZDPM1rf3ak9qd%252Fimage.png%3Falt%3Dmedia%26token%3Dd54dfc03-d702-4886-8e82-e885ee11d19d&width=768&dpr=4&quality=100&sign=92cef7cac65e992713ed1469fa45c40e756d9a938a2d59232cef28c4a72b7a73)

### Task node

- **User**: Creators uses task node as AI agents to help them create tasks for other players to trade. Task node can be an offchain device, an onchain agent, or an AI blockchain that can output a complete task string.
- **Function**: Create and assign objectives for both AI and human agents to solve, to maximize the subnet total rewards and minimize the CAC. Task nodes are designed for creators to improve their working efficiency.
- **Reward**: About 50% of $AILP token would be distributed to task nodes & creators after they create the task. In order to incentivize task creators to promote games in their communities, and earn transaction fees as a percentage of the market cap in the loser side.

### Data node

- **User**: creators, players, and validators can all select data nodes to provide real-time information to support decisions. Data nodes can directly work as information source to support each party make decisions as well.
- **Function**: AI or institutions that actively collect and reuse information to provide evidence for inference node to make decisions.
- **Reward**: Inference node would actively select data node to make decisions, and about 25% of $AILP token woud be distirbuted to the data nodes that make right decisions.

### Inference node

- **User**: Players employ inference nodes to make decisions. They can deposit the money to the inference nodes and delegate the work entirely to inference nodes to make decisions.
- **Function**: AI or humans draw conclusions from gathered knowledge (which can be auditable on-chain) and learn from each other's decision-making processes. Inference nodes are for players to make better decisions.
- **Rewards**: The inference node deposits $USDC to the expected outcome of the game based on the model output or personal judgment and earns $USDC based on the correctness of the judgment. The inference node can use $USDC to purchase $AILP for additional revenue-sharing rights. There will be a 10% $AILP token available for public sale.

### Validation node

- **User**: validators use validation nodes to verify the results of each game in an objective manner. Similarly, validators can delegate the work to validation nodes or can do the validation work by themselves manually. Creators can also use validation node to automatically announce the outcome of the game, but it is on his/her own risk of doing it.
- **Function**: AI or humans to check the correctness or consensus of conclusions. Validation nodes help validators to verify the results in the network. The reward is distributed if there is a high discrepancy between the claimed results and the results verified by validators.
- **Reward**: To encourage a routine check for every event outcome, 15% of $AILP token is distributed to all validation nodes, and each event can have up to 10 validation nodes.

## II. Communication protocol

Due to the four nodes that are connected by Aimelia.network might exist on different blockchains and even off-chain, it is important to have a tailored cross-chain messaging infrastructure to communicate key information across different nodes. The only two solutions we have for cross-chain communications are Wormhole and LayerZero. However, neither of them supports users to deposit tokens inside of the cross-chain system. So directly employing either LayerZero or Wormhole creates an additional layer of communication cost since these protocols need to support three ways of communication at the same time:

- The communication between AI chains (including blockchains holding task, inference, validation and data nodes).
- Deposit tokens ($USDC) from deposit blockchain (chain-0) to AI chains and exchange for $AIME and $AILP.
- Distribute rewards from the blockchain (chain-0) to other AI chains.

In addition, the message that is sent between AI chains might include model configurations, prompts, and agent status, which is very different from the normal payload that is supported by LayerZero and Wormhole. So we decided to have our own cross-chain messaging protocol for Aimelia. network.

One unique feature we have is we reuse the blockchain that users deposit tokens for Oracle and message communication. The benefits are multifolds, we not only saves the communicaiton cost and improve the efficiency of the system, we record the token transactions along with the evidences that the agent utlized together, which gauranteed the intermediate process is decentralized, transparent, and rewardable.

The architecture is shown as follows:

![comm-architecture](https://whitepaper.aimelia.network/~gitbook/image?url=https%3A%2F%2F516989656-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCCzRRAwggtrnfKBiYaGq%252Fuploads%252Fb7ER2tdSVt65R9SXhWsC%252Fimage.png%3Falt%3Dmedia%26token%3D5df0fb89-f2d3-4077-a643-ac8b3e1ebb99&width=768&dpr=1&quality=100&sign=98c817abda11f1f2567c1d0355c982350d0e30b12dfc55085a3914e0de4de09d)

Through this design, our protocol can be deployed to any L2 blockchain (chain-0) with a rollup technique implemented. By integrating the oracle and deposit function into the same blockchain, we can better leverage the existing token holders and liquidity on-chain and bring the AI solution to event creators and players to any blockchain.

## III. Message

In order to send messages to different AI layers, it is critical to tailor the message that is sent to different AI chains according to their underlying infrastructure. The message that passed across the blockchain should contain the following information:

```
1. Sender Address
2. Sender Blockchain ID
3. Sender type (data, task, inference, validation node)
4. Receiver public address
5. Receiver Blockchain ID
6. Receiver requested type (data, task inference, validation node)
7. Prompt for LLM
8. State of the system up to now
9. Possible Actions
10. Estimated Maximum payoff
11. Maximum computation cost
12. Response time
```

The #7 to #12 are key messages that decide the resource allocation in the target AI chains.
