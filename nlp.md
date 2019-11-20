> Node2Vec

https://towardsdatascience.com/node2vec-embeddings-for-graph-data-32a866340fef

> NLP

http://www.wildml.com/deep-learning-glossary/

> Applying Deep Learning To Airbnb Search

https://arxiv.org/abs/1810.09591

https://www.shangyexinzhi.com/article/details/id-146242/

> How to Explain the Prediction of a Machine Learning Model?

https://lilianweng.github.io/lil-log/2017/08/01/how-to-explain-the-prediction-of-a-machine-learning-model.html

> Generalized Language Models

https://lilianweng.github.io/lil-log/2019/01/31/generalized-language-models.html

> An Overview of Deep Learning for Curious People

https://lilianweng.github.io/lil-log/2017/06/21/an-overview-of-deep-learning.html

> Learning Word Embedding

https://lilianweng.github.io/lil-log/2017/10/15/learning-word-embedding.html

> BERT

https://www.jiqizhixin.com/articles/2019-11-05-2

https://lilianweng.github.io/lil-log/2019/01/31/generalized-language-models.html

https://github.com/hanxiao/bert-as-service

https://www.tensorflow.org/hub

https://towardsdatascience.com/how-bert-leverage-attention-mechanism-and-transformer-to-learn-word-contextual-relations-5bbee1b6dbdb

https://medium.com/swlh/a-simple-guide-on-using-bert-for-text-classification-bbf041ac8d04

https://appliedmachinelearning.blog/2019/03/04/state-of-the-art-text-classification-using-bert-model-predict-the-happiness-hackerearth-challenge/

https://github.com/google-research/bert

https://blog.insightdatascience.com/using-bert-for-state-of-the-art-pre-training-for-natural-language-processing-1d87142c29e7

https://pypi.org/project/keras-bert/

https://towardsdatascience.com/how-to-do-text-binary-classification-with-bert-f1348a25d905

https://colab.research.google.com/github/google-research/bert/blob/master/predicting_movie_reviews_with_bert_on_tf_hub.ipynb



> GPT2

https://github.com/Morizeyao/GPT2-Chinese

https://github.com/rish-16/gpt2client

Language Models are Unsupervised Multitask Learners

https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

https://terrifyzhao.github.io/2019/02/18/GPT2.0%E8%AE%BA%E6%96%87%E8%A7%A3%E8%AF%BB.html


目前效果较好的大部分的nlp任务都会应用预训练语言模型的迁移知识，主要是采用两阶段的模型。第一阶段进行预训练，一般是训练一个语言模型。最出名的是BERT,BERT的预训练阶段包括两个任务，一个是Masked Language Model，还有一个是Next Sentence Prediction。通过预训练能够利用海量的无标注的语料，以从中抽取出语言学特征，并在第二阶段结合具体任务，把这些从海量无标注语料中抽取出的语言学特征作为特征补充，迁移到下游任务中进行应用。第一阶段预训练出的模型具有很强的泛化能力，一方面是因为语料非常丰富能够得到很好的表征，另一方面是因为使用多层的Transformer作为特征提取器能够抽取出泛化能够更强的特征。从GPT2.0可以看出加大用于进行预训练模型的语料，同时提高这些语料的质量能够使训练出的模型更具泛化性能。从微软提出的多任务深度神经网络以及清华和华为ERNIE: Enhanced Language Representation with Informative Entities以及百度的ERNIE: Enhanced Representation through Knowledge Integration来看补充更多的先验知识供预训练语言模型学习能够使模型泛化能力更高。ERNIE相当于融入了知识图谱，清华的ERNIE在BERT的MLM以及Next Sentence Prediction任务的基础上增加了denoising entity auto-encoder (dEA)任务，这是自然而然应该想到了，MLM相当于在字上的降噪，增加了实体信息，自然应该在实体层次进行降噪。

在具体的第二阶段的任务中我们只需结合第一阶段的预训练（pre-train）模型简单的修改一些输出层，再用我们自己的数据进行一个增量训练，对权重进行一个轻微的调整（fine-tune）。例如BERT训练好的模型会保存在checkpoint中，在我们进行具体的第二阶段的任务时，例如分类任务，只需传入当前的训练语料会加载预训练模型的图以及训练好的具备丰富特征的参数，因为预训练好的模型泛化能力很强，所以具体任务中只需要对可训练的这些参数进行fine-tuning（微调）便能满足当前任务，因为可用的标注语料很少，只用这些语料通过特征抽取器可能并无法抽取出泛化能力强的表征，通过预训练的模型能够进行很好的特征补充，使得抽取出的特征更加适用于我们具体的任务。结合具体任务的训练语料对可训练的参数进行微调，然后把这些微调后的参数以及图保存起来，以便于我们进一步进行预测时使用。

> Ref

https://www.cnblogs.com/dyl222/p/10960842.html

https://www.cnblogs.com/dyl222/p/10779742.html

