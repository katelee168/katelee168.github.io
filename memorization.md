## Memorization @ Google Research, Brain Team

Our goal is to quantify and detect memorization with a eye towards improving privacy guarantees and learning more about how models learn. 

### We've shown that:
* we can extract more memorized examples from larger models \[[paper](https://arxiv.org/abs/2202.07646)\]
* examples with duplicates in the training data are easier to extract \[[paper](https://arxiv.org/abs/2202.07646)\]
	* removing duplicates dramatically reduces memorization and leads to language models that generalize better
* evaluating the upper bound of memorized examples is difficult because discoverability is difficult \[[paper](https://arxiv.org/abs/2202.07646)\]

### How can you find memorized examples?
*For more discussion on trade-offs of studied definitions of memorization, please see this blog. **TODO***

Given a model, how can we evaluate the amount of memorization?

Unfortunately, there is no current strategy to discover upper bounds of memorization. 

1. The simplest strategy to evaluate an 

What about identifying memorized examples that are seen just a few times?


Duplicate examples play such a large role in memorized examples, but we can identify examples that are seen a few times but have a large impact on the model through measuring counterfactual memorization. 

Protecting privacy in unstructured data like language is extra challenging. 


