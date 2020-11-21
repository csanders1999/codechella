import pandas as pd
import numpy as np
from sklearn.feature_extraction.txt import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#Helper functions
def get_bio_from_index(index):
    return df[df.index == index]["bio"].values[0]

def get_index_from_bio(bio):
    return df[df.bio == bio]["index"].values[0]

#STEP ONE: CSV data file reader
df = pd.read_csv("professional_data.csv")

#STEP TWO: select features
features = ['keywords', 'sector', 'buzzwords','overview']

#STEP THREE: Create a column in DF which combines all selected features
for feature in features:
    df[feature]=df[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords'+" "+row['sector']+" "+row['buzzwords']+" "+row['overview']]
    except:
        print "Error:", row

    df['combined_features'] = df.apply(combine_features, axis=1)


#STEP FOUR: Create count matrix from this new combined column
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])

#STEP FIVE: Compute the cosine similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)
# user used words x,y,z.... user seems to be in sector x..
users_sector = #technology, healthcare, retail, etc...

#STEP SIX: get index of suggested buzzwords from its sector
sector_index = get_index_from_bio(users_sector)

common_buzzwords = list(enumerate(cosine_sim[sector_index]))

#STEP SEVEN: Get list of suggested bios from users in similar sector
sorted_similar_users = sorted(common_buzzwords, key=lambda x:x[1],reverse=True)

#STEP EIGHT: Print first x amount of bios from professionals in that sector
i=0
for element in sorted_similar_users:
    print get_bio_from_index(element[0])
    i=i+1
    if i> #amount of bios

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
