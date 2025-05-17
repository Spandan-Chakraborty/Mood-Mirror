# Mood Mirror: A Certified Mood Analyzer ✨

**Mood Mirror** is a quirky and fun Streamlit-based web application that uses **DeepFace** (a facial analysis framework) to detect your mood from a selfie. It then plays a funny audio message and shows a meme to either match your vibe or cheer you up!

---

## Features

* **Upload your selfie and get your mood analyzed**
* **Enjoy personalized audio messages based on your detected emotion**
* **Random memes to lighten your day**
* **Intuitive and clean UI made with Streamlit**
* **Backend powered by DeepFace, using deep learning for accurate emotion recognition**

---

## How it Works

1.  **You upload a selfie.**
2.  The app saves the image and passes it to a **Jupyter Notebook** using **papermill**.
3.  The Notebook uses **DeepFace** to analyze the emotion in your image.
4.  The result is stored in a text file which is read back in the Streamlit app.
5.  Based on the detected emotion, a relevant audio file is played and a custom message is displayed.
6.  I recommend using a virtual environment for this, as it works better for the likes of tensorflow.

---

## Technologies Used

* **Streamlit:** For building the interactive frontend.
* **DeepFace:** For facial emotion recognition.
* **Python and Papermill:** For notebook automation.
* **PIL:** For image processing.

---

## Setup Instructions

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/yourusername/mood-mirror.git](https://github.com/yourusername/mood-mirror.git)
    cd mood-mirror
    ```

2.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    Make sure you also have **Jupyter Notebook** installed for papermill to work.

    ```bash
    pip install notebook papermill deepface streamlit
    ```

3.  **Folder Structure**

    ```
    ├── main.py             # Streamlit app file
    ├── another_one.ipynb   # DeepFace analysis notebook
    ├── audio/              # Folder with audio files for each emotion
    ├── memes/image/        # Folder with meme images
    ├── uploaded_image.jpg  # Uploaded selfie gets saved here
    ├── input_path.txt      # Temp file to pass path to notebook
    ├── output.txt          # Result written from notebook
    ```

---

## Run the App

```bash
streamlit run main.py
```

## Example Emotions

Happy: Balloons, upbeat audio, and a compliment!
Sad: Snow effect and comforting words.
Angry: Hilarious anger-control tips.
Fear, Disgust, Surprise, Neutral: Each comes with unique messages and vibes.

## Notes
The emotion detection is powered by DeepFace.analyze() using custom backend and alignment settings.
Papermill lets us run the notebook in the background and grab the output seamlessly.

## License
MIT License

# Created with joy and some sass by Spandan!





