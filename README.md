# PromptQG
This is the repository for our FIRE 2023 paper "Harnessing the Power of Prompt-based Techniques for Generating School-Level Questions using Large Language Models". Code and Dataset coming soon!

## Definitions
Before delving into the details of the dataset, let's establish some key definitions for better understanding:

1. Context: A segment upon which the question is formed.

2. Long Prompt: A long textual cue for the question (i.e., a longer sequence of words or phrases, covering the main theme of the context).

3. Short Prompt: A short textual cue for the question (i.e., a condensed representation of the key information or focus of the context). Primarily, we select a noun phrase from the beginning portion of the context to serve as a short prompt.

4. Question: A deep question that aligns with the context and is coherent with the prompts.

![workflow_fire](https://github.com/my625/PromptQG/assets/149454879/b5636bf0-8508-4428-9427-bd2c2ece8864)

Welcome to our training dataset named "Data.zip"! This dataset is designed for training purposes and contains valuable information for three different settings: long prompt, short prompt, and without prompt. The dataset is comprised of three CSV files, each catering to a specific setting:

  (i)   QAG_Train_Long.csv
  
 (ii)   QAG_Train_Short.csv
 
(iii)   QAG_Train_wop.csv

File Structure
Each CSV file within the dataset consists of two essential fields:

a. question: This field contains the actual question that the dataset is centered around.
b. context_Prompt: The context field is followed by the respective prompt (long, short, or without prompt), providing additional context for understanding the given question.

## File Descriptions

1. QAG_Train_Long.csv
   
This file is tailored for training scenarios where long prompts are utilized to enhance the context of the questions. The "context_Prompt" field in this CSV file contains the context followed by the long prompt associated with each question.


3. QAG_Train_Short.csv
   
In this file, the training dataset is configured for scenarios where short prompts are employed. The "context_Prompt" field contains the concise prompt following the context for each question.

5. QAG_Train_wop.csv
   
For scenarios without any prompts, this file provides a dataset that focuses solely on the question and its context without any additional prompts. The "context_Prompt" field in this CSV file contains only the context relevant to each question.

## Contact Information
For any questions, concerns, or feedback regarding the dataset, please contact us at [subhankar.ai@kgpian.iitkgp.ac.in].

Thank you for choosing our dataset for your research and training needs!
