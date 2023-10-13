import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from io import StringIO

world_history = """
query;answer
What year did World War I begin?;1914
Who was the first President of the United States?;Washington
Which ancient civilization built the Great Pyramid of Giza?;Egypt
Who was the first woman to fly solo across the Atlantic Ocean?;Earhart
What is the period known as the "Dark Ages" in Europe often called?;Medieval
In which year did Christopher Columbus reach the Americas?;1492
Who was the first Emperor of China's Qin Dynasty?;Qin Shi Huang
What was the primary cause of the French Revolution?;Inequality
Which famous explorer led the first expedition to circumnavigate the globe?;Magellan
Who was the founder of the Mongol Empire?;Genghis Khan
What event marked the beginning of World War II?;Invasion of Poland
Who wrote "The Communist Manifesto" with Friedrich Engels?;Marx
What was the name of the ship on which Charles Darwin sailed to the Galápagos Islands?;Beagle
Who was the famous nurse during the Crimean War known as the "Lady with the Lamp"?;Nightingale
Which ancient empire built the city of Persepolis?;Persian
Who was the first woman in space?;Tereshkova
What is the ancient Egyptian writing system of pictorial symbols called?;Hieroglyphics
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
What was the famous ancient trade route connecting the East and West?;Silk
Who was the Roman general and dictator who was assassinated in 44 BC?;Julius Caesar
Which famous speech began with "Four score and seven years ago"?;Gettysburg
What was the historical period of renewed interest in art and learning in Europe?;Renaissance
Who was the founder of the Maurya Empire in ancient India?;Chandragupta
What was the first artificial satellite launched into space by the Soviet Union?;Sputnik
Who is known for the theory of relativity and the equation E=mc²?;Einstein
Which ancient civilization is known for its terracotta army?;China
Who was the first African American woman in space?;Mae Jemison
What was the system of forced labor in the Inca Empire called?;Mita
Who was the legendary king of Uruk in Mesopotamian mythology?;Gilgamesh
Which conflict is often referred to as the "Great War"?;World War I
Who is known for his heliocentric model of the solar system?;Copernicus
What was the name of the ship that carried the Pilgrims to North America in 1620?;Mayflower
Who was the first female Prime Minister of the United Kingdom?;Thatcher
Which battle marked the final defeat of Napoleon Bonaparte?;Waterloo
Who was the ancient Greek philosopher known for his contributions to ethics and politics?;Aristotle
What event is often considered the start of the American Civil War?;Fort Sumter
Who was the leader of the Soviet Union during the Cuban Missile Crisis?;Khrushchev
What ancient wonder was a colossal statue of the Greek god Zeus?;Statue
Who was the first European explorer to reach India by sea?;Vasco da Gama
Which document outlined the rights and liberties of the American colonists?;Declaration
Who was the founder of the Gupta Empire in ancient India?;Chandragupta
What was the name of the first permanent English settlement in North America?;Jamestown
Who was the ancient Greek philosopher known for his contributions to mathematics and geometry?;Euclid
Which city was the center of the Italian Renaissance?;Florence
Who was the author of "The Prince," a political treatise on leadership and power?;Machiavelli
What was the ancient city in Anatolia known for the Trojan War?;Troy
Who was the American civil rights leader known for his "I Have a Dream" speech?;King
Which empire was founded by Suleiman the Magnificent?;Ottoman
Who was the first woman to win a Nobel Prize and the only person to win Nobel Prizes in two different scientific fields?;Curie
What was the code of laws created by the Babylonian king Hammurabi?;Hammurabi's
Who was the French military leader who became Emperor of the French?;Napoleon
What is the term for the exchange of plants, animals, and cultures between the Old World and the New World after the voyages of Christopher Columbus?;Columbian
Who was the ancient Egyptian queen who aligned herself with Julius Caesar and Mark Antony?;Cleopatra
Which civilization is known for creating the first known writing system, Cuneiform?;Sumerians
Who was the American inventor known for the phonograph and the light bulb?;Edison
What was the name of the failed invasion of Cuba by Cuban exiles and the U.S. government in 1961?;Bay of Pigs
Who was the Italian explorer who discovered the Americas for Spain?;Columbus
Which ancient civilization built the city of Machu Picchu?;Inca
Who was the leader of the Soviet Union during the Cuban Missile Crisis?;Khrushchev
What was the ancient wonder known as the hanging gardens?;Babylon
Who was the first woman to fly solo across the Atlantic Ocean?;Earhart
Which ancient civilization is known for its pyramids, including the Great Pyramid of Giza?;Egypt
Who was the founder of the Maurya Empire in ancient India?;Chandragupta
What was the name of the ship on which Charles Darwin sailed to the Galápagos Islands?;Beagle
Who was the Roman general and dictator who was assassinated in 44 BC?;Julius Caesar
What was the system of forced labor in the Inca Empire called?;Mita
Who was the legendary king of Uruk in Mesopotamian mythology?;Gilgamesh
What was the historical period of renewed interest in art and learning in Europe?;Renaissance
Who was the founder of the Gupta Empire in ancient India?;Chandragupta
What was the name of the ship that carried the Pilgrims to North America in 1620?;Mayflower
Who was the first female Prime Minister of the United Kingdom?;Thatcher
Which battle marked the final defeat of Napoleon Bonaparte?;Waterloo
What event is often considered the start of the American Civil War?;Fort Sumter
Who was the leader of the Soviet Union during the Cuban Missile Crisis?;Khrushchev
Who was the first European explorer to reach India by sea?;Vasco da Gama
What was the name of the first permanent English settlement in North America?;Jamestown
Who was the author of "The Prince," a political treatise on leadership and power?;Machiavelli
What was the ancient city in Anatolia known for the Trojan War?;Troy
Who was the American civil rights leader known for his "I Have a Dream" speech?;King
Which empire was founded by Suleiman the Magnificent?;Ottoman
Who was the first woman to win a Nobel Prize and the only person to win Nobel Prizes in two different scientific fields?;Curie
What was the code of laws created by the Babylonian king Hammurabi?;Hammurabi's
Who was the French military leader who became Emperor of the French?;Napoleon
What is the term for the exchange of plants, animals, and cultures between the Old World and the New World after the voyages of Christopher Columbus?;Columbian
Who was the ancient Egyptian queen who aligned herself with Julius Caesar and Mark Antony?;Cleopatra
Which civilization is known for creating the first known writing system, Cuneiform?;Sumerians
Who was the American inventor known for the phonograph and the light bulb?;Edison
What was the name of the failed invasion of Cuba by Cuban exiles and the U.S. government in 1961?;Bay of Pigs
Who was the Italian explorer who discovered the Americas for Spain?;Columbus
Which ancient civilization built the city of Machu Picchu?;Inca
What was the name of the famous ancient trade route connecting the East and West?;Silk
Who was the founder of the Mongol Empire?;Genghis Khan
What event marked the beginning of World War II?;Invasion of Poland
Who wrote "The Communist Manifesto" with Friedrich Engels?;Marx
What is the period known as the "Dark Ages" in Europe often called?;Medieval
In which year did Christopher Columbus reach the Americas?;1492
Who was the first Emperor of China's Qin Dynasty?;Qin Shi Huang
What was the primary cause of the French Revolution?;Inequality
Which famous explorer led the first expedition to circumnavigate the globe?;Magellan
Who was the founder of the Maurya Empire in ancient India?;Chandragupta
What was the first artificial satellite launched into space by the Soviet Union?;Sputnik
Who is known for the theory of relativity and the equation E=mc²?;Einstein
Which ancient civilization is known for its terracotta army?;China
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
What was the famous ancient trade route connecting the East and West?;Silk
Who was the founder of the Mongol Empire?;Genghis Khan
What event marked the beginning of World War II?;Invasion of Poland
Who wrote "The Communist Manifesto" with Friedrich Engels?;Marx
What is the period known as the "Dark Ages" in Europe often called?;Medieval
In which year did Christopher Columbus reach the Americas?;1492
Who was the first Emperor of China's Qin Dynasty?;Qin Shi Huang
What was the primary cause of the French Revolution?;Inequality
Which famous explorer led the first expedition to circumnavigate the globe?;Magellan
Who was the founder of the Maurya Empire in ancient India?;Chandragupta
What was the first artificial satellite launched into space by the Soviet Union?;Sputnik
Who is known for the theory of relativity and the equation E=mc²?;Einstein
Which ancient civilization is known for its terracotta army?;China
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
What was the name of the ship on which Charles Darwin sailed to the Galápagos Islands?;Beagle
Who was the famous nurse during the Crimean War known as the "Lady with the Lamp"?;Nightingale
Which ancient empire built the city of Persepolis?;Persian
Who was the first woman in space?;Tereshkova
What is the ancient Egyptian writing system of pictorial symbols called?;Hieroglyphics
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
What was the famous ancient trade route connecting the East and West?;Silk
Who was the founder of the Mongol Empire?;Genghis Khan
What event marked the beginning of World War II?;Invasion of Poland
Who wrote "The Communist Manifesto" with Friedrich Engels?;Marx
What is the period known as the "Dark Ages" in Europe often called?;Medieval
In which year did Christopher Columbus reach the Americas?;1492
Who was the first Emperor of China's Qin Dynasty?;Qin Shi Huang
What was the primary cause of the French Revolution?;Inequality
Which famous explorer led the first expedition to circumnavigate the globe?;Magellan
Who was the founder of the Maurya Empire in ancient India?;Chandragupta
What was the first artificial satellite launched into space by the Soviet Union?;Sputnik
Who is known for the theory of relativity and the equation E=mc²?;Einstein
Which ancient civilization is known for its terracotta army?;China
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
What was the name of the ship on which Charles Darwin sailed to the Galápagos Islands?;Beagle
Who was the famous nurse during the Crimean War known as the "Lady with the Lamp"?;Nightingale
Which ancient empire built the city of Persepolis?;Persian
Who was the first woman in space?;Tereshkova
What is the ancient Egyptian writing system of pictorial symbols called?;Hieroglyphics
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
What was the famous ancient trade route connecting the East and West?;Silk
Who was the founder of the Mongol Empire?;Genghis Khan
What event marked the beginning of World War II?;Invasion of Poland
Who wrote "The Communist Manifesto" with Friedrich Engels?;Marx
What is the period known as the "Dark Ages" in Europe often called?;Medieval
In which year did Christopher Columbus reach the Americas?;1492
Who was the first Emperor of China's Qin Dynasty?;Qin Shi Huang
What was the primary cause of the French Revolution?;Inequality
Which famous explorer led the first expedition to circumnavigate the globe?;Magellan
Who was the founder of the Maurya Empire in ancient India?;Chandragupta
What was the first artificial satellite launched into space by the Soviet Union?;Sputnik
Who is known for the theory of relativity and the equation E=mc²?;Einstein
Which ancient civilization is known for its terracotta army?;China
Who was the first American astronaut to orbit the Earth?;Glenn
Which war is often referred to as the "War of 1812"?;Second
Who was the last Pharaoh of Ancient Egypt?;Cleopatra
Which treaty officially ended World War I?;Versailles
"""

