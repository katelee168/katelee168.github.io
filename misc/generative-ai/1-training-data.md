---
title: "Training data"
---
<!--
Audience
Broadly general audience w/ some interest in tech/law. Needs to have a broad grasp of the full range of stuff out there
Some historical context (that the tech folks are also missing)
What should people know for later entries to make sense?
-->

## Section 1

<!--All generative models are trained on data, in particular, they are trained to reproduce the data in their training set. 
Data can come in all sorts of forms. Today, we have generative models trained on text, images, music, speech, and code. You could imagine getting more specific: training models just on fan-fiction, court filings, or XX. 
People create datasets
Through different types of curation-->

If you’ve seen the recent TikTok trend transforming people into historical versions of themselves^[[Lensa AI climbs the App Store charts as its ‘magic avatars’ go viral](https://techcrunch.com/2022/12/01/lensa-ai-climbs-the-app-store-charts-as-its-magic-avatars-go-viral/), or had a conversation with the chatbot, ChatGPT, you’ve interacted with generative AI. 
<!--In the last year, use of generative AI has exploded. People now use it to generate songs, to pose as customer service representatives, and to XX. -->
All those models have seen lots of images and/or text–some of which looks like the generation and some of which doesn’t. All the data that the model has seen is called training data. 
That’s because generative AI models are statistical models of large swaths of data. 
The current generation of models are all trained to reproduce data in a training set. 
Current generative models are trained to reproduce their training data. That means that if the sentence “Mary had a lamb” were in the training data, then the model would get a higher reward for choosing “lamb” after it sees “Mary had a” than any other word (even though Mary probably also had other farm animals!). 
Generative models today are often general purpose–but you could imagine training a model specifically on code data (such as CoPilot), legal data, news, Tweets, speech, old-school films, and so much more. For the incredibly broad definition of data, there is an equally broad set of possible generative models that could be trained. 

![This picture will do a better job of explaining how incredible some of these image generations are than I could do with words.](./images/todo.png)


But who puts these datasets together? And what’s in them? We’ll unpack those questions in this article. 


The goal of an AI system is to act intelligently. A system that processes language should be able to parse an input sentence into an abstract form, combine that sentence with contextual world knowledge, and produce a grammatical output sentence that is relevant and informative. For example, given the sentence "a dog bit my leg", we know from the rules of English grammar that "the dog" is a noun phrase that serves as the subject of the sentence, but also from contextual knowledge that dog is the sort of thing that is more likely to bite than leg, and that a leg is the sort of thing that a dog might bite. 

The early work in AI assumed that building a language system would simply involve encoding this type of grammatical and contextual knowledge and mechanically applying it. Thus, programming languages for logical and symbolic manipulation such as LISP and Prolog were developed as alternatives to numerical processing languages like fortran. Resources such as cyc and wordnet were developed as large-scale databases of real-world knowledge.

The use of data sets as they are understood in modern AI began with the statistical revolution of the late 90s and early 2000s. Researchers began to recognize that language is full of complexity and ambiguity, and we could not simply encode our way to working systems, at least not without prohibitively expensive annotation processes. It would be much easier and more reliable to simply collect examples of language and observe the properties we wanted to encode in the way that they are most useful to the system that we have, rather than what we want the system to achieve. This was the era of Jelinek's famous quote about linguists and statisticians.

The revolution in data was driven by a number of factors beyond the availability of new statistical tools such as text classifiers and HMMs. First, text data in digital form became much more available due to the rise of the internet. Data sets such as Sam Roweis' 20 Newsgroups took advantage of pre-web text forums. Second, shared evaluations allowed expensive annotated datasets to be created and distributed. This trend was led particularly by NIST in Information Retrieval through TREC and related conferences and by LDC collections such as the Penn Treebank. These collections emphasized annotations such as parse trees or relevance judgments rather than the documents themselves as the primary benefit. Third, the growth of online activity provided compelling operational use cases for data-driven statistical models. Internet search supercharged information retrieval research, and spam classification proved a watershed in the impact of ML-based classifiers.

Still, collections remained small and special-purpose. Collection sizes tended to be in the thousands and tens of thousands of documents. Collections were built to support specific applications, and the focus remained on annotations as the key value. While "unlabeled" text began to be more readily available, it was difficult to show that it had any real value beyond smaller, supervised datasets. As a result, data work tended to focus on layering annotations on existing documents, most notably the Penn WSJ articles.

## Section 2: Early-modern Datasets (1990s-2000s)

<!--
All datasets are curated: they are all collected and organized. However, earlier datasets in computational linguistics received more careful attention paid to each individual datapoint. 
Paragraph of pre-history to the 70s. Very early datasets for computational linguistics were hand assembled. 
Everything is hand labeled
Linguistic Data Consortium
MNIST
Multimodal
Modern era (2000s)
Wordnet
WMT
Technical features of canonical ones. Pick 2-4 from that era
-->

We’ll start our story with one of the first dataset machine learning students learn about: MNIST^[[About MNIST](https://www.lri.fr/~marc/Master2/MNIST_doc.pdf). The original website seems to be password-protected: https://yann.lecun.com/exdb/mnist/.]. First released in 1999, the dataset was built by Mixing NIST’s datasets of handwritten numbers and contained only 60,000 examples in the training set. As a point of reference, LAION-5B, an image dataset made in 2022, has 5.85 billion text-image pairs. 
When we say this dataset was highly curated, we mean that we know its provenance, it has high coherence, and it is easily inspectable. 
All the digits in MNIST were written by either high school students or employees at the US Census Bureau and compiled by NIST, aka, the provenance of the data is the high school students and Census employees via NIST.
The data in MNIST is rather uniform: all data are 32x32 pixels large, presented in black-and-white, and the digits are roughly centered in the image.
This dataset has the added feature of being incredibly well studied. A quick Google Scholar search of MNIST returned 76,900 results^[To be fair, it isn’t 76,900 articles on MNIST because the name is also synonymous with “small dataset” so other datasets like Fashion-MNIST that has photos of clothing, also appear in the search results.]. MNIST is so well studied, that we know exactly which examples are labeled incorrectly [**Todo, find the citation**].



> Aspects of datasets
>
> * **Provenance**: understanding of where the data comes from
> * **Coherence**: all the data is of a particular, easy do describe form
> * **Inspectability**: the data is easy to inspect and it’s possible to [**TODO. this isn’t quite right. Looking for a different word here.**]

In some ways, MNIST is closer to modern-day datasets in that it is lightly annotated (each image is annotated only with the label of number in the image) compared with language datasets from the same time. For example, WordNet, an early linguistic dataset that studied relationships between words was carefully, manually curated and annotated. The project started in 1985 and was first released in 1995–that’s 10 years to create the dataset^[[Princeton University "About WordNet." WordNet. Princeton University. 2010.](https://wordnet.princeton.edu/)].
The current version of WordNet (v3.0, released in 2006) contains 147,278 unique noun, verb, adjective, and adverb strings and is (compressed) 10.5MB. 
That’s a far, far cry from the 800GB dataset, the Pile, released in 2020^[[The Pile: An 800GB Dataset of Diverse Text for Language Modeling](https://arxiv.org/abs/2101.00027)]. 
As far as provenance, coherence, and inspectability go, WordNet was entirely put together by hand: the provenance is the authors of the dataset who did their best to format the data in a coherent manner. 
**TODO: Also write about PennTreebank**

LDC

## Section 3: Explosion of datasets size (2010-today)

**TODO: Say that this is focused on language datasets**
<!--
Exponential growth of datasets (and the scale today)
General description of what these datasets have in common
Data is gathered from somewhere
Different approaches out there for how datasets are put together. 
Proprietary datasets
Existing datasets people have curated
Existing datasets (Enron)
Web-scraping (CC)
Stock photography sites
-->

Language datasets of that time were reflective of both the technical limitations of the computers and systems that researchers ran, and model design. At the time, natural language models were similarly hand-designed, and relied on features like XX that XX. For instance, IBM’s Watson (developed in 2011) explicitly parsed sentences into linguistic components then used hand-designed features to win at Jeopardy **TODO VERIFY**. 
Up until 2016, Google Translate similarly used phrase-based translation which broke sentences into linguistic parts to translate separately^[[A Neural Network for Machine Translation, at Production Scale](https://ai.googleblog.com/2016/09/a-neural-network-for-machine.html)].

Today’s language datasets are diverse and vary in size, type or presence of annotations, and level of curation. 
There still exist small, curated datasets (that are often used to evaluate trained models), such as each individual task in Big-Bench^[The distinction between evaluation and training is not super clear. Evaluation datasets are often benchmarks that come with a training and test set. It’s common practice to train on the data from the training set of the evaluation benchmark then test on the evaluation benchmark’s test set. https://github.com/google/BIG-bench].
But the major change is on the other end of the spectrum where datasets have gotten a lot larger, have minimal to no annotations, and have a different style of curation (more on this in section **TODO**)

Many open-source, large datasets predominantly contain data scraped from the web. 
Datasets like The Pile and C4 are both 800GB or roughly **TODO**; the dataset for BLOOM was 1.6TB of pre-processed text^[[BLOOM Training data](https://huggingface.co/bigscience/bloom#training-data)], and unreleased datasets used for training Chinchilla is 1.4T tokens^[[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)]. 
All of these datasets have minimal annotations, mostly meta-data saved when the data is collected as opposed to annotations added by a person. 
These datasets are often filtered with automatic metrics removing things that are “poor quality,” “duplicates,” “toxic,” or “unnecessary.” All of these terms are necessarily vague which limits the effectiveness of the automatic metrics used to filter the datasets. 
For these large, web-scraped datasets, we no longer have meaningful provenance. We might know that a paragraph of text is from a particular website, but that won’t necessarily tell us who the author of the text is, or who the photographer or artist is and whether they have permission to post the content.
```This gets even more complicated with user-generated text. ← not sure where I was going w/ this ```
<!--Provenance:
The RealNews dataset is a filtered dataset of web-scraped data. 
contains text from web-domains that are →
TODO: Having loose coherence isn’t bad
Provenance means more than just where the data comes from. It can also 

The other type of large dataset contains proprietary data. To be frank, the only ways to collect massive amounts of data cheaply are to scrape it from the web, or use data generated by users of a product or through the course of creating a product. For example, the Amazon Reviews dataset (2018)^[[Amazon Review Data (2018)](https://nijianmo.github.io/amazon/index.html)] contains 233.1M examples with customer ratings. Other popular datasets in this vein are the Netflix recommendations dataset^[[Kaggle: Netflix](https://www.kaggle.com/datasets/shivamb/netflix-shows)] and IMDB movie reviews^[[IMDB Datasets](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)], or the Google Books N-gram corpus (2.2 TB of text!)^[[Wikipedia: Google Books N-gram Viewer](https://en.wikipedia.org/wiki/Google_Ngram_Viewer)].

I lied slightly, there are sometimes structures in the world that dataset creators can take advantage of. For example, the annual Workshop on Machine Translation (WMT) challenge, first started in 2006, but still going as of 2023), releases a shared dataset to evaluate the ability of models to translate across multiple languages^[[WMT 2023](http://www2.statmt.org/wmt23/index.html), [WMT 2006](https://www.statmt.org/wmt06/)]. 
The shared task in 2016 included news articles in multiple different languages, and parallel training data (data that has a given sentence in the first language and that same sentence in a second language) for IT support and biomedical translation. [WMT 2016, News task description](https://www.statmt.org/wmt16/). 
Narrowing the scope of the data to news articles (or to IT support, or biomedical work) can make it easier to find parallel training data, and also explicitly makes a choice about what kind  and quality^[Quality in the sense of qualitative features.] of data is relevant. The explicit choice of scope gives the data a stronger coherence. 
In these settings, the provenance may be easy to write down, but depending on the domain at hand, it could still be challenging to understand what exactly it means. 
It’s harder to talk about provenance, coherence, and inspectability

Datasets were hand curated because
Technology (computers) were a lot more limited in memory and compute and could not process
Models had a lot less capacity to find patterns in unstructured data
There are so many different datasets. You can explore over 23,000 datasets on HuggingFace that are language, vision, and multi-modal^[[HuggingFace Datasets](https://huggingface.co/datasets)]. Kaggle, another popular dataset host, boasts 50,000 public datasets^[[Kaggle](https://www.kaggle.com/)]

## Data collection

In a sense, the training data you use is the most important choice you could make in determining copyright and privacy violations of your generative model. It’s just really hard to generate infringing content if none of your training data is infringing. Of course, it’s not that simplistic, because there are many different types of data that get integrated together into a model. 
For example, most generative AI models currently released are interactive–they take in some information from the users and then generate content. That’s called prompt data. 
There’s also at least two types of training data: training data and human-feedback data^[Which is, yes, an absurd name for the data. It’s always weird to talk about us as a species: “the humans.”]. 
We’re going to first discuss training data collection, then data curation and data processing. Finally, we’ll discuss collecting human-feedback data, and how prompt data integrates into the model system..

There’s a bit of a pendulum swing here. In the past (like, 2017), NLP systems were developed from scratch for specific tasks, so they used task-specific data. These curated datasets were important to comply with regulations [todo] and also because models didn’t have the capacity to deal with shitty data, and there was no reason to collect it. As models got larger and larger they were able to pick out patterns we cared about in the data^[Models also pick out patterns that we don’t care for in the data–which is the motivation behind model alignment–to keep only the patterns we want.] without us manually curating the data and also became more general purpose.
Whether or not this is a “true statement” is hotly debated amongst researchers. 
However, the fact remains that the largest language models use training data that is minimally curated compared with standard dataset collection practices from pre-2017
^[It’s not a secret that most datasets are crap. And by crap, we mean that they’re incredibly messy. In all data science, the first step is to “clean” and explore the data. Of course, “crap” is a catch-all term, and the ways in which data can be messy vary widely. However, whenever you’re dealing with large collections of data that are not cost-effective to manually curate and inspect, the dataset will necessarily contain anomalies and errors. Even if it were possible to manually curate and inspect the entire dataset, it would be impossible to find all possible patterns across the data because we are 1. All humans who have limited brain capacity and whose background makes it easier to identify some patterns and not others, and 2. Some patterns are not semantically meaningful to humans.]
Data is primarily scraped from the web. Even so, it’s not enough to _just_ scrape whatever data you come across.

Dataset creators have a lot of choices to make. For example, should the dataset be primarily one language? Should it include an equal balance across as many languages as possible? What about an unequal balance across languages? That question actually hides even more choices. If an English sentence includes a single French word, is that sentence English or French? What about an entire French sentence embedded into an otherwise English paragraph? The answer to “Where do you draw the line” is often just a choice. As much as we would like to back each choice by science, it’s cost, and compute, prohibitive to run a different experiment for each one of these choices. 
For some choices, there’s no experiment that would yield a reliable answer for each question we pose. That’s because the answer is contextual and cultural. 
If the French sentence in the English paragraph is “Bon appetit!” then we would consider the paragraph to still primarily be English because that’s a sentence that’s often crossed-over to English. However, that wouldn’t be the case if the sentence was “Mon chat noir continue de s'enfuir” ^[In English: “My black cat keeps running away.”].
However, let’s say that black cats running away became a trend on TikTok, then perhaps “Mon chat noir continue de s’enfuir” would cross-over into English.

The list of data choices is extremely long. Let’s discuss some types of English text on the web. If I were to show you just the text from a Wikipedia article, a news article, a wiki-how article, and some Tweets, I bet you could guess which website they were from. Each website has a style and set of constraints based on the implicit and explicit expectations of the authors and audience. Now which ones of those websites should go into a dataset? 
Well it depends on what you want to use that dataset for.
In one popular language dataset, the Pile, the dataset creators chose to include multiple “academic” datasets, like PubMed, ArXiv, and FreeLaw, and code from Github. This means that models trained on the Pile will have seen medical literature, legal literature, and code. A model not trained on code would have a much harder time generating code^[This doesn't mean that models not explicitly trained on code can’t generate code. Webscraped data is not clean, and there will inevitably be some code mixed in.].


![Example of dataset composition. These are all the datasets that make up [the Pile](http://arxiv.org/abs/2101.00027).](./images/pile-composition.png)

There’s been some efforts within the community to encourage dataset creators to document what data goes into it. For example, many datasets within HuggingFace (a popular open-source model and dataset repository) now have [datasheets](https://arxiv.org/abs/1803.09010) attached to them. As an example, this is the Pile’s [datasheet](https://arxiv.org/pdf/2201.07311.pdf). Datasheets collect information about how the data was collected, the motivation behind it, any preprocessing that was done, and future maintenance plans. 
Unfortunately, many companies don’t release many details about their proprietary datasets.
If understanding nuances of training data is important for choosing amongst APIs, then the lack of open-documentation obfuscates which API would be best for an application. 
<!--To the extent that training data impacts the applications a model can be used for later, it will be challenging for users shopping for APIs to determine which API will be best for their use case. -->
<--!To the extent that understanding nuances of training data enables individuals who are choosing amongst APIs to determine which API will be best for their use case, the lack of open documentation will make that challenging. -->\

Unfortunately, as we see, just writing down where data comes from is insufficient to understand what the datasets actually contain. 
As unfortunate as that is, other models have been trained on data that is not documented, nor public.


For example, here is a data

## Section 4: Data curation
Datasets are big
Datasets are messy 
Datasets are choiceful 
People never see all data points.


Measures of quality
Bad words filters
Curation to match the downstream task (is less of a thing now)

Datasets in the Pile are named for where the data was collected from. 
As we discussed, that doesn’t always describe what constitutes the component datasets: Github contains a lot more than just code. Wikipedia can contain multiple languages. 
Ideally, we would use finer-grained filters to understand and curate data. 

Or rather, it _ought_ to depend on what you want to use that dataset for. The crazy thing about modern language models is that we can be more hands off in data curation than we expected. 
But, as we become more familiar with these models, we learn that we can’t be as hands-off as we have been. It turns out that including data in the training set that looks similar to the downstream applications means that the model performs better on those applications! **TODO: Insert stuff about few-shot eval here**. Hence, we see the pendulum swing back towards more hands-on curation of datasets. 



The standard is for dataset creators to set some notion of quality (that is often not easy to explain or document because quality is not easy to explain or document)^[Some of us want rigor in this process, but we’re not going to get it because we’re dealing with cultural constructs that don’t lend themselves easily to quantification.], then choose websites, other datasets that meet that standard and add those together to form the full dataset. 
I’ve arbitrarily defined the distinction between data collection and data curation to be adding vs. removing data from the dataset. Ultimately, these are all choices dataset creators make about what can be included. 

## Section 5
Gathered with differing intentions over rights over the data
Problematic consent over use of the data.
People use whatever is available to them
Any books that are online will definitely be used. 

## Graveyard

What we accept vs. what is acceptable. 
“We don’t have to care about training data.” You have to unpack every single word in that sentence. Who is “we?” Who gets to not care about training data? Who doesn’t have the luxury of not caring about training data?
There’s a bit of a divergence between open-source datasets and proprietary datasets, like the ones that OpenAI and Google can train on. 
Today’s language datasets fall into two categories: large datasets used for training models, and smaller, more curated datasets used for evaluation. The smaller, more curated datasets still sometimes 
Most large datasets with annotations are collections of data generated by users in the course of a product’s life-time; for example, 
Fun image
