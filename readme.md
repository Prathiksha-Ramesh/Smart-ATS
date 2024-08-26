# Smart ATS

Smart ATS is a Streamlit-based application that helps users improve their resumes by analyzing them against job descriptions using an AI-powered Applicant Tracking System (ATS). The tool provides a JD match percentage, identifies missing keywords, and generates a profile summary, all tailored to tech-related fields like software engineering, data science, and big data engineering.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshot](#screenshot)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Overview

Smart ATS leverages Google's Generative AI to evaluate resumes based on a given job description. It offers insightful feedback to improve your resume's alignment with the job market's competitive demands, especially in the tech sector.

## Features

- **Resume Evaluation**: Upload your resume and get an in-depth analysis of how well it matches a given job description.
- **Keyword Analysis**: Identify missing keywords that are crucial for matching the job description.
- **Profile Summary**: Generate a concise profile summary based on the content of your resume and the job description.
- **Interactive Interface**: User-friendly interface for uploading resumes and pasting job descriptions.

## Screenshot

Here is a screenshot of the Smart ATS application:

![Smart ATS Screenshot](./Screenshot%202024-08-24%20104516.png)

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/smart-ats.git
    cd smart-ats
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a `.env` file in the root directory with the following content:

      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

    - Replace `your_google_api_key` with your actual Google API key.

## Usage

To run the application:

```bash
streamlit run app.py
```
## How It Works:

- **Enter Job Description**: Paste the job description into the provided text area.
- **Upload Resume**: Upload your resume in PDF format.
- **Submit**: Click the "submit" button to get the analysis.
- **View Results**: The app will display a detailed analysis of your resume against the job description.

## Project Structure

- `app.py`: Main application file that handles the Streamlit interface and core functionality.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `.env`: Environment variables file (not included in the repository; must be created by the user).
- `Screenshot 2024-08-24 104516.png`: Screenshot of the application interface.

## Dependencies

The project uses the following dependencies:

- `python-dotenv`: For managing environment variables.
- `streamlit`: For building the interactive user interface.
- `PyPDF2`: For extracting text from PDF files.
- `google-generativeai`: For generating summaries using Google's Generative AI.

For a full list of dependencies, please refer to the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
