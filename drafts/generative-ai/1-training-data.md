<!--Training data [feedback]-->

# Chapter 1: Training data {#intro}

<p align="right">
by [Katherine Lee](https://katelee168.github.io/) and [Daphne Ippolito](https://daphnei.com/) </br>
April 28, 2023
</p>

The training data used to develop generative models has a direct impact on their outputs (aka *generations*).
If there are no Garfield comics in a model's training data, what are the odds of it spontaneously generating a Garfield comic?
Good selection of training data is the most important way creators can control the risk of copyright and privacy infringements in the resulting, generative model. 
^[We should couch this by saying that training dataset design is the _current_ most important set of choices model creators have. There are other models in the works that are trying to reduce copyright and privacy infringements by attributing generations to specific examples in the data, or by adding noise to obscure individual data points (differential privacy), or by limiting the scope of a model to an application where copyright and privacy are less of a concern (for example, Disney training on scripts where they own all the copyrights).]
The sheer amount of data required for training modern-day generative model makes it impossible for dataset creators to interact with each item in the dataset, and thus impossible to know exactly the content, source, and context of each item in the dataset. 
For example, a dataset creator might be able to answer the question: “How many Garfield comics are there in the training data?”, but they might not be able to answer the questions: “How many fan or parody Garfield comics are there in the training data?” 


In this chapter, we discuss datasets of the not-so-distant past (the late 1990s and early 2000s) and how datasets and dataset collection practices have changed.
Then, we discuss what the choices data curators make to create modern-day, generative-AI datasets. 
Finally, we acknowledge both the difficulty in making educated choices and the real impact those choices have on the resulting models. 


### Table of Contents

1. [**A Brief History**](#early-datasets): Early datasets used for generative modeling were much smaller, had denser annotations, and were more likely to be manually curated. 
2. [**Today’s Datasets**](#today-datasets): Today’s datasets are on the scale of multiple terabytes. It’s impossible to annotate or fully understand these datasets. 
3. [**Data collection**](#data-collection): Datasets collection requires making a lot of choices about what data is relevant. The impact of those choices on generations from the model is not well understood. 
4. [**Data curation**](#data-curation): Data curation requires understanding the goals of the models, which are often un-, or under-specified, and the cultural context of the data. Again, the size of the datasets can make this a challenges.
5. [**Conclusion & Next: Copyright and Training Data**](#next)

## A Brief History {#early-datasets}

> Early work in generation didn't "learn" from data. 
> As statistical models have become more capable through computed and increased dataset sizes, annotations have come in and out of favor to provide intermediaries to better train or evaluate generative models.
<!-- > as models became better able to represent unstructured data. As models got better, the need to evaluate them also grew, prompting an resurgence of heavily annotated datasets.  -->


The earliest work in language generation didn't "learn" from data.
Early chatbots, such as [ELIZA](https://dl.acm.org/doi/10.1145/365153.365168) (1966) and ALICE (1995), and early work on [novel](https://minds.wisconsin.edu/handle/1793/57816) (1973) and [story](https://www.proquest.com/docview/304049508) (1993) generation, used techniques from classical artificial intelligence to generate text based on hand-crafted rules and grammars.

Similarly, early work on photo-realistic image generation didn't use any grounding in photography.
Rather, the field of Graphics focused on building mathematical models of 3D objects, such as the famous [Utah teapot](https://graphics.cs.utah.edu/teapot/) (1975), and then rendered them onto a 2D images, writing algorithms to mimic the shadowing and light effects of the real world.
Other work used procedural algorithms to generate realistic textures TODO(add more here).
TODO: add ben poole's work here on making 3D renderings from photographs.


<figure style="text-align:center;">
  <img src="images/Utah_teapot.png" alt="The Utah teapot" style="width:37%;">
  <figcaption>The Utah Teapot was one of the first 3D models constructed of a real-world object. Early work in Graphics sought to render 3D objects like the teapot realistically in 2D images.</figcaption>
</figure>

We'll first discuss some historical language datasets then return to image datasets in a later [section](#image-generation).

### Language datasets

Early monolingual datasets, such as the Brown Corpus and the Penn Tree Bank, were collected from literary, government, and news sources, and were densely annotated with linguistic structure, such as parts-of-speech^[Is a word a noun, or verb, or adverb?] and syntax^[Syntax is the hierarchical structure of a sentence.] annotations.
Early work in natural language processing  assumed that building a language understanding system would require encoding this type of linguistic knowledge and mechanically applying it. 
^[For example, one might use linguistic structure to understand that in the sentence "The dog fetched the ball.", "the dog" is a noun phrase serving as the subject of the sentence. Additionally, we might infer from context that a dog is the sort of thing that is more likely to fetch than a ball, and that a ball is the sort of thing that a dog might fetch.]
Building annotated datasets was a labor-intensive process, often this was completed by professional, highly skilled annotators at organizations like the Linguistic Data Consortium, though some datasets like TODO chose to crowdsource annotations from non-experts.

The shift towards larger datasets was driven by the growth of electronic records and the internet.
Some notable datasets include [English Gigaword](https://catalog.ldc.upenn.edu/LDC2003T05) (2003), sourced text from English newswire; the Enron Emails dataset (2001), sourced from emails released by the US federal government during its investigations of Enron;and the [One Billion Word Benchmark](https://arxiv.org/abs/1312.3005) (2013), sourced from government documents and newswire.

All of the datasets mentioned so far have a trait in common--the source material was either public record or explicitly licensed for research usage.
However, as it became apparent that bigger datasets led to superior models of language, and the field of NLP saw rapid advancements in the algorithms and computing hardware needed to efficiently processing large amounts of data,  efforts to build responsibly-sourced and hand-curated datasets could not keep with with the demand for big datasets.

It wasn’t just the growth of the internet that drove the growth in dataset sizes, increased computational power (a.k.a. compute) and new model designs meant that statistical models increased in capacity and became better at finding patterns in unstructured data. 
These shifts also decreased the need for annotations since models were able to pick out patterns in the data that corresponded with tasks without relying on data that was curated for the task. 

For example, some of the earliest generation applications to work with large text corpora were machine translation.
From multilingual data sources such as United Nations documents and news sites, dataset creators assembled datasets of two or more languages of the same topics. Some of these datasets had aligned text (a specific sentence in two or more languages), but some datasets, like TODO were simply transcripts of the same meeting in multiple languages--these were effectively loosely annotated.
These datasets were used to build statistical language models which would learn to output translations for any input sentence.

In the 2010s, we saw the rise of web-scraped datasets.
The [Book Corpus](https://arxiv.org/abs/1506.06724) (2015) scraped 11k books from Smashwords, a website for self-published e-books; the [WritingPrompts dataset](https://aclanthology.org/P18-1082/) (2018) scraped the r/writing-prompts subReddit;
We also saw increasing use of crowd-sourced datasets, such as Wikipedia and OpenSubtitles, where it can't always be validated that content creators had the rights to upload the text that they did.
For the most part, these datasets were not annotated with the rich linguistic information which accompanied older datasets.
Not only were these annotations infeasible to collect on massive datasets, but advancements in machine learning methods made them unnecessary for strong performance on many language tasks.
^[Up until 2016, Google Translate used phrase-based translation which broke sentences into linguistic parts to translate separately. These techniques have [since been replaced by neural networks](https://ai.googleblog.com/2016/09/a-neural-network-for-machine.html).]

Most recently, we have seen the growth of datasets which don't just collect documents from a single web domain, but instead attempt to sample from the entirety of the web.
Some prominent examples are [RealNews](https://rowanzellers.com/grover/) (2019), [C4](https://c4-search.apps.allenai.org/) (2019), and [WebText](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf) (2019)
All state-of-the-art large language models are trained on this type of data.

There are also large datasets containing proprietary data. Those datasets may be annotated with user actions, such as number of stars for Amazon Reviews, or Netflix recommendations. [Amazon’s Review dataset](https://nijianmo.github.io/amazon/index.html), released dataset in 2018, contains 233.1M examples with customer ratings, and [Netflix’s recommendations dataset](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data) contains 100M customer ratings. Other popular datasets in this vein are [IMDB movie reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews), or the [Google Books N-gram corpus](https://en.wikipedia.org/wiki/Google_Ngram_Viewer) (2.2 TB of text!).

### Image Generation

Until relatively recently, most of Machine Learning with image data focused on classification tasks than image generation.
Early datasets include [MNIST](https://www.lri.fr/~marc/Master2/MNIST_doc.pdf) (1999), which consisted of 60,000 black-and-white images of digits; [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), which contained 60,000 photographs of objects from 10 classes, including airplanes, frogs, and cats; and Imagenet (2009), which contains over 14 million images from 1,000 classes.
Deep Learning researchers relied heavily on these datasets to develop methodologies for image classification, and early work on machine learning-powered image generation, including [generative adversarial networks (GAN)](https://arxiv.org/pdf/1406.2661.pdf) (2014) and [denoising diffusion models](https://dl.acm.org/doi/abs/10.5555/3495724.3496298), followed suit.
For many years, the diversity present in large datasets like Imagenet confounded image generation approaches.
Large but more narrowly-scoped datasets allowed for the development of models with higher fidelity generations.
Prominent datasets included [Celeb-A](https://openaccess.thecvf.com/content_iccv_2015/html/Liu_Deep_Learning_Face_ICCV_2015_paper.html) (2015) which contained 200k close-up images of faces; [Caltech-UCSD Birds](https://vision.cornell.edu/se3/caltech-ucsd-birds-200/) with over 11k bird photos; and [Oxford Flowers 102] with 1k flower photos.



<figure style="text-align:center;">
  <img src="images/mnist.png" alt="Examples from MNIST" style="width:37%;">
  <img src="images/laion-cats.jpeg" alt="Examples from LAION" style="width:37%;">
  <figcaption>**left**: Examples from [MNIST](https://en.wikipedia.org/wiki/MNIST_database). **right**: Examples from [LAION 5B](https://laion.ai/blog/laion-5b/). </br>  Note the uniformity of the images in MNIST vs. the varying aspect ratio and image quality in LAION. Additionally, LAION images come with much longer captions that don’t always exactly describe what is in the image, whereas labels associated with MNIST images are the number written in the image.</figcaption>
</figure>

Of course, the most exciting models today don't just generate an image from a single class identifier like "bird" or airplane."
Models like Stable Diffusion or Imagen can parse complex natural language descriptions to generate entire novel photorealistic images.
TODO: include an example image
Good text-to-image models require training images with rich captions describing them.
Early [GAN-based text-to-image models](http://proceedings.mlr.press/v48/reed16.pdf) collected human-written descriptions of the images in the Birds and Flowers datasets.
[MS-COCO](https://cocodataset.org/#home) (2015), a dataset intended for image captioning research, was also co-opted to be used in reverse, its examples flipped to generate an image from a caption.


Like in Language research, it quickly became clear that larger datasets resulted in superior models.
In addition, training datasets needed to be high-resolution in order to create high-resolution, high-fidelity generations.
[LAION 5B](https://laion.ai/blog/laion-5b/) (2022) met this need with a dataset of over 5 billion image-text pairs, creating by sweeping over the websites in the Common Crawl, collecting images with detailed [alt-text](https://www.accessiblepublishing.ca/a-guide-to-image-description/) descriptions.
^[Alt-text descriptions of images are an accessibility feature intended for situations where an image cannot be rendered. For example, visually impaired people using screen readers will read alt-text in lieu of seeing the image.]
This is the dataset most state-of-the-art open-source text-to-image models are trained on.

TODO OTHER IMAGE

<figure style="text-align:center;">
  <img src="images/imcl2016_fig1_v3.png" alt="Early GAN-generated images" style="width:37%;">
  <img src="images/stablediffison_bird_flower.jpeg" alt="Examples from LAION" style="width:37%;">
  <figcaption>**left**: Generations from one of the first text-to-image synthesis [papers (2016)](http://proceedings.mlr.press/v48/reed16.html). **right**: A generated image from DALL-E 2, a state-of-the-art text-to-image model.</figcaption>
</figure>





## Today’s datasets {#today-datasets}

> Today’s datasets are on the scale of multiple terabytes. 
<!-- > It’s impossible to annotate or fully understand these datasets.  -->
> Fully annotating and understanding these datasets is impossible.
> Annotations are used either to better ensure or validate that particular ideas or structures are learned from the data. 

The datasets used to train today’s large language models are massive and predominantly contain data scraped from the web^[The Pile, ROOTS, and Chinchilla all combine data scraped from the web with additional data sources.]. The Pile and C4 are both 800GB; [ROOTS]((https://huggingface.co/bigscience/bloom#training-data)) was 1.6TB of pre-processed text, and the unreleased dataset Chinchilla used for training is 5.3 TB^[The number reported in their [paper](https://arxiv.org/abs/2203.15556) was 1.4T tokens, or 4x the training data for a different language model, Gopher, which used 300B tokens. For [Gopher](https://arxiv.org/abs/2112.11446), they sampled 12.8% of the dataset _MassiveText_ that contains 10.5TB of data. 0.128 * 4 * 10.5TB = 5.3TB]. 
It’s impossible for dataset creators to read each individual data point let alone annotate them.

This automated collection process can obscure important context such as the provenance of the data. 
For data in these large, web-scraped datasets, dataset creators might know that a paragraph of text is from a particular website, but that won’t necessarily tell us who the author of the text is, or who the photographer or artist is and whether they have permission to post the content.
For example, chat logs are typically between two or more people. Both people do not need to consent for one person to put that chat log somewhere publicly where it could become part of the dataset. The chats could also become public through a data leak, or as a result of malicious action, for example, personal chats were leaked during the GamerGate harassment campaign^[GPT2, another language model, generated a conversation between two real individuals using their usernames. This conversation wasn’t exactly as it appeared in the GamerGate harassment campaign, but was about the same topic. More on this topic in [this blog](https://bair.berkeley.edu/blog/2020/12/20/lmmem/) and [this paper](https://dl.acm.org/doi/fullHtml/10.1145/3531146.3534642).]. 
The entire movie *The Fast and the Furious*, could become part of a dataset without the dataset creator’s knowledge because someone decided to tweet out the entire movie in [two minute clips](https://mashable.com/article/twitter-copyright-full-movies).
^[Other copyright concerns could arise. For example, there are instances [license laundering](https://en.wikipedia.org/wiki/Licence_laundering) on Github: individuals taking Github repositories that have a license and reposting it without the original license.]
Additionally, without provenance and inferred cultural context, data may look unexpected. For example, a generative AI model may refer to "sex" as "seggs" because individuals online have adapted to censorship by using the homophones, such as "seggs", to discuss sensitive topics.

In contrast, the provenance of MNIST is much more clear. 
The dataset was built by *M*ixing two datasets from the *N*ational *I*nstitute of *S*cience and *T*echnology's datasets of handwritten numbers one written by high school students and the other by employees at the US Census Bureau.

Additionally, we know how many and which examples are labeled incorrectly in the MNIST^[[Northcutt, 2019](https://arxiv.org/abs/1911.00068) investigated mislabeled images in MNIST. Anecdotally, Yann LeCunn has been overheard claiming he knows every mislabeled image in MNIST.] because MNIST has been extensively studied^[Over 6000 papers cite MNIST directly and a Google Scholar search returned 76,900 articles that mention MNIST.  MNIST has become synonymous with “small, standard dataset” so other datasets like Fashion-MNIST, which has photos of clothing, also appear in the search results.].
This was possible both because MNIST was an extremely popular dataset over the course of it's nearly 25 year history, and because it's much, much smaller, than today's datasets (97,500x smaller than LAION^[LAION-5B has 5.85 billion text-image pairs. MNIST has 60,000 examples.]).
<!-- since MNIST is one of the oldest and most extensively studied machine learning datasets (and TODOx smaller than LAION,  -->

The massive size of today's datasets makes it a challenge to identify potentially mislabeled or misleadingly labeled images--there are often more than one way for images to be labeled, leading to misleading or incomplete labels
^[There is some work investigating mislabeled [examples](https://arxiv.org/abs/2208.11695), but this work is rarely done compared with the number of existing datasets.]. 
For example, LAION captions may not describe the content of the image at all, or may not accurately describe the image the LAION captions may not even accurately describe the content of the image and could even be written in multiple languages. 

That being said, modern models are remarkably capable of performing tasks _in spite_ of misleading or mislabeled examples^[TODO Cite chiyuan's randomness paper]. 
They are remarkably capable of also performing tasks that they weren't explicilty trained to do. 
<!-- That being said, modern models are remarkably capable of performing tasks that they were not explicitly trained to do.  -->
Many generative language models are trained to generate the next word in the sentence^[Other modern LMs can be trained with other objective functions, like masked language modeling (also called span corruption), or the UL2 loss. More info [here](https://ai.googleblog.com/2022/10/ul2-20b-open-source-unified-language.html)] ^[Many generative image models are trained to reconstruct a given training example.]. 
However, modern models can perform tasks like reversing a sentence^[Try it yourself in [ChatGPT](https://chat.openai.com/).]! 
Providing examples of what “reversal” means in the prompt to the model can help the model understand the pattern, but models are not successful every time and are very sensitive to the format of the prompt.

Annotated datasets can help evaluate the effectiveness of models on a task we care about and also to augment un-annotated data to make those tasks easier. 
In that sense, the LAION captions could be thought of as "annotations" of the image dataset that enable the model to more effectively learn the contents of the images--the captions would be very difficult to learn without the "annotated" captions collected. 
Here is another example: if "doctor" always appears in the training set with the pronouns "he/him,"" the model trained on that dataset would pick up that pattern and not use any other pronoun. 
Annotated text could be used to measure this issue by testing explicitly measuring pronoun and profession correlations. 
In the late 2010s, researchers created many annotated datasets to evaluate models, including: [Big-Bench](https://github.com/google/BIG-bench), [GLUE](https://gluebenchmark.com/), [SuperGLUE](https://super.gluebenchmark.com/), and [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/).
All of these datasets feature leader-boards to compare trained models. 
Today, model alignment through reinforcement learning through human feedback^[Reinforcement Learning through Human Feedback (RLHF) is a technique for providing feedback to the model about how "good" a generation was. This is currently used in popular models such as ChatGPT.] could also be thought of as providing annotations to the data to steer generation in a particular way.

These annotated datasets are commonly used for evaluation, though the distinction between evaluation and training is not super clear as the datasets are often benchmarks that come with a training and test set. It’s common practice to train on the data from the training set of the evaluation benchmark then test on the evaluation benchmark’s test set.

TODO: some better transition here? 


<!-- Today’s language models, just like today’s image models, use many fewer annotations and rely more on computational power to discover statistical patterns.
It wasn’t just the growth of the internet that drove the growth in dataset sizes, increased computational power (a.k.a. compute) and new model designs meant that statistical models increased in capacity and became better at finding patterns in unstructured data. 
These shifts also decreased the need for annotations since models were able to pick out patterns in the data that corresponded with tasks without relying on data that was curated for the task.  -->




## Data collection {#data-collection}

> Datasets collection requires making a lot of choices about what data is relevant. The impact of those choices on generations from the model is not well understood. 

The balance of genres in a dataset affects the model's knowledge and ability. 
For example, should the dataset be primarily one language? Should it include an equal balance across as many languages as possible? What about an unequal balance across languages? That question actually hides even more choices. If an English sentence includes a single Italian word, is that sentence English or Italian? What about the sentence, “I walked from campo dei fiori to santa Maria degli angeli?” Additionally, many situations are contextual and cultural. Before René Magritte’s 1929 painting, we would have said “Ceci n'est pas une pipe” was French, but today, it would also be commonly understood by many English speakers.
As much as we would like to back each decision on what data to include by science, it’s cost- and compute- prohibitive to run a different experiment for each decision. 
Thus many of these decisions are just choices the dataset creator makes.


<figure style="text-align:center;">
  <img src="images/pipe.jpeg" alt="Ceci n’est pas une pipe" style="width:50%;">
  <figcaption>Est-ce French? Is this l'anglais?</figcaption>
</figure>

Even within one language there are many varieties of text that come from different sources. Data from Twitter, code repositories, personal blogs, advertisements, FanFiction, PasteBin dumps, text for search-engine optimization, and so on, are going to look very different.
Dataset creators make assumptions about the content of each domain and often choose to include or exclude entire domains. 
For example, Wikipedia is a popular source of data because it contains curated articles about a diverse array of topics. If the dataset creator wanted to create a model that was able to give coding advice, they may choose to include StackExchange or Github data as well.
^[Github contains far more than just code. For example, many repositories also contain Readmes written in prose. Additionally, since many websites and blogs are hosted on Github, Github can also contain personal, narrative stories.]
But Wikipedia isn’t conversational. If interactions with the generative model are meant to feel fluid and natural, then the dataset creator may choose to add chat data, such as Youtube Subtitles, HackerNews conversations, or Twitter. 

In one popular language dataset, the Pile, the dataset creators chose to include multiple “academic” datasets, like PubMed, ArXiv, and FreeLaw, and code from Github. This means that models trained on the Pile will have seen medical literature, legal literature, and code. A model not trained on code would have a much harder time generating code^[This doesn't mean that models not explicitly trained on code can’t generate code. Webscraped data is not clean, and there will inevitably be some code mixed in.].




<figure style="text-align:center;">
  <img src="images/pile-composition.png" alt="Data composition within the Pile" style="width:75%;">
  <figcaption>[The Pile](http://arxiv.org/abs/2101.00027) is made up of many smaller datasets. Many of these components are web-scrapes focused on a specific domain, such as Wikipedia, StackExchange, USPTO (United States Patent and Trademark Office), and ArXiv. Some components, like Enron Emails,  EuroParl^[“Proceedings of the European Parliament in 21
European languages from 1996 until 2012” ([The Pile](http://arxiv.org/abs/2101.00027)).], and Project Gutenberg^[Collection of out-of-copyright books available online.] are not explicitly scraped from the web.</figcaption>
</figure>

There have been some efforts within the ML community to encourage dataset creators to document the choices they made. 
A common choice is to create a [datasheet](https://arxiv.org/abs/1803.09010) which collects information about how the data was collected, the motivation behind it, any preprocessing that was done, and future maintenance plans.^[Many datasets available on HuggingFace (a popular open-source model and dataset repository) now have datasheets attached to them.]
As an example, this is the Pile’s [datasheet](https://arxiv.org/pdf/2201.07311.pdf). 
However, even an extensive datasheet like the Pile’s still still answers only a tiny fraction of the questions you could ask about what data it contains, why it was included, and how it was collected.
Additionally, many companies don’t release many details about their proprietary datasets.
^[For example, we don’t know much about the training data for ChatGPT, nor the difference between ChatGPT’s and [Claude’s](https://www.anthropic.com/earlyaccess) datasets. However, to the extent that similarity between training data and the user’s downstream task has an impact on the generative AI’s performance on the tasks, then companies should feel motivated to document and release additional information about what was in the training data to enable users to choose the right API for their application.]

## Data curation {#data-curation}

> Data curation requires understanding the goals of the models, which are often un-, or under-specified, and the cultural context of the data. Again, the size of the datasets can make this a challenge.


While dataset curators frequently say they want “clean data,” the term is a misnomer. Instead, dataset curators typically mean that they want a dataset that creates a “good model.”
“Good” is extremely un- and under-specified which makes many possible choices of data valid. 
^[Many generative AI models are referred to as “general purpose models.” Models are never general because data and modeling choices create preferences and limitations, however, the intent of the creators is to make the model as general as possible.]
Some model creators will also specify a “good model that doesn’t cause harm.” Let’s get a little more specific with that and take “don’t generate toxic content” as an illustrative example. It’s an easy goal to state but hard to implement. 

What constitutes "toxic" content  is ill-defined and constantly evolving, and classifications of toxicity can be correlated with other aspects of text, such as sexual explicitness.
^[[Prior work](https://maria-antoniak.github.io/resources/2021_acl_bad_seeds.pdf) demonstrates how biases can seep into bias measurements through choices in the topics.]
^[The [Perspective API](https://medium.com/jigsaw/better-discussions-with-imperfect-models-91558235d442) is one API that tries to identify “toxic” content. Again, what is considered “toxic” is context dependent, and in this case may be better explained as “stuff you don’t want advertisements associated with.”]
For example, the Texas’ Liberty County Vindicator posted the full text of the Declaration of Independence and [Facebook’s moderation flagged it as hate speech](https://www.washingtonpost.com/news/the-intersect/wp/2018/07/05/facebook-censored-a-post-for-hate-speech-it-was-the-declaration-of-independence/]).
Additionally, different individuals or groups may have different interpretations of the same text, complicating the process of deciding what data to include and exclude. 
For example, the LGBTQ community centers sexual orientation and sexual experience. Filtering out data related to sexual orientation and sexual experience could inadvertently remove data related to the LGBTQ community.
^[[This paper](https://arxiv.org/abs/2104.08758) provides an example of this in the dataset C4.] ^[One way to approach this challenge is to adopt a more flexible and inclusive approach to data collection and analysis. This may involve working closely with individuals or groups who have expertise in the cultural context under study and being open to multiple perspectives and interpretations. Overall, it is important to recognize that cultural data is often fluid and dynamic, and our understanding of it may change over time. Therefore, any process for determining what data to include and exclude must be adaptable and open to revision as new insights emerge. It may also involve acknowledging the limitations of quantitative methods in capturing the full complexity of cultural data and being open to using qualitative approaches that allow for more nuanced and contextualized analysis.]
Whatever process we use must be adaptable and open to revision. We can never have a black and white process of determining what data to include and exclude because we are dealing with cultural connotations that resist quantification and objectivity.

However, the scale of the datasets encourages dataset creators and curators to use automatic methods to decide on mass what data to include or remove. 
For example, a secondary model trained with labels for “toxic” or “low-quality” data could be used to label all data in a dataset. This present-day annotation is much less structured than prior, linguistic annotations. 
Even with data curation, the training data for the largest generative models are still minimally curated compared with standard dataset collection practices from pre-2017.
^[It’s not a secret that most datasets are crap. And by crap, we mean that they’re incredibly messy. In all data science, the first step is to “clean” and explore the data. Of course, “crap” is a catch-all term, and the ways in which data can be messy varies widely. However, whenever you’re dealing with large collections of data that are not cost-effective to manually curate and inspect, the dataset will necessarily contain anomalies and errors. Even if it were possible to manually curate and inspect the entire dataset, it would be impossible to find all possible patterns across the data because we are 1. All humans who have limited brain capacity and whose background makes it easier to identify some patterns and not others, and 2. Some patterns are not semantically meaningful to humans.]

Unfortunately, even if we agreed on what was “toxic” there isn’t a clear, technical solution for how to reduce toxic content. Some researchers propose removing any data deemed “toxic,” and other researchers disagree arguing that it’s better to include some “toxic” data so that models are able to identify and stop generation of “toxic” content [**TODO**, citations] and argue that we should control outputs of models, not inputs.
Labeling data for concepts like “toxicity” can help evaluate generations from models.
These annotations need not be structured as a dataset, and some creators of generative models prefer to directly annotate the media produced by the model. This labeled data can also be useful for future training purposes, as it can be used to train classifiers based on the new labels.

The lack of technical consensus here is often not for lack of desire but rather a reflection of both how many of these questions are societal and cannot be answered technically, and also of the computational cost required to investigate these questions.
The process of testing whether to include a slice of data can involve training a model with and without that slice of data. That’s called ablation testing. Unfortunately, today’s models are massive (billions of parameters) and can cost millions of dollars to train. Also, unfortunately, testing with smaller models doesn’t always have the same results as testing on larger models making straightforward testing cost-prohibitive.
^[Models develop capabilities at larger sizes ([Wei, 2022](https://openreview.net/forum?id=yzkSU5zdwD))]
This means that model creators can’t afford to test every possible definition of “toxic” or every combination of “include/exclude” for different types of data.

And yet, including or excluding, and identifying “toxic” content is just one of many, many choices dataset curators have to _just make_.
As we discussed before in the section [_Data Collection_](#data-collection), dataset creators must also decide whether to include mostly text in one language or whether to mix in multiple languages. The line between dataset curation and creation isn’t well-defined and people can use either term to refer to the same acts.
^[I’ve arbitrarily used data collection to refer to adding data to the dataset and data curation to be filtering data out of the dataset. Ultimately, adding and removing data are just a series of choices dataset creators and curators can make about what can be included. Dataset curation is a part of the dataset creation process. Additionally, the choice of adding particular sub-datasets means choosing to exclude other sub-datasets, which is also a curation choice. The reason to use two terms, dataset creator and dataset curator, at all is because often datasets are created and then filtered later on by a different set of people. ]
Datasets can also be curated differently depending on the application at hand.
For example, another choice dataset curators may make is whether it’s better to include mostly chat logs when creating a chat bot or if dataset creators should also include news articles or code.
All this is to say that dataset collection and curation is an active area of research for which the answers depend heavily on the open-ended goals of generative modeling.
^[This is not to say that “open-ended” is necessarily bad. One exciting result from generative AI releases has been seeing the multitude of ways people have used the systems. Exciting, and perhaps unintentional.]

## Conclusion & next up: Copyright and Training Data {#next}

What dataset creation really boils down to is a set of choices. Datasets could look different, and they _were_ different. But today’s datasets are shaped by the present set of influences: model sizes, availability of data and compute, open-ended goals (and sometimes, a lack of desire to specify a specific goal), difficulty defining societal concepts, and business incentives.

We started this journey discussing how the choices in training data can raise copyright issues. Next in this series on generative AI, we’ll discuss what sorts of copyrightable works could be included in the training data, why they may have ended up there, and whether or not that is permissible. Additionally, we’ll discuss how different media (text, image, video, music, etc.) might require different treatment.

 Instead, dataset curators typically mean that they want a dataset that creates a “good model.”
Ultimately, datasets exist to serve the tasks we want models to do. "General purpose" is not a task that it is easy to develop a dataset for.
Fro example, OpenAI's models are trained for the goal of being general-purpose, except if the purpose is generating hate speech.

## Dedication

This piece is dedicated to the late, [Chris Cieri](https://www.ldc.upenn.edu/christopher-cieri-1963-2023), director of LDC, with whom we had discussed the early versions of this paper in 2021. 

## Acknowledgements

This discussion is fueled by years of discussions with wonderful people, including, but not limited to: [James Grimmelman](https://james.grimmelmann.net/), [David Mimno](https://mimno.infosci.cornell.edu/), [A. Feder Cooper](https://afedercooper.info/), [Daphne Ippolito](https://daphnei.com/), [Nicholas Carlini](https://nicholas.carlini.com/), [Florian Tramèr](https://floriantramer.com/), [James Bradbury](https://twitter.com/jekbradbury), [Shayne Longpre](https://www.shaynelongpre.com/), [Chris Cieri](https://twitter.com/chris_cieri?lang=en), and [Lillian Lee](https://www.cs.cornell.edu/home/llee/)
