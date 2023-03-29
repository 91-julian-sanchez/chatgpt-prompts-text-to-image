# Prompt Generator for Text-to-Image Models
This is a Python program that generates prompts for text-to-image models using OpenAI's GPT-3 API. It currently supports the Stable Diffusion, Midjourney, and Dalle2 models.

#  Installation
To use this program, you'll need to install the following Python packages:

- dotenv
- openai
- rich
- typer

You can install these packages using pip:
```bash
pip install -r requirements.txt
```

Next, create a `.env` file in the same directory as `main.py` and add your OpenAI API key:
```bash
CHATGPT_API_KEY=<your_api_key_here>
```

# Usage
To generate prompts, simply run the following command:

```bash
python main.py
```

The program will prompt you for input and generate prompts using OpenAI's GPT-3 API. You can choose to generate more prompts or exit the program.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue. We welcome contributions of all kinds, including bug reports, feature requests, and code changes.

## License
This project is licensed under the MIT License.
