import os
import pickle
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity

def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            qa_dict[row['prompt']] = {
                'returnstring': row['returnstring'],
                'mbti': row['mbti'],
                'learning': row['learning'],
                'temperature': float(row['temperature'])
            }
    return qa_dict

class TextSimilarity:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def update_embeddings(self, qa_dict, save=True):
        vecstorepath = 'vecstore.pkl'
        vectorizerpath = 'vecstorevectorizer.pkl'

        # Load or initialize the vectorizer
        try:
            with open(vectorizerpath, 'rb') as f:
                self.vectorizer = pickle.load(f)
        except FileNotFoundError:
            pass  # vectorizer will be initialized with default parameters

        # Load or initialize the vecstore
        try:
            with open(vecstorepath, 'rb') as f:
                vecstore = pickle.load(f)
        except FileNotFoundError:
            vecstore = {}

        prompts = list(qa_dict.keys())
        texts = [qa_dict[prompt]['returnstring'].lower() for prompt in prompts]

        vectors = self.vectorizer.fit_transform(texts)

        for i, prompt in enumerate(prompts):
            vec = vectors[i].toarray()[0]
            vec = vec / np.linalg.norm(vec)
            vecstore[prompt] = vec

        if save:
            # Save the vectorizer
            with open(vectorizerpath, 'wb') as f:
                pickle.dump(self.vectorizer, f)

            # Save the vecstore
            with open(vecstorepath, 'wb') as f:
                pickle.dump(vecstore, f)

        return vecstore

    def top_similar_ques(self, user_query, vecstore):
        prompt_vector = self.vectorizer.transform([user_query]).toarray()[0]
        prompt_vector = prompt_vector / np.linalg.norm(prompt_vector)

        similarities = []
        for prompt, vector in vecstore.items():
            similarity = np.dot(prompt_vector, vector)
            similarities.append((prompt, similarity))

        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        return list(sorted_similarities)

    def top_similar_prompts(self, user_query, vecstore):
        prompt_vector = self.vectorizer.transform([user_query]).toarray()[0]
        prompt_vector = prompt_vector / np.linalg.norm(prompt_vector)

        similarities = []
        for prompt, vector in vecstore.items():
            similarity = np.dot(prompt_vector, vector)
            similarities.append((prompt, similarity))

        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        return [(prompt, score) for prompt, score in sorted_similarities]
    
    def top_similar_docs(self, prompt, vecstore, qa_dict):
        prompt_vector = self.vectorizer.transform([prompt]).toarray()[0]
        prompt_vector = prompt_vector / np.linalg.norm(prompt_vector)

        similarities = []
        prompts = list(qa_dict.keys())
        
        for prompt in prompts:
            vector = vecstore[prompt]
            similarity = np.dot(prompt_vector, vector)
            similarities.append(similarity)

        most_similar_index = similarities.index(max(similarities))
        most_similar_prompt = prompts[most_similar_index]
        most_similar_returnstring = qa_dict[most_similar_prompt]['returnstring']
        most_similar_mbti = qa_dict[most_similar_prompt]['mbti']
        most_similar_learning = qa_dict[most_similar_prompt]['learning']
        most_similar_temperature = qa_dict[most_similar_prompt]['temperature']

        return list([most_similar_prompt, most_similar_returnstring, most_similar_mbti, most_similar_learning, most_similar_temperature])
    
    def extractive_summary(self, prompt, similar_conversation, max_features=1000):
        # create vectorizer
        vectorizer = TfidfVectorizer(max_features=max_features)

        # convert list to text
        text = ''.join(str(elem) for elem in similar_conversation)

        # clean text
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'\s+', ' ', text)

        # extractive summarization using cosine similarity
        sentences = re.split('[.?]', text)
        sentences = [sentence.strip() for sentence in sentences if len(sentence) > 10]
        sentences_vec = vectorizer.fit_transform(sentences)
        prompt_vec = vectorizer.transform([prompt])
        similarity_scores = cosine_similarity(sentences_vec, prompt_vec)

        # sort by similarity scores and take top sentences
        num_sentences = min(5, len(sentences))
        top_indices = similarity_scores.flatten().argsort()[::-1][:num_sentences]
        top_sentences = [sentences[index] for index in top_indices]

        # join top sentences into summary
        summary = ' '.join(top_sentences)

        return summary