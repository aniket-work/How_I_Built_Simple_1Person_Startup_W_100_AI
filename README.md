# How_I_Built_Simple_1Person_Startup_W_100_AI
🛡 How I Built Simple 1 Person Startup With 100% AI 🛡

## Introduction

This project demonstrates how AI enables one-person businesses, allowing anyone to become an entrepreneur or solopreneur. By leveraging AI tools, we can now handle complex tasks that previously required multiple experts. This README guides you through setting up and running an AI-powered e-commerce platform that uses AI for product classification and shipping logistics.

## What's This Project About?

This project is a practical implementation of a one-person startup powered entirely by AI. It includes:

1. A Streamlit-based frontend for an e-commerce website
2. A Flask backend server that communicates with an AI model
3. AI-powered product classification for shipping categories
4. A simple database system for storing product information

The project demonstrates how AI can automate tasks like product categorization, enabling efficient management of an e-commerce platform by a single person.

## Why Use This Project?

- Learn how to integrate AI into a real-world business application
- Understand the potential of AI in streamlining business operations
- Gain insights into building scalable, AI-powered web applications
- Explore how tasks typically requiring teams can be handled efficiently by AI

## Architecture

The project consists of the following components:

1. Frontend: Streamlit Web Application
2. Backend: Flask Web Server with RESTful API
3. Services: LLM Service for product classification, Database Service for data management
4. External Components: Groq API for LLM model access
5. Data Storage: JSON file (company_db.json)

**Prerequisites:**
- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

**Steps:**
1. **Virtual Environment Setup:**
   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv How_I_Built_Simple_1Person_Startup_W_100_AI
     ```
   - Activate the environment:
   
     - Windows:
       ```bash
       How_I_Built_Simple_1Person_Startup_W_100_AI\Scripts\activate
       ```
     - Unix/macOS:
       ```bash
       source How_I_Built_Simple_1Person_Startup_W_100_AI/bin/activate
       ```
2. **Install Project Dependencies:**

   - Navigate to your project directory and install required packages using `pip`:
   
     ```bash
     cd path/to/your/project
     pip install -r requirements.txt
     ```

3. **Setup Groq Key:**

   - Obtain your Groq API key from [Groq Console](https://console.groq.com/keys).
   - Set your key in the `.env` file as follows:
   
     ```plaintext
     GROQ_API_KEY=<YOUR_KEY>
     ```

4. **Run the Shipping Application**

   Finally, execute the following command to start the Drive-Through application:

   ```bash
   python server.py
   streamlit run web_site.py   
   ```
5. Launch UI at :  http://localhost:8501/
