import os
import spacy
nlp = spacy.load("en_core_web_sm")
import torch
#!pip install transformers
#!pip install transformers[sentencepiece]
#uu=open("IN-Abs/test-data/stats-IN-test.txt")
#ll=uu.readlines()
#ll=os.listdir("/DATA1/aniket/raw_files/IN-Abs/judgement/")
no_of_words=0
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, Trainer, TrainingArguments

tokenizer = AutoTokenizer.from_pretrained("facebook/mbart-large-50")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/mbart-large-50")
torch_device="cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForSeq2SeqLM.from_pretrained("ouput_model_p/", use_cache=True).to(torch_device)
def summerize(text, max_len, min_len):
    '''
    Function to generate summary using Pegasus
    input:  nested_sentences - chunks
            max_l - Maximum length
            min_l - Minimum length
    output: document summary
    '''
    #print(text)
    try:
        input_tokenized = tokenizer.encode(text, return_tensors='pt',max_length=100,truncation=True).to(torch_device)
        summary_ids = model.generate(input_tokenized,
                                          num_beams=9,
                                          length_penalty=0.1,
                                          min_length=min_len,
                                          max_length=max_len,
                                    )
        #print(summary_ids)
        summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0]
        #print(summary)
        return summary
    except:
        return

import os
temp1=open("C_test.txt","r",encoding='utf-8')
text1=temp1.readlines()
for i in range(0,len(text1)):
    text1[i]=text1[i].strip("\n")
#import os
temp2=open("P_test.txt","r",encoding='utf-8')
text2=temp2.readlines()
for i in range(0,len(text1)):
    text2[i]=text2[i].strip("\n")
fff=open("output_model_t5_wop.txt","w")
for i in range(0,len(text1)):
	print(text1[i],text2[i])
	output=summerize(text1[i]+text2[i],50,20)
	print(output)
	fff.write(output+"\n")
