from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import re

"""
Download following files:
1. config.json
2. pytorch_model.bin
3. spiece.model
4. tokenizer.json

Make a directory named 'pegasus' inside 'model' 
Place the downloaded files inside 'pegasus' directory 
Link: https://huggingface.co/google/pegasus-xsum/tree/main
"""

PEGASUS_PATH = './model/pegasus'
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = PegasusTokenizer.from_pretrained(PEGASUS_PATH)
model = PegasusForConditionalGeneration.from_pretrained(PEGASUS_PATH).to(device)

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def pre_process(input):
    input = deEmojify(input)
    input = input.replace('.', '.<eos>')
    input = input.replace('?', '?<eos>')
    input = input.replace('!', '!<eos>')
    return input

def post_process(output):
    final_output=""
    final_output += output[0].upper()
    for i in range(1,len(output)):
        if i-2>=0 and output[i-2]==".":
            final_output += output[i].upper()
        else:
            final_output += output[i]
    return final_output

def get_chunks(input, max_chunk_size = 300):
    
    sentences = input.split('<eos>')
    current_chunk = 0 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk_size:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    return chunks

def getSummary(text):
    text = pre_process(text)
    chunks = get_chunks(text)
    
    final_output = ""
    for input in chunks:
        input = pre_process(input)
        batch = tokenizer(input, truncation=True, padding='longest', return_tensors="pt").to(device)
        translated = model.generate(**batch)
        output = tokenizer.batch_decode(translated, skip_special_tokens=True)
        final_output = final_output + " " + post_process(output)
    
    return final_output