# In A Nutshell

### KADAMM

## Description

* User can search for which relevant articles would be fetched.
* User can select which articles he/she wants to summarize.
* Abstract summaries of each unique article is generated. Uniqueness of an article is determined by its cosine distance with other articles.
* User can also upload articles in .txt/.docx format to get their summaries. 

## Links
* GitHub Repo link: [Link to repository](https://github.com/Kushal-Ajay-Shah/In_A_Nutshell)

## Technology stack

Tools and technologies that were learnt and used in the project.

1. Python
2. HTML
3. CSS
4. JavaScript
5. Flask
6. PyTorch
7. transformers

## Project Setup

>Clone GitHub Repository
```
git clone https://github.com/Kushal-Ajay-Shah/In_A_Nutshell.git
```
>Create a venv/conda environment 
* For venv:
```
python3 -m venv /path/to/new/virtual/environment
```
* For conda:
```
conda create --name /name/of/environment
```
>Activate virtual environmenrs
* For venv
```
source /path/to/new/virtual/environment/bin/activate
```
* For conda
```
conda activate /name/of/environment
```
>Install requirements 

Navigate to the repo directory then:- 
* For venv
```
pip3 install -r requirements.txt
```
* For conda
```
conda install --file requirements.txt
```
Download following files:
[Link](https://huggingface.co/t5-base/tree/main)
1. config.json
2. pytorch_model.bin
3. spiece.model
4. tokenizer.json

Make a directory named 't5-base' inside 'model' 
Place the downloaded files inside 't5-base' directory 

## Usage
> Run the **app.py** file
```
python3 app.py
```
> You can now see the demo of the website on http://127.0.0.1:8000/

## Applications
>Sometimes it is required to refer to online news articles to obtain further information about a topic, trend or event beyond what is already known. It would take hours of manual effort to go through these news articles, understand them and assimilate key findings. Often information would be spread out and not available in a single article.

>Thus reading a summary might help the user to avoid reading the entire article or may help him decide if he wants to read that article in detail.


## Future scope
>Currently, the project provides Single-Doc Abstractive Summary.

>Our next goal would be to provide a Multi-Doc Abstractive Summary. Through this the user can get summary of multiple docs thus covering more information while taking into similarity between articles. 

## Screenshots

![Screenshot alt text](https://img.freepik.com/free-photo/blue-purple-technology-circuit_73426-205.jpg "Here is a screenshot")