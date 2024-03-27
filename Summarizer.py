#Importing needed modules.

from transformers import pipeline
from os import listdir , mkdir
from time import sleep

def Summarize(path,replace=False,mx_length=130,mn_length=30)->None:
    
    '''
    Summarize text files using transformers pipeline method.

    Return -> None.
    
    Parameters:
        path: path of text files that you want to summrize (str).
        
        replace: default-> False, If True it replaces summarized text in original file.
                 If False, it makes a "Result" folder in path then saves the summarized texts into it
                 with a new name "summarized_(original name)" (boolean).
                 
        mx_length: max length of words (int).
        
        mn_length: min length of words (int).
    '''
    if replace:
        
        summarizer = pipeline('summarization')
        for p in listdir(path):
            with open(f'{path}\\{p}','r') as file:
                summarized_text = summarizer(file.read(),max_length=mx_length,min_length=mn_length,do_sample=False)
                with open(f'{path}\\{p}','w') as target_file:
                    target_file.write(summarized_text[0]['summary_text'])
                    
    else :
        
        mkdir(f'{path}\\Result')
        summarizer = pipeline('summarization')
        for p in listdir(path):
            if p == 'Result':
                continue
            with open(f'{path}\\{p}','r') as file:
                summarized_text = summarizer(file.read(),max_length=mx_length,min_length=mn_length,do_sample=False)
                with open(f'{path}\\Result\\summarized_{p}','w') as target_file:
                    target_file.write(summarized_text[0]['summary_text'])

#Testing the function.
 
Summarize('D:\\python_text_files\\Texts for LLM')
sleep(2)