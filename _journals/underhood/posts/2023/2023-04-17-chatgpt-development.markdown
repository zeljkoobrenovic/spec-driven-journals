---
layout: post
title: "LLMs, ChatGPT and Evolution of Software Engineering: Patterns, Anti-Patterns, and Quality Imperative"
date:   2023-04-16 21:12:01 +0100
categories: architecture
author: by Željko Obrenović (obren.io)
permalink: chatgpt-se-evolution
icon: assets/icons/chatgpt.png
timetoread: 15 min
excerpt: "LLMs like ChatGPT can significantly impact software engineering by synergically combining Natural Language Processing (NLP), LLM-driven Soft Programming, and Traditional Hard Programming. Three synergy patterns: Generative Pattern, Learning and Explanation Pattern, and Hardening Pattern, can help developers harness the potential of these technologies."

---
<style>
    h2 {
        margin-top: 42px;
        font-size: 50px;
    }
    h3 {
        margin-top: 42px;
        font-size: 40px;
    }
</style>

![](assets/images/chatgpt/grandmother-gd1611d538_1920.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/sasint-3639875/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1822560">Sasin Tipchai</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1822560">Pixabay</a>
</div>

> **KEY POINTS:**
> * The primary objective of this article is to present a framework that can better structure discussions about ChatGPT and software engineering.
> * Using this framework, I discuss that LLMs like ChatGPT can positively impact software engineering by synergically combining Natural Language Processing (NLP), LLM-driven Soft Programming, and Traditional Hard Programming.
> * Three synergy patterns, Generative Pattern, Learning & Explanation Pattern, and Hardening Pattern, can help developers harness the potential of these technologies.
> * Developers must be cautious of anti-patterns such as Over-generation and Knowledge Pollution (Bullshit Asymmetry Principle), Softening Hard Knowledge, and Unnatural Verbalizations.
> * Ideally, we should be able to produce better software faster, not by AI replacing developers but by having developers employ productivity gains from AI to spend more time improving products’ quality.



&nbsp;

* TOC
{:toc}

&nbsp;

## Intro

[ChatGPT](https://chat.openai.com/), an advanced AI language model using [GPT-3](https://openai.com/blog/gpt-3-apps) and [GPT-4](https://openai.com/research/gpt-4), has gained attention in various fields, including software engineering. This AI model demonstrates exceptional language understanding, allowing complex problem-solving, code generation, and software documentation. Consequently, developers are integrating ChatGPT into their processes to reduce development time and improve software quality. While there is a lot of hype, the growing reliance on ChatGPT in software engineering is here to stay.

With this article, I want to help software developers to understand the underlying structure and developments behind recent ChatGPT hype. By assessing the technology’s foundation, developers can make informed decisions about incorporating ChatGPT, ensuring its effective use while avoiding over-dependence or misaligned expectations. This balanced approach allows them to maximize ChatGPT’s benefits and combine them with traditional software engineering practices.

The primary objective of this article is to present a framework that can better structure discussions about ChatGPT and software engineering. Using this framework, I discuss that:
* LLMs like ChatGPT can positively impact software engineering by synergically combining Natural Language Processing (NLP), Soft Programming, and Traditional Hard Programming.
* Three synergy patterns, Generative Pattern, Learning & Explanation Pattern, and Hardening Pattern, can help developers harness the potential of these technologies.
* Developers must be cautious of anti-patterns such as Over-Generation and Knowledge Pollution (Bullshit Asymmetry Principle), Softening Hard Knowledge, and Unnatural Verbalizations.
* Ideally, we should be able to produce better software faster, not by AI replacing developers but by having developers employ productivity gains from AI to spend more time improving products’ quality.


## The Framework: Soft and Hard Programming + NLP

Many discussions about ChatGPT tend to focus on low-level machine learning topics, such as deep learning, or on the high-level impact of the AI "revolution" on business and humanity. These conversations are not suited to understanding the practical implications of recent advancements in specific disciplines, like software engineering. To address this, I will use a model that outlines three high-level developments that, when used synergically, will further evolve the software engineering field. This model represents the styles and skillsets developers will need to master to benefit from the full power of AI-assisted software development.

From a software engineering point of view, I see three key developments that current advances in AI leverage (Figure 1):

* **Natural Language Processing (NLP)**: [NLP](https://en.wikipedia.org/wiki/Natural_language_processing) has improved significantly, allowing AI models like ChatGPT to engage in human-like conversations. These advances enable developers to interact with tools in everyday language, simplifying tasks and enabling better human-machine collaboration. It can automate documentation, enhance code readability, and improve team communication. This new possibility will require developers to rethink new modes of interactions, both when building solutions for users and for internal tooling.

* **Soft Programming**: By soft programming, I mean a general set of methods for [training machines through examples](https://kozyrkov.medium.com/the-simplest-explanation-of-machine-learning-youll-ever-read-bebc0700047c) to, for instance, learning from existing code to generate new solutions. Knowing how to train programs with examples rather than instructions and how to test, monitor and deploy such soft/probabilistic solutions is an important skill to master.

* **Hard Programming**: Despite AI and NLP advancements, ["traditional" programming languages](https://obren.io/tools/tech/index.html?catalog=programming_languages) are still crucial, and will keep developing. We should expect continued progress in programming languages, their syntax, libraries, and compilers supporting developers in controlling their code, optimizing performance, and addressing security concerns.

The [Appendix](#appendix-evolution-of-programming-and-ai) provides an overview of the evolution of these three key developments. The seemingly "overnight" success of [Large Language Models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model) and ChatGPT is not due to an abrupt breakthrough but a series of progressive advancements that have evolved. The convergence of developments in traditional programming, NLP, and soft programming now allows individuals to synergistically combine these technologies synergistically, creating powerful new solutions.

![](assets/images/chatgpt/framework.png)
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px;">
<b>Figure 1:</b> Large Language Models (LLMs) like ChatGPT can have a significant impact on software engineering by synergistically combining Natural Language Processing (NLP), LLM-driven Soft Programming, and Traditional Hard Programming.
</div>


Each of described three developments sits at the shoulders of knowledge giants. They can provide us not only with particular techniques but a vast body of knowledge that you can leverage when you engage with them:
* **Soft/probabilistic knowledge**: soft programming is not possible without context knowledge. AI models, like LLMs, provide a rich context of world knowledge you can leverage or fine-tune with your data and examples.
* **Language knowledge**: NLP tools embed a significant amount of growing linguistic and other knowledge for hundreds of languages. 
* **Hard/explicit knowledge**: classical programming leverages billions of lines of code in libraries, frameworks, and services used when you develop your solutions.

One of the fascinating developments behind ChatGPT recently is that we can now synergically connect these three bodies of knowledge without significant investments.

Developers can use AI and NLP while leveraging traditional programming languages. This balanced approach can create a versatile software engineering process, leading to better products and satisfied users.

## Synergy Patterns 

While each of the three developments (Soft Programming, Hard Programming, NLP) is useful in itself, the true power of AI-assisted software development, in my view, will come by mastering their synergic usage. To fully exploit the possibilities offered by the combination of Soft Programming, NLP, and Hard Programming, I identify three new synergy patterns that software developers can now leverage:

* **Generative Pattern**: This pattern refers to the ability to utilize large language models (LLMs) like ChatGPT to generate new text content and code. By understanding how to leverage these models effectively, developers can automate and streamline various aspects of the software engineering process, such as code generation and documentation.

* **Learning and Explanation Pattern**: This pattern focuses on the ability to communicate complex concepts and constructs in a clear, personalized manner using natural language. Mastering this skill enables developers to create more user-friendly interfaces, enhance collaboration among team members, and facilitate a better understanding of software systems for technical and non-technical stakeholders.

* **Hardening Pattern**: This pattern adds accuracy and reliability to the probabilistic, by-example nature of "soft" programming. By developing this skill, developers can ensure that the generated code meets the necessary performance, security, and maintainability standards while integrating seamlessly with the more deterministic aspects of traditional hard programming.

By mastering these three new synergy patterns, software developers can fully harness the combined potential of NLP, Soft Programming, and Hard Programming, leading to more efficient, innovative, and robust software development processes.


### Generative Pattern

Using Soft Programming techniques, developers can leverage ChatGPT and similar large language models (LLMs) to generate natural language text and code, making the software development process more efficient, intuitive, and accessible, transforming how software developers approach their tasks. Using LLMs to produce high-quality text and code may be essential in modern software development (Figure 2).


![](assets/images/chatgpt/generative.png)
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px;">
<b>Figure 2:</b> By using Soft Programming techniques, developers can leverage ChatGPT and similar large language models (LLMs) to generate both natural language text and code, making the software development process more efficient, intuitive, and accessible.
</div>

The current hype surrounding LLMs primarily revolves around discovering and sharing effective techniques for generating accurate and contextually appropriate text and code. These tips and tricks can range from understanding how to provide specific prompts to fine-tuning the models to produce more accurate outputs. Mastering these techniques is crucial for developers looking to harness the full potential of LLMs like ChatGPT.

By effectively leveraging LLMs, developers can streamline various aspects of their work, including code generation, debugging, and documentation. This approach can increase efficiency and innovation within the software development process. Furthermore, LLM-generated content can help bridge the gap between technical and non-technical stakeholders, fostering better communication and collaboration within teams and organizations.

However, developers must still exercise their skills in critical analysis and problem-solving to ensure the quality and reliability of the generated content. By striking a balance between utilizing LLMs and traditional software development techniques, developers can harness the power of these advanced AI models while maintaining the necessary control and precision in their work.


### Explanation and Learning Pattern

The combination of NLP and ChatGPT presents an opportunity to enhance understanding and education in various fields. By leveraging the advanced language capabilities of ChatGPT, individuals can learn faster and improve their teaching abilities. Acquiring this critical skill enables more effective knowledge transfer and fosters a better learning environment (Figure 3).


![](assets/images/chatgpt/nlp-patterns.png)
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px;">
<b>Figure 3:</b>  NLP and ChatGPT can help learners grasp complex concepts and code more efficiently.
</div>

NLP and ChatGPT can help learners grasp complex concepts more efficiently by providing concise, contextual explanations of code or complex concepts and data tailored to their needs. Its ability to generate relevant examples and analogies further enriches the learning experience, aiding the comprehension and retention of new information. Furthermore, ChatGPT can offer instant feedback and support, making it an invaluable resource for self-paced learning and skill development.

In addition to its learning capabilities, developers can utilize ChatGPT as a powerful teaching aid. Educators can harness the AI model to create personalized learning materials, such as adaptive quizzes, interactive exercises, or customized lesson plans, which cater to each student's unique needs and preferences. Incorporating ChatGPT into their teaching toolkit allows educators to save time on content creation while ensuring that their instructional methods remain engaging and effective.

Ultimately, learning faster with ChatGPT and using it to enhance teaching methods is a valuable skill in today's rapidly evolving world. By embracing this new educational paradigm, learners and educators can benefit from a more adaptable, efficient, and engaging learning experience.


### Hardening Pattern

One way to make LLMs more robust is by using conventional programming languages to create chatbot plugins that can help the LLMs handle specific tasks or scenarios. For example, design an LLM to assist with customer service. You can also create a plugin using a programming language like Python or Java to handle specific customer inquiries or complaints. This plugin could be integrated into the LLM's existing architecture, allowing it to take more complex scenarios and provide more accurate responses (Figure 4).

![](assets/images/chatgpt/hardening.png)
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px; font-style: italic">
<b>Figure 4:</b> Using conventional programming languages can make LLMs and similar AI techniques more robust and capable of handling a more comprehensive range of scenarios and tasks.
</div>

Another way to make LLMs more robust is by using programming languages to improve their natural language processing capabilities. For example, you could use machine learning algorithms to train the LLM to understand better and interpret natural language inputs. This process could involve using programming languages like Python or R to develop custom algorithms and models that can help the LLM better understand the nuances of human language.

Overall, using conventional programming languages can make LLMs and similar AI techniques more robust and capable of handling a more comprehensive range of scenarios and tasks. By leveraging the power of programming languages, developers can create custom plugins and algorithms to help LLMs better understand and respond to user inputs, ultimately improving their overall performance and effectiveness.

## Anti-Patterns

Despite the benefits, software developers must be cautious of anti-patterns such as:
* Over-Generation and Pollution, 
* Softening Hard Knowledge, and
* Unnatural Verbalizations.

### Over Generation and Pollution

The [Bullshit Asymmetry Principle](https://en.wikipedia.org/wiki/Brandolini's_law) is a concept coined by the Italian software developer and blogger Alberto Brandolini. It states that "*the amount of energy needed to refute bullshit is an order of magnitude bigger than to produce it.*" In other words, creating false or misleading information is much easier than fact-checking and correcting it. As an AI language model, ChatGPT can generate text on a wide range of topics at a breakneck pace. However, ChatGPT creates text based on the patterns it has learned from the data provided to it for training. If such training data are of low quality, the ChatGPT's answer will be similar (i.e., [garbage in, garbage out](https://en.wikipedia.org/wiki/Garbage_in,_garbage_out)). Of course, ChatGPT has the potential to help combat the spread of misinformation and "bullshit" by generating accurate and fact-checked information in response to queries. However, without awareness and appropriate measures, we may end up with an AI-driven technology that can create a massive amount of misleading information that will be practically impossible to refute.


The ease of using LLMs like ChatGPT has democratized AI-generated text and code, but having in mind Brandolini's observation,  it also brings potential risks, leading to several concerns:

* **Content oversaturation**: Widespread LLM use may lead to an excess of low-quality content, making finding valuable information difficult.
* **Inaccurate or misleading information**: Developers may generate content without deep subject knowledge, causing inaccuracies and misinformation.
* **Code quality and maintainability**: Generated code may not follow best practices, affecting maintainability and scalability.
* **Plagiarism and originality**: LLMs could encourage plagiarism or derivative work, harming intellectual property rights and creativity.
* **Ethical concerns**: Generating low-quality text and code can propagate biases and prejudices from LLMs' training data, raising ethical issues.

The ease of content creation can lead to a vicious circle of deteriorating knowledge quality (Figure 6).

<div style=" margin-bottom: 32px; text-align: center">
<img src="assets/images/chatgpt/low-quality-spiral.png" style="width: 600px"><br>
</div>
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px;">
<b>Figure 6:</b> The negative cycle of content over-generalization begins with difficulty finding knowledge, leading to using ChatGPT as a knowledge source. This usage creates overdependence on it. Overdependence, combined with easy knowledge generation, results in a large amount of low-quality content. The high volume and low quality make finding knowledge even harder, starting the cycle again.
</div>

If left unattended, this vicious circle can create a massive amount of low-quality knowledge across all areas (Figure 7).

![](assets/images/chatgpt/low-quality-network.png)
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px; font-style: italic">
<b>Figure 7:</b> The network of low-quality knowledge arises from the ease of generating text and code using Generative Pattern. This knowledge becomes part of the data and examples used by LLMs to generate new content, further deteriorating the quality of knowledge produced.
</div>

Promoting responsible LLM usage and emphasizing human oversight in generating text and code are essential. Encouraging developers to verify accuracy, adhere to software development best practices, and maintain ethical standards can help mitigate risks tied to LLMs like ChatGPT.



### Softening Hard Knowledge

Large language models (LLMs) like ChatGPT and their probabilistic approach can offer numerous benefits in generating text and code and providing explanations. However, using LLMs to replace hard knowledge and explicit facts may lead to several issues, including softening hard knowledge (Figure 5).
* **Blurring of hard knowledge**: The probabilistic approach of LLMs can result in the blurring or softening of hard knowledge, leading to ambiguity or uncertainty. This approach can be problematic when dealing with subjects that demand precise and unambiguous information, as it may dilute the clarity and objectivity associated with hard knowledge.

* **(Un)reliability**: LLMs generate content based on probabilities, which means they might not always provide correct or up-to-date information. Relying solely on LLMs for factual knowledge could lead to misinformation or misconceptions, particularly in areas where accuracy is crucial.

* **Lack of domain expertise**: Although LLMs have a broad understanding of various subjects, they may need more depth of knowledge and context that domain experts possess. This limitation could result in superficial or misleading answers, which can be detrimental in fields that require specialized knowledge.

* **Bias**: LLMs are trained on data from the internet, which can include biased or prejudiced information. As a result, LLM-generated content may inadvertently perpetuate harmful stereotypes or reflect discriminatory attitudes. Relying on LLMs for hard knowledge could exacerbate existing biases and undermine efforts to promote fairness and inclusivity.

* **(Lack of) critical thinking**: Overreliance on LLMs for knowledge acquisition might decrease critical thinking and problem-solving skills. These cognitive abilities are essential for evaluating the integrity and relevance of information and developing a deep understanding of complex topics.

![](assets/images/chatgpt/softening.png)
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px;">
<b>Figure 5:</b> Softening pattern occurs when hard knowledge sources are ignored, and soft knowledge sources are used to obtain information instead.
</div>


It is crucial to balance utilizing LLMs and relying on traditional sources of hard knowledge, such as textbooks, research papers, and domain experts, to mitigate these issues. By maintaining a healthy skepticism towards LLM-generated content and verifying its accuracy, users can make the most of these powerful tools while minimizing their potential drawbacks and preserving the integrity of hard knowledge.

<div style="font-size: 90%; color: #323232; margin-bottom: 32px; text-align: center">
<img src="assets/images/chatgpt/wife.jpeg" style="width: 400px"><br>
</div>
<div style="font-size: 90%; color: #323232; margin-bottom: 32px;">
Source: https://twitter.com/DrEliDavid/status/1617762423972429824
</div>



### Unnatural Verbalizations

LLMs like ChatGPT make generating natural language content easy, but this convenience can cause issues such as unnatural verbalizations, loss of nuance, inappropriate medium, and oversimplification.

* **Inappropriate medium**: Visual representations might be more suitable for certain types of information than natural language.
* **Unnatural verbalizations**: LLMs may create awkward phrasing, reducing communication effectiveness.
* **Loss of nuance and context**: Over-reliance on NLP-generated content can lead to misunderstandings, especially with complex topics.
* **Oversimplification**: LLM-generated content may oversimplify complex concepts, causing a loss of essential details.

To balance LLM use with other forms of representation, developers should consider the most effective medium for their message and apply human oversight and critical thinking to maintain content quality, nuance, and context.


## Conclusions: Focus on Quality

The integration of Hard Programming, Soft Programming, and NLP through LLMs like ChatGPT can further advance software engineering. This technology mix increases efficiency and innovation, helping professionals and businesses excel. However, there are risks and negatives to address.

> Ideally, we should be able to produce better software faster, not by AI replacing developers but by having developers employ productivity gains from AI to spend more time improving products' quality. 

In my view, the key to maximizing the positive impact involves using productivity gains from usage of LLMs for quality assurance. This ensures AI-generated output is accurate, unbiased, and safe. The NN/g Nielsen Norman Group's article, "[ChatGPT Lifts Business Professionals’ Productivity and Improves Work Quality](https://www.nngroup.com/articles/chatgpt-productivity/)," supports this idea (Figure 8). It found that using ChatGPT for business documents saved time and significantly improved work quality. This is because people spent more time on editing (quality improvement) and less time on drafting the document. I also similarly developed this document, brainstorming and drafting the paper with the help of ChatGPT and spending a significant amount of time on multiple rounds of editing.

<br>
<div style="font-size: 90%; margin-bottom: 32px; text-align: center">
<img src="assets/images/chatgpt/chatgpt-authoring-productivity.jpg" style="width: 600px"><br>
</div>
<div style="font-size: 90%; color: #323232; font-style: italic; margin-bottom: 32px">
<b>Figure 8:</b> Credit: <a href="https://www.nngroup.com/articles/chatgpt-productivity/">NN/g Nielson Norman Group</a>. The bar chart compares the average time in minutes spent on three stages of writing a document: 1) brainstorming, 2) creating the first draft, and 3) editing the draft. It shows the time taken by users who used ChatGPT (top bar) and those who didn't (bottom bar). The data is from a study by Noy and Zhang (2023).
</div>

The previous diagram also illustrates my dream of AI-assisted software engineering: to give us more time to think through our decisions, validate, test, and improve their quality while simultaneously reducing the time-to-market. Ideally, we should be able to produce better software faster, not by AI replacing developers but by having developers employ productivity gains from AI to spend more time improving products' quality. And [improving quality is a sustainable way to reduce costs and speed up software development](https://martinfowler.com/articles/is-quality-worth-cost.html). By leveraging AI and other productivity tools, developers can reduce the time spent on repetitive or tedious tasks, such as code reviews and testing, and instead focus on improving the overall quality of the software. By enhancing the quality, developers can also reduce the overall software development costs by catching and fixing issues earlier in the development cycle before they become more expensive. Additionally, higher-quality software is typically more reliable and requires fewer updates and patches, which can further reduce costs over time.


But I am cautious about this dream as our ambitions will also grow. Software engineering history can teach us one thing (see the quote from Bruce Shiver from almost 40 years ago): every time we increase our development productivity, such an increase is followed by an even more considerable rise in our ambitions to build more applications and bigger systems.

> “Many of the challenges facing the software industry today are a direct result of **our insatiable appetite for new
> computer-based systems applications**. Others confront us simply because we have not managed to successfully solve a
> large number of problems that we ourselves created many years ago.”
> <br><br>--Bruce D. Shriver, From the Editor-in-Chief, IEEE Software, **January 1984**.

In conclusion, to harness the power of Hard Programming, Soft Programming, and NLP, the right balance between AI and human expertise is crucial. By emphasizing quality assurance and fostering a cooperative relationship between AI and humans, developers can unlock the full potential of this technology and minimize associated risks. As nicely described by the NN/s's article, AI and skilled human professionals collaborating is essential. By working together, they form a symbiotic relationship that surpasses individual capabilities. As AI develops and integrates more into the business world, our focus should shift to fostering collaboration between AI and humans. This aligns with Doug Engelbart's vision of advanced user interfaces augmenting human intellect, not replacing it.



<br>
## APPENDIX: Evolution of Programming and AI

> "The entire history of software engineering can be seen as one of raising levels of abstraction." 
> <br>--Grady Booch

<br>

The seemingly "overnight" success of LLMs and ChatGPT is not due to an abrupt breakthrough but a series of progressive advancements that have evolved. The convergence of developments in traditional programming, NLP, and soft programming allows individuals to synergistically combine these technologies synergistically, creating a powerful and efficient solution.

### Hard Programming Evolution

The [evolution of programming languages](https://en.wikipedia.org/wiki/History_of_programming_languages) has consistently trended towards higher levels of abstraction, enabling developers to concentrate more on the problem at hand and less on underlying implementation details. This article delves into the growing abstraction in programming languages, demonstrating how each stage has empowered developers and facilitated the creation of increasingly complex and sophisticated software systems.

**From Machine Code to Assembly Languages**: 
In programming's early days, developers worked with [machine code](https://en.wikipedia.org/wiki/Machine_code), manually inputting binary instruction sequences executed by computer hardware. [Assembly languages](https://en.wikipedia.org/wiki/Assembly_language) offered a significant abstraction leap, utilizing mnemonic codes that were more human-readable and simpler to write. An assembler translated these mnemonics into machine code, freeing developers from directly manipulating binary instructions.

**High-Level Programming Languages: FORTRAN and COBOL**: 
The emergence of high-level programming languages like [Fortran](https://en.wikipedia.org/wiki/Fortran) and [COBOL](https://en.wikipedia.org/wiki/Fortran) in the late 1950s represented another major abstraction milestone. These languages employed more natural syntax and constructs, allowing developers to express complex algorithms and data manipulation tasks more intuitively. High-level languages enabled portability across different machines, making code reuse more practical.

**Structured Programming: ALGOL, Pascal, and C**: 
[Structured programming languages](https://en.wikipedia.org/wiki/Structured_programming), such as [ALGOL](https://en.wikipedia.org/wiki/ALGOL), [Pascal](https://en.wikipedia.org/wiki/Pascal_(programming_language)), and [C](https://en.wikipedia.org/wiki/C_(programming_language)), introduced control structures (e.g., loops and conditionals) and modularization, enabling developers to organize better and manage code. This abstraction level made reasoning about program flow easier, reducing cognitive load on developers while further enhancing code reusability and maintainability.

**Object-Oriented Programming: Smalltalk, C++, and Java**: 
[Object-oriented programming (OOP) languages](https://en.wikipedia.org/wiki/Object-oriented_programming) abstract real-world entities or abstract concepts through classes and objects. OOP languages like [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk), [C++](https://en.wikipedia.org/wiki/C++), and [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) promoted encapsulation, inheritance, and polymorphism, fostering modularity and code reuse. OOP languages significantly streamlined large-scale software creation and maintenance by allowing developers to model complex systems using objects.

**Scripting and Domain-Specific Languages: Perl, Python, and Ruby**: 
Scripting languages like [Perl](https://en.wikipedia.org/wiki/Perl), [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), and [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)) increased abstraction by offering higher-level constructs for everyday tasks and specialized domains. These languages often featured powerful libraries, expressive syntax, and dynamic typing, allowing developers to write less code and accomplish more. Domain-specific languages, conversely, provided tailored abstractions and constructs for specific problem domains, further simplifying the development process.

**Declarative Programming: SQL, Prolog, and HTML**: 
[Declarative programming languages](https://en.wikipedia.org/wiki/Declarative_programming), including [SQL](https://en.wikipedia.org/wiki/SQL), [Prolog](https://en.wikipedia.org/wiki/Prolog), and [HTML](https://en.wikipedia.org/wiki/Prolog), signified another substantial abstraction step. Unlike imperative languages, which focus on a task's performance, declarative languages emphasize the desired outcome, allowing developers to express their intent without detailing the exact steps to achieve it. This abstraction enables developers to reason at a higher level, often leading to more concise and maintainable code.

**Functional and Reactive Paradigms**: 
[Functional programming languages](https://en.wikipedia.org/wiki/Functional_programming) like [Haskell](https://en.wikipedia.org/wiki/Haskell) and [Scala](https://en.wikipedia.org/wiki/Scala_(programming_language)) and [reactive paradigms](https://en.wikipedia.org/wiki/Reactive_programming) such as the [Reactive Extensions (Rx) library](https://en.wikipedia.org/wiki/ReactiveX) offer new abstraction levels by prioritizing immutability, pure functions, and reactive programming constructs. These paradigms allow developers to manage states better, handle concurrency, and create more robust and scalable software systems.

### Natural Language Processing Evolution

Over the years, [natural language processing (NLP)](https://en.wikipedia.org/wiki/Natural_language_processing) has developed significantly, facilitating increasingly complex interactions between humans and computers. This article examines the growing abstraction in NLP, from the early days of rudimentary template-based systems to cutting-edge conversational AI models like ChatGPT, and how these advancements have reshaped our interactions with machines.

**Template-Based Systems: NLP's Early Days**:
The first NLP systems used basic [template-based approaches](https://en.wikipedia.org/wiki/Template_processor) to produce and interpret language. These systems employed predefined templates with placeholders that were filled based on user input. Although limited in flexibility and capable of handling only elementary interactions, they established the foundation for more advanced NLP techniques.

**Rule-Based Systems and Syntax Analysis**: 
[Rule-based systems](https://en.wikipedia.org/wiki/Rule-based_system), which utilized grammatical and syntactic rules to analyze and generate language, marked the next stage in NLP evolution. These systems were more advanced than template-based approaches, offering a better understanding of language structure and increased flexibility. However, they still struggled with ambiguities and demanded considerable manual effort to develop and maintain the rules.

**Statistical Methods and Machine Learning**: 
The introduction of [statistical methods](https://cl.lingfil.uu.se/~nivre/docs/statnlp.pdf) and machine learning in the 1990s represented a considerable shift in NLP abstraction. These techniques enabled the automatic extraction of patterns and relationships from extensive datasets, allowing NLP models to learn from and adapt to real-world language data. This transition significantly improved tasks like part-of-speech tagging, named entity recognition, and sentiment analysis.

**Deep Learning and Word Embeddings**: 
The advent of [deep learning](https://en.wikipedia.org/wiki/Deep_learning) and [word embeddings](https://en.wikipedia.org/wiki/Word_embedding), such as [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) and [GloVe](https://en.wikipedia.org/wiki/GloVe), further advanced NLP by allowing models to learn dense vector representations of words that captured their semantic meanings. These embeddings facilitated more powerful and efficient models capable of handling complex language understanding tasks like machine translation and text summarization.

**Transformers and Contextualized Language Models**: 
The emergence of the [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) and contextualized language models, including [Bidirectional Encoder Representations from Transformers (BERT)](https://en.wikipedia.org/wiki/BERT_(language_model)) and [Generative Pre-trained Transformers (GPT)](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer), changed NLP by enabling models to learn deep contextual representations of words in a sentence. These models utilized self-attention mechanisms and large-scale unsupervised learning, resulting in significant performance enhancements across various NLP tasks, such as question answering, text classification, and more.

**Conversational AI and ChatGPT**: 
The latest advancements in NLP have led to sophisticated conversational AI models like [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT). Building upon the [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) , these models can engage in more natural, context-aware conversations with users. By leveraging large-scale pre-training and fine-tuning techniques, ChatGPT and similar models can understand and generate human-like responses, paving the way for various applications, from customer support to virtual assistants.

### Soft Programming Evolution

[Programming by example (PbE)](https://en.wikipedia.org/wiki/Programming_by_example) offers a powerful software development method that lets developers specify their intentions through examples instead of writing code. As PbE has progressed, it has become more abstract, capable of addressing increasingly complex tasks. This article investigates the growing abstraction in PbE, from its humble beginnings to the innovative use of ChatGPT prompting, and explores how training machine learning models can be viewed as a form of low-level programming by example.

**Early PbE: Macros and Scripting**:  
In PbE's early stages, simple [macros](https://en.wikipedia.org/wiki/Macro_(computer_science)) and scripting languages enabled users to automate repetitive tasks by recording their actions or offering example input-output pairs. While these systems had limited flexibility, they laid the groundwork for more advanced PbE methods.

**Spreadsheets and Formula Inference**: 
The widespread use of [spreadsheets](https://en.wikipedia.org/wiki/Spreadsheet) brought a new abstraction level to PbE. Users could create formulas based on example data, and spreadsheet software would automatically deduce the intended calculations. This method simplified data manipulation and analysis for non-programmers, allowing them to concentrate on the problem without concerning themselves with the underlying code.

**Inductive Programming and Synthesis**: 
[Inductive programming](https://en.wikipedia.org/wiki/Inductive_programming) and program synthesis techniques emerged as a more robust way to generate code from examples. These methods utilized formal techniques and constraint-solving algorithms to produce code that fulfilled given input-output pairs automatically. Although more flexible and expressive than previous PbE methods, inductive programming, and synthesis often demanded substantial computational resources and faced scalability challenges.

**Machine Learning: A New Form of PbE**: 
With the advent of machine learning, PbE entered a new phase. Training a machine learning model can be considered [a low-level PbE form](https://kozyrkov.medium.com/the-simplest-explanation-of-machine-learning-youll-ever-read-bebc0700047c)), where the model learns to execute a task based on example inputs and corresponding outputs. This approach enables greater flexibility and adaptability, as models can generalize from the provided examples to tackle unseen situations.

**ChatGPT Prompting: PbE Meets Conversational AI**: 
The emergence of [conversational AI models](https://en.wikipedia.org/wiki/Chatbot) like ChatGPT has unlocked new potential in programming by example. Users can supply natural language prompts and example data to guide the model in generating code, automating tasks, or solving intricate problems. ChatGPT's capacity to comprehend and produce human-like responses facilitates more intuitive and efficient interactions, narrowing the gap between users and code generation. Prompting enables intuitive interactions and bridges the gap between users and code generation.
