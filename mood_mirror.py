import streamlit as st
import subprocess
from PIL import Image
import os
import random

st.set_page_config(page_title="Mood Analyzer", layout="centered")

st.title("Welcome to Mood Mirror!✨")
st.write("Upload a selfie and let a Spandan Certified Intelligence guess your mood!")
st.write(".....And Potentially cheer you Up!!")

img_ext = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
image_dir = r"memes\image"
img_files=[]

for i in os.listdir(image_dir):
    if str(i).endswith(img_ext):
        img_files.append(i)


if img_files:
    random_image = random.choice(img_files)
    random_image_path = os.path.join(image_dir, random_image) 


st.subheader("Before we start, let me show you something cool!")

if st.button("Click me!"):
    if random_image_path:
        st.image(random_image_path, caption="Here is a Random Meme!", use_column_width=True)
    else:
        st.warning("No random image available.") 




uploaded_file = st.file_uploader("📤 Upload your image bruv!", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_path = os.path.join("uploaded_image.jpg")
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    
    st.image(Image.open(image_path), caption="Your uploaded image", use_column_width=True)

   
    with open("input_path.txt", "w") as f:
        f.write(image_path)

    
    with st.spinner("Analyzing your mood... 🤖 Whatever it turn out to be!\n Just make sure to always put up a wide Smile!\n For That's the best thing you can wear!"):
        result = subprocess.run(["papermill", "another_one.ipynb", "out.ipynb"])

    
    try:
        with open("output.txt", "r") as f:
            emotion = f.read().strip()
            all = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
            if emotion not in all:
                st.error("❌ Could not determine your mood. Please try again.")
            else:
                if emotion == 'happy':
                    st.balloons()
                    st.write("Oh my God! The mirror is blushing!")
                    audio_file_mp3 = open("audio\happy_audio.mp3", "rb")
                    audio_bytes_mp3 = audio_file_mp3.read()
                    st.audio(audio_bytes_mp3, format="audio/mpeg")
                
                elif emotion == 'sad':
                    st.snow()
                    st.warning("😢")
                    st.write("Don't be sad! Remember, there's some bastard still out there, pushing the door when the sign says 'pull'!")
                    audio_file_mp3 = open("audio\sad_audio.mp3", "rb")
                    audio_bytes_mp3 = audio_file_mp3.read()
                    st.audio(audio_bytes_mp3, format="audio/mpeg")
                
                elif emotion == 'angry':
                    st.warning("😡")
                    st.write("When you feel angry, it's important to take a deep breath and count till 10. Remember to throw a punch at 8! Noone expects that!")
                    audio_file_mp3 = open("audio\Angry_audio.mp3", "rb")
                    audio_bytes_mp3 = audio_file_mp3.read()
                    st.audio(audio_bytes_mp3, format="audio/mpeg")
                
                elif emotion == 'fear':
                    st.warning("😨")
                    st.write("Nah bro! This fear is overrated! Lose it for god's sake! Remember that you're not facing your mom after coming home late!")
                    audio_file_mp3 = open("audio\Fear_audio.mp3", "rb")
                    audio_bytes_mp3 = audio_file_mp3.read()
                    st.audio(audio_bytes_mp3, format="audio/mpeg")
                
                elif emotion == 'disgust':
                    st.warning("🤢")
                    st.write("Honestly Dude! Get your shit together! The most disgusting thing in this world are People!")
                    audio_file_mp3 = open("audio\disgust_audio.mp3", "rb")
                    audio_bytes_mp3 = audio_file_mp3.read()
                    st.audio(audio_bytes_mp3, format="audio/mpeg")
                
                elif emotion == 'surprise':
                    st.warning("😲")
                    st.write("Did Jesus come by and say 'Surprise Mother******'?")
                    audio_file_mp3 = open("audio\surprise_audio.mp3", "rb")
                    audio_bytes_mp3 = audio_file_mp3.read()
                    st.audio(audio_bytes_mp3, format="audio/mpeg")
                
                elif emotion == 'neutral':
                    st.write("I see US in Black and White!")
                
                else:
                    st.warning("😐")
        
        st.success(f"🧠 Your dominant emotion is: **{emotion.capitalize()}**")
    
    except FileNotFoundError:
        st.error("❌ Could not read output. Make sure the notebook ran successfully.")
    
    
    


 

