# 🌟 image_to_dream - *Dream Visualizer*

**Dream Visualizer** is a Streamlit-based web application that empowers **Indian students** to see themselves achieving their dream goals. By uploading a photo and specifying a dream (e.g., *"I want to be an astronaut"*), the app uses **GPT-4 Vision** and **DALL·E 3** to generate a visually stunning, emotionally resonant portrait grounded in Indian cultural context.

This tool is designed to **inspire and motivate** incoming college students by providing a **personalized, aspirational** vision of their future success.

---

## ✨ Features

- 📸 **Photo Upload**: Upload a JPG, JPEG, or PNG image of yourself.
- 💭 **Dream Goal Input**: Enter your dream (e.g., IAS officer, cricketer, startup founder).
- 🤖 **AI-Powered Visualization**:
  - Uses **GPT-4 Vision** to understand your image.
  - Uses **DALL·E 3** to generate a dream image grounded in Indian culture.
- 📅 **Downloadable Output**: Save the AI-generated image as a PNG.
- 🖥️ **User-Friendly Interface**: Clean layout built with Streamlit for both desktop and mobile use.

---

## 🧰 Prerequisites

Before setting up, ensure you have:

- Python ≥ 3.8  
- OpenAI API Key  
- Git (optional for cloning)  
- A code editor (VS Code / PyCharm etc.)  
- Internet connection (for APIs and package installation)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/NikhilDendeti/image_to_dream.git
cd image_to_dream
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Using pip:

```bash
pip install streamlit openai requests pillow python-dotenv
```

**OR** create a `requirements.txt`:

```text
streamlit==1.38.0
openai==1.42.0
requests==2.31.0
pillow==10.4.0
python-dotenv==1.0.1
```

Then install:

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
pip list
```

---

## 🔐 Configuration

1. **Create a `.env` file** in the root directory:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

2. **Add `.env` to `.gitignore`** to keep it secure:

```
.env
```

---

## 📱 Usage

### Run the App

```bash
streamlit run dream_visualizer.py
```

The app will open at [http://localhost:8501](http://localhost:8501)

### Interact with the App

1. Upload your photo (JPG/JPEG/PNG).
2. Enter your dream goal (e.g., "I want to be a doctor").
3. Click **"Generate Dream Image"**.
4. View the result and click **"Download Image"** to save as `dream_visualization.png`.

### Stop the Server

```bash
Ctrl + C
```

---

## 📁 File Structure

```
image_to_dream/
│
├── dream_visualizer.py     # Main Streamlit app
├── .env                    # Environment variable config
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## 🧹 Troubleshooting

- **"Please set the OPENAI_API_KEY" error**: Ensure `.env` exists and is correctly formatted.
- **Image Upload Fails**: Make sure the image is JPG/JPEG/PNG and not corrupted.
- **OpenAI API Errors**: Check your key, internet, and quota.
- **Streamlit Not Found**: Run `pip install streamlit`.
- **Image Not Displayed**: Confirm that OpenAI returns a valid URL and `requests.get()` is successful.

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/your-feature
```

3. Make your changes and commit:

```bash
git commit -m "Add your feature"
```

4. Push and create a Pull Request:

```bash
git push origin feature/your-feature
```

Please follow **PEP 8** guidelines and add helpful comments where needed.

---

## 🙏 Acknowledgments

- **Streamlit** – for the intuitive frontend framework  
- **OpenAI** – for GPT-4 Vision and DALL·E 3  
- **Pillow** – for image manipulation  
- **python-dotenv** – for secure environment variable management

---

## 🇮🇳 Built with ❤️ for Indian students to visualize their dreams and inspire their future.

