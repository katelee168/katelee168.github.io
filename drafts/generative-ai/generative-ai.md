---
title: "Generative AI"
tags: [machine learning, datasets, generative ai, artificial intelligence, copyright, privacy, law]
---
<p align="right">May 29, 2023</p>

If you’ve seen the recent TikTok trend of transforming people into historical versions of themselves^[[Lensa AI climbs the App Store charts as its ‘magic avatars’ go viral](https://techcrunch.com/2022/12/01/lensa-ai-climbs-the-app-store-charts-as-its-magic-avatars-go-viral/)], or had a conversation with the chatbot ChatGPT you’ve interacted with generative AI. 
<!--In the last year, use of generative AI has exploded. People now use it to generate songs, pose as customer service representatives, and aid in drug discovery. -->
These impressive capabilities are driven by a comparable explosion of available data on the web–driven, in part, by all of us.
<!--Very large datasets have played a significant role in AI progress in general over the years, but have been absolutely critical to generative AI development. -->
Any media that you have posted publicly — words, images, videos, etc. — are fair game for being used as training data for these generative models.^[In this case, public does not mean places like Facebook’s friends list, but does mean Twitter and Reddit.]
This might not feel so different from how companies and websites already collect and train on your data, but the way generative models are trained means your data can be memorized and re-generated by generative models in new contexts. 
That’s because generative AI models are trained to exactly reproduce their training data. If the sentence “Mary had a little lamb” were in the training data, then the model would get rewarded more for choosing “lamb” after it sees “Mary had a little” than any other word (even though Mary probably also had other farm animals!). 
^[Generative models today are often general purpose, but you could imagine training a model specifically on human-written code (such as CoPilot), legal data, news, Tweets, speech, old-school films, and so much more. For the incredibly broad definition of data, there is an equally broad set of possible generative models that could be trained. ]

Welcome to an explainer series where we lay out the building blocks for generative AI models and shed some light onto the copyright issues that might arise. 

_Why copyright?_

Some of the data in training datasets may be copyrighted or have licenses attached. There is an active debate over whether training on copyrighted data constitutes infringement, and if an output that looks almost identical to the training data constitutes infringement. This debate centers [several](https://www.theregister.com/2023/01/16/stability_diffusion_lawsuit/) [recently-filed](https://www.smithsonianmag.com/smart-news/are-ai-image-generators-stealing-from-artists-180981488/) [lawsuits](https://githubcopilotlitigation.com/) related to [copyright](https://stablediffusionlitigation.com/) in generative AI models.

Generative AI models change the landscape of what content creation could look like and questions individual ownership over and our relationship to our data. Copyright is just one lens for individuals and corporations to maintain control over their content and monetize it. Privacy issues also arise when discussing data collection for generative models. Additionally, questions of labor and compensation may also arise alongside copyright issues. 

In this first chapter, we’ll build an understanding of how dataset creators juggle choices for what to include in a dataset, and the implications that their choices have for the generative AI model. In later chapters, we’ll discuss copyrightable works in the training data, the model generation process, whether training or outputs are infringement, and liability that model creators / distributors might have. 

> Jump to a specific chapter
> 
> 1. [**How is training data constructed?**](1-training-data.html)
> 2. **What is copyrightable?** [coming soon]
> 3. **How do you generate from generative AI models?** [coming soon]
> 4. **Is training infringement? Do outputs infringe?** [coming soon]