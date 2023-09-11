# AI-Powered Educational Chatbot

**1. Problem Statement:**
Educational institutions face challenges in providing personalized and efficient support to students seeking academic assistance. Students often have questions that can be addressed by leveraging existing knowledge, but the availability of human resources to answer these questions can be limited. This results in delayed responses and inefficient utilization of resources.

**2. Solution:**
We propose the development of an AI-powered educational chatbot to address these challenges. The chatbot will use advanced text analysis, machine learning models, and GPT-3.5 Turbo to provide instant and personalized responses to students' academic queries. The chatbot will leverage pre-existing question-answer pairs, learn from user interactions, and generate relevant and accurate answers.

**3. Tech Stack Used:**
- Python for programming and scripting
- GPT-3.5 Turbo for natural language generation
- Scikit-learn and Keras for machine learning models
- TensorFlow for deep learning
- pandas and numpy for data manipulation
- Flask for building the web application
- HTML/CSS for front-end design

**4. Organization/Institution:** Bennett University

**5. Individual/Team:**
The project will be undertaken by a team of four senior computer science students with expertise in natural language processing, machine learning, and web development.

**6. Duration:** 3 months

**7. Screenshots:**
![1](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/a40dc803-4083-40f5-a112-549b612e2e4e)
![2](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/364da545-b50f-453b-b34e-5c6c104db17e)
![3](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/549d1a08-31c1-43cd-ab1d-3d6a795ab1d4)
![4](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/09f366e6-3c89-4fac-83de-8d58ed67532c)
![5](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/f7b024cf-9e37-4c11-85b7-e77db9d576e9)
![6](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/75ac6dbc-2a25-4d9d-a5e8-b4355c184fa5)
![7](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/27ece6b7-db7a-4e43-b1fb-431c8c736d49)
![8](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/bf18dc52-c5d2-45dd-8313-5eb87786f5da)
![9](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/9a313d5d-6d2c-4455-b3d1-ad3ef8d02aca)
![10](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/4241f6f3-c450-4f5e-bf19-184e2327f9b2)
![11](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/c14834da-399a-4986-a02f-288ab741fbfb)
![12](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/d9f8e39c-176f-4ef0-9703-dbf04a19dbc4)
![13](https://github.com/heathbrew/AI-Powered-Educational-Chatbot/assets/55629425/04845fa4-ff39-414d-9eec-91969949abe4)



**8. Observations:**
- Improve student satisfaction by providing instant and accurate responses.
- Analyze user interactions to enhance the chatbot's knowledge base.
- Monitor user feedback to identify areas for improvement.
- Evaluate the impact on resource utilization within the institution.

**9. Link to Project:**
The project documentation, source code, and live demo will be available on the GitHub repository: https://github.com/heathbrew/AI-Powered-Educational-Chatbot

**`send_gptnew` Function: AI-Powered Response Generation**
This pivotal function orchestrates the AI-powered response generation process within the educational chatbot. By leveraging the GPT-3.5 Turbo model and various similarity analyses, it crafts relevant and informative responses based on the user's input prompt and the desired response temperature.

**Function Steps:**
1. **Similarity Calculation:** The function commences by calculating the similarity value between the user's input prompt and prompts stored in the `vecstore`. This calculation is facilitated by the `top_similar_prompts` method, which gauges the likeness between the provided prompt and existing data.

2. **Database Check:** If the input prompt is found within the `qa_dict` and corresponds to the specified temperature, the chatbot promptly fetches the associated response from the dictionary. This expedited retrieval enhances user experience by directly providing accurate responses.

3. **Similarity Threshold Check:** Should the calculated similarity value surpass a pre-defined threshold (0.2), the function accesses a conversation similar to the input prompt from the `vecstore`. Utilizing the `extractive_summary` method, an extractive summary is crafted from this conversation. This summary succinctly encapsulates relevant information, further enhancing the user's experience.

4. **GPT-3.5 Turbo Interaction:** If neither of the previous conditions is met, implying that the prompt is not found in `qa_dict` or lacks high similarity, the function engages the GPT-3.5 Turbo model. The generated response is enriched with details such as personality type and learning style, both extracted through dedicated machine learning models.

5. **Updating Knowledge Base:** The newly generated response is seamlessly incorporated into the `qa_dict`, thereby enriching the chatbot's knowledge base. Subsequently, the embeddings and associated metadata are updated to reflect this recent addition.

**Loading Models and Tokenizers:**
In alignment with the chatbot's multifaceted functionality, the code encompasses loading procedures for essential machine learning models and tokenizers. These components empower the chatbot to classify personality types, ascertain learning styles, and contribute to the overall sophistication of its responses.

**Loading QA Data:**
The chatbot's responsiveness is rooted in the availability of relevant data. The code ensures a steady supply of such data by harnessing the `load_qa_data` function to read question-answer pairs and associated metadata from a CSV file. This foundation of knowledge facilitates the chatbot's capacity to furnish tailored and informative responses to user queries.

Through the systematic orchestration of these processes, the `send_gptnew` function embodies the chatbot's prowess in intelligently crafting responses, thereby augmenting the educational support experience.
