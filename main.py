from dotenv import load_dotenv
import os
import openai
from rich import print
import typer

load_dotenv()  # take environment variables from .env.

def generate_prompt():
    """
    Generates a prompt for text-to-image models using OpenAI's GPT-3 API.

    Returns:
        None
    """
    print("[bold blue]Generating prompts...[/bold blue]")
    # Context for the chat assistant
    assistant_context = {"role": "system", "content": "You are an expert in Prompt Engineering, specialized in generating prompts for text-to-image models (Stable Diffusion, Midjourney, or Dalle2)"}
    messages = [assistant_context]

    # Example prompt to get started
    user_prompt = __example_prompt()
    messages.append({"role": "user", "content": user_prompt})

    # Generate the response from the chat assistant
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response_content = response.choices[0].message.content

    # Print the response to the console
    print(f"[bold green]\nprompts > [/bold green]")
    print(response_content)

    # Ask if the user wants to generate more prompts
    more_prompts = typer.confirm("\nDo you want to generate more prompts?")
    if more_prompts:
        generate_prompt()
    else:
        print("Prompt generation complete.")

def __example_prompt() -> str:
    return """Examples of high quality prompt for stunning close-up photorealistic illustration of Ana de Armas for text-to-image models (Stable Diffusion, midjourney or Dalle2) are

    - portrait of beautiful happy young ana de armas, ethereal, realistic anime, trending on pixiv, detailed, clean lines, sharp lines, crisp lines, award winning illustration, masterpiece, 4k, eugene de blaas and ross tran, vibrant color scheme, intricately detailed

    -  alberto seveso and geo2099 style, A highly detailed and hyper realistic portrait of a gorgeous young ana de armas, lisa frank, trending on artstation, butterflies, floral, sharp focus, studio photo, intricate details, highly detailed, by Tvera and wlop and artgerm

    Give me more examples."""

if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")
    print("[bold green]Prompt generator for text-to-image models[/bold green]")
    print("[bold white]Close-up illustration (BETA)[/bold white]")
    generate_prompt()