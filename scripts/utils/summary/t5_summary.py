from transformers import T5TokenizerFast, T5ForConditionalGeneration
import re

"""
Download following files:
1. config.json
2. pytorch_model.bin
3. spiece.model
4. tokenizer.json
Make a directory named 't5-base' inside 'model' 
Place the downloaded files inside 't5-base' directory 
Link: https://huggingface.co/t5-base/tree/main
"""
T5_PATH = './model/t5-base' # T5 model path
# initialize the model architecture and weights
t5_model = T5ForConditionalGeneration.from_pretrained(T5_PATH)
# initialize the model tokenizer
t5_tokenizer = T5TokenizerFast.from_pretrained(T5_PATH)

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
            # print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    return chunks

def getSummary(text):
    text = pre_process(text)
    chunks = get_chunks(text)
    
    final_output = ""
    for input in chunks:
        inputs = t5_tokenizer.encode("summarize: " + input, return_tensors="pt", max_length=512, padding="max_length", truncation=True)
        summary_ids = t5_model.generate(inputs, num_beams=int(2), no_repeat_ngram_size=3, length_penalty=2, min_length=30, max_length=120, early_stopping=True)
        output = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        final_output = post_process(output)
        final_output = final_output + " " + output
    
    return final_output