df_history = pd.read_csv(StringIO(world_history), delimiter = ';')
df_history.drop_duplicates(ignore_index = True)
df_history = df_history.iloc[0:100]

# Function to find the most similar response
def get_most_similar_response(df, query, top_k=1):
    vectorizer = TfidfVectorizer()
    all_data = list(df['query']) + [query]
    tfidf_matrix = vectorizer.fit_transform(all_data)

    document_vectors = tfidf_matrix[:-1]
    query_vector = tfidf_matrix[-1]
    similarity_scores = cosine_similarity(query_vector, document_vectors)

    sorted_indexes = similarity_scores.argsort()[0][::-1][:top_k]

    most_similar_queries = df.iloc[sorted_indexes]['query'].values
    most_similar_responses = df.iloc[sorted_indexes]['answer'].values

    # Concatenate the responses into a single string
    responses_qry = " ".join(most_similar_queries)
    responses_str = " ".join(most_similar_responses)

    return responses_qry,responses_str

df = pd.DataFrame(df_history)

# Streamlit app
st.title("History Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me a question about history."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    responses = get_most_similar_response(df_history, prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        for response in responses:
            st.markdown(f"{response}")

    # Add assistant response to chat history
    for response in responses:
        st.session_state.messages.append({"role": "assistant", "content": f"{response}"})