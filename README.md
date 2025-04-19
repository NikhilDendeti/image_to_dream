Dream Visualizer
Dream Visualizer is a Streamlit-based web application that allows Indian students to visualize themselves achieving their dream goals. By uploading a photo and specifying a dream (e.g., "I want to be an astronaut"), the app uses OpenAI's GPT-4 Vision and DALL·E 3 to generate a visually striking, emotionally resonant portrait of the user having realized their dream, grounded in an Indian cultural context.
The app is designed to inspire incoming college students by providing a personalized, aspirational vision of their future success.
Features

Photo Upload: Upload a JPG, JPEG, or PNG image of yourself.
Dream Goal Input: Enter your dream goal (e.g., becoming an IAS officer, cricketer, or startup founder).
AI-Powered Visualization: Uses GPT-4 Vision to describe the uploaded image and DALL·E 3 to generate a high-quality, culturally authentic image of you achieving your dream.
Downloadable Output: Save the generated image as a PNG file.
User-Friendly Interface: Built with Streamlit for a simple, centered layout optimized for desktop and mobile.

Prerequisites
Before setting up the project, ensure you have the following:

Python: Version 3.8 or higher.
OpenAI API Key: Obtain an API key from OpenAI.
Git: For cloning the repository (optional).
Text Editor: VS Code, PyCharm, or any editor for managing the code.
Internet Connection: Required for API calls and dependency installation.

Installation
Follow these steps to set up the project locally:

Clone the Repository (or download the code):
git clone https://github.com//dream-visualizer.git
cd dream-visualizer


Create a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Install the required Python packages using the provided requirements.txt (or manually as listed below):
pip install streamlit openai requests pillow python-dotenv

Alternatively, create a requirements.txt with:
streamlit==1.38.0
openai==1.42.0
requests==2.31.0
pillow==10.4.0
python-dotenv==1.0.1


Verify Installation:Ensure all packages are installed by running:
pip list



Configuration
To use the OpenAI API, you need to set up an environment variable for the API key:

Create a .env File:In the project root directory, create a file named .env with the following content:
OPENAI_API_KEY=your-openai-api-key-here

Replace your-openai-api-key-here with your actual OpenAI API key.

Secure the .env File:Ensure the .env file is added to .gitignore to prevent it from being committed to version control:
.env



Usage
Run the Streamlit app and use it to generate your dream visualization:

Start the Streamlit Server:From the project directory, run:
streamlit run dream_visualizer.py

This will launch the app in your default web browser at http://localhost:8501.

Interact with the App:

Upload a Photo: Select a JPG, JPEG, or PNG image of yourself using the file uploader.
Enter Your Dream Goal: Type your dream (e.g., "I want to be a doctor") in the text input field.
Generate the Image: Click the "Generate Dream Image" button.
View and Download: The generated image will appear on the screen. Use the "Download Image" button to save it as dream_visualization.png.


Stop the Server:Press Ctrl+C in the terminal to stop the Streamlit server.


File Structure
dream-visualizer/
│
├── dream_visualizer.py  # Main Streamlit application script
├── .env                 # Environment variables (not committed)
├── requirements.txt     # Python dependencies (optional, create as needed)
├── .gitignore           # Git ignore file
└── README.md            # This file

Troubleshooting

Error: "Please set the OPENAI_API_KEY in the .env file":Ensure the .env file exists in the project root and contains a valid OPENAI_API_KEY.
Image Upload Fails:Verify the uploaded file is a valid JPG, JPEG, or PNG and is not corrupted.
API Errors:Check your OpenAI API key and ensure you have sufficient credits/quota. Verify your internet connection.
Streamlit Not Found:Run pip install streamlit in your virtual environment.
Generated Image Not Displaying:Ensure the OpenAI API response includes a valid image URL and that requests.get() succeeds (status code 200).

For additional help, check the Streamlit documentation or OpenAI API documentation.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request with a detailed description of your changes.

Please ensure your code follows PEP 8 style guidelines and includes appropriate comments.

Acknowledgments

Streamlit: For the intuitive web app framework.
OpenAI: For providing GPT-4 Vision and DALL·E 3 APIs.
Pillow: For image processing capabilities.
python-dotenv: For secure environment variable management.


Built with ❤️ for Indian students to visualize their dreams and inspire their future.
