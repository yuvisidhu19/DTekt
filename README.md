# Description
DTekt is a chrome extension that can identify counterfeit products on Amazon using sentiment analysis of the product reviews by only "verified purchase" buyers i.e. the review of the customers who have actually bought the product. Sentiment analysis applies a mix of statistics, natural language processing (NLP), and machine learning to identify and extract subjective information from text files, for instance, a reviewer’s judgments and assessments about a particular product. This extension can scrape the website and collect the necessary data which is further fed to a pre-trained ML (Bert) model, which in turn, returns a rating from 1 to 100. The higher the rating, the higher is the product's authenticity.

Demo: https://www.youtube.com/watch?v=xn-f6er939U&ab_channel=JashandeepSingh


# Methodology
Two types of dataset are used to create models. One (fake.txt and real.txt) is used to classify whether the given text implies if the product is a counterfeit or not. But due to lack of data, another dataset (pos.txt and neg.txt) was used which classifies if the given text implies a positive emotion or a negative emotion. Sometimes, a negative comment can imply that the customer is not satisfied with a product or the product is of poor quality, which might be due to the fact that the product is a counterfeit. So, two bert models have been trained to produce a negativeness score and a fakeness score and both are combined in a way, providing more weight to fakeness score and less weight to negativeness score, to generate a final score which implies the authenticity of the product.

# Formula used
```
counterfeit_score = fakeness * 0.7 + negativeness * 0.3

authenticity_score =  round(1 - counterfeit_score)*100
```

# Screenshot
![WhatsApp Image 2022-07-31 at 7 07 31 PM](https://user-images.githubusercontent.com/67970877/182040545-c2ff3936-b746-447c-8924-8f7ea8ce0af4.jpg)
