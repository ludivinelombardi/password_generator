import random 
import streamlit as st

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generate_password(characters):
	password = []

	for i in range(characters):
		password.append(random.choice(chars))

	random.shuffle(password)
	return ("".join(password))
    

st.title("Password Generator")
st.info("Strong password are important. With this generator, create strong password and protect all your accounts.")
mdp1 = st.slider(label="Pick a number", min_value=6, max_value=26)
if st.button(label="Generate"):
    passwd = generate_password(mdp1)
    st.success('You generated a strong password \n')
    st.subheader(passwd) 
