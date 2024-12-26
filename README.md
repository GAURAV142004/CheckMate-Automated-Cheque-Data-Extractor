# CheckMate-Automated-Cheque-Data-Extractor
Description

CheckMate is a Python-based project designed to simplify the process of cheque data extraction and management. With advanced features such as authentication and automated data extraction, it provides a streamlined solution for handling cheque-related tasks efficiently and securely.

Features

Cheque Data Extraction: Automatically extract data from scanned cheque images.

User Authentication: Secure access to ensure data privacy.

Centralized Management: Combines multiple functionalities in a unified system.

Technologies Used

Python: Core programming language.

Environment Variables: Managed using a .env file.

Dependencies: Managed through requirements.txt.

Installation

Follow these steps to set up and run the project locally:

Clone the Repository:

git clone https://github.com/your-username/CheckMate-Cheque-Processor.git
cd CheckMate-Cheque-Processor

Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the root directory.

Add the required variables as specified below.

Usage

Run the main script to start the application:

python main.py

Use the homepage.py to interact with the UI or system features.

Follow the authentication process to access secured functionalities.

Environment Variables

Ensure the following variables are configured in your .env file:

SECRET_KEY: Your application's secret key.

DB_CONNECTION: Database connection string (if applicable).
