from transformers import T5Tokenizer, T5ForConditionalGeneration

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
t5_tokenizer = T5Tokenizer.from_pretrained(T5_PATH)

def getSummary(input):
    # encode the text into tensor of integers using the tokenizer
    inputs = t5_tokenizer.encode("summarize: " + input, return_tensors="pt", max_length=512, padding="max_length", truncation=True)
    summary_ids = t5_model.generate(inputs, num_beams=int(2), no_repeat_ngram_size=3, length_penalty=2, min_length=120, max_length=300, early_stopping=True)
    output = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    # print(summary_ids)
    # print(output)
    return output