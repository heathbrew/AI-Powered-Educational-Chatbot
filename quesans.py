import pandas as pd

# create an empty dataframe with the desired headers
df = pd.DataFrame(columns=['prompt', 'returnstring', 'mbti', 'learning','temperature'])

# write the dataframe to a CSV file
df.to_csv('question_answer.csv', index=False)
