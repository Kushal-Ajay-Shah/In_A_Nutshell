import math
import string
  
# splitting data into words
# translation table is a global variable
# mapping upper case to lower case and
# punctuation to spaces
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)
# returns a list of the words
# in the file
def get_words_from_data(text): 
      
    text = text.translate(translation_table)
    word_list = text.split()
      
    return word_list

# counts frequency of each word
# returns a dictionary which maps
# the words to  their frequency.
def count_frequency(word_list): 
      
    D = {}
      
    for new_word in word_list:
          
        if new_word in D:
            D[new_word] = D[new_word] + 1
              
        else:
            D[new_word] = 1
              
    return D

def word_frequencies(data): 
      
    word_list = get_words_from_data(data)
    freq_mapping = count_frequency(word_list)

    return freq_mapping

# returns the dot product of two documents
def dotProduct(D1, D2): 
    Sum = 0.0
      
    for key in D1:
          
        if key in D2:
            Sum += (D1[key] * D2[key])
              
    return Sum

def vector_angle(D1, D2): 
    numerator = dotProduct(D1, D2)
    print(numerator)
    denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
    print(denominator)
    return numerator / denominator

def documentSimilarity(data_1, data_2):
      
    sorted_word_list_1 = word_frequencies(data_1)
    sorted_word_list_2 = word_frequencies(data_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    return distance   

# print(documentSimilarity('A hardworking 19-year-old boy broke the internet, inspiring millions with his determination to pursue his goals of joining the Indian Army. Now, as his video has garnered attention from all corners, he admitted it’s “overwhelming” and asked all to just let him concentrate on his dream. It was filmmaker Vinod Kapri who initially caught the boy on camera running through Noida late in the night. The video made him an internet sensation overnight, also connecting the boy to those who came forward to help. Kapri once again met the boy to check up on him, and how he was doing after getting so much attention, particularly from the media. Talking about his popularity, the boy identified as Pradeep Mehra from Almora in Uttarakhand, said, “Itna bhi woh nahi hona hai ki main zyada upar char gaya hoon (I don’t want it to seem that I am flying too high).” Afraid he might get distracted from his goal, he added: “Agar mujhe zyada hi upar chhada denge toh jo mera goal hai na main uspe focus nahi kar payunga. Matlab mein zyada interview nahi dena chhata kisiko (If they give me too much fame, I won’t be able to focus on my goal. Hence I don’t want to do too many interviews)”.',"Every single day new chapters of success are written. But what makes them successful is the effort that has been put in for years. A 19-year-old Indian boy, named Pradeep, seems to be putting the hard work despite several hardships in his life. The civil services aspirant's video went viral on social media after he shared his vision and routine with filmmaker Vinod Kapri. While the entire country has been bowled over by Pradeep's relentless attitude, cricketing personalities like Harbhajan Singh and Kevin Pietersen have also reacted to the viral video. “This will make your Monday morning! What A Guy!,” tweeted Pietersen. This will make your Monday morning! What A Guy! “Champions are made like this .. whether on sports field or anything they do in life .. He will be a winner thank you vinod for sharing this .. yes PURE GOLD,” Harbhajan reacted. champions are made like this .. whether on sports field or anything they do in life .. He will be a winner 'Last night at 12 o'clock on the road of Noida, I saw this boy running very fast with a bag on his shoulder. I thought he is in some trouble, lift should be given. Repeatedly offered lift but it declined... You will fall in love with this child if you listen to the reason,' Kapri had captioned the clip shared on social media. In the video, Kapri had asked Pradeep about the reason behind his run. Answering the movie director, the teenage boy said: 'I always run on my way back home (from McDonald's Noida Sector 16 where he works).' Kapri even offered a lift to Pradeep but he refused saying that would interrupt his training. On being further questioned about the topic, Pradeep said that he wants to represent the Indian Army.'"))