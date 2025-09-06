import requests
import json
import re
import time
import sys
import os

API_URL = "https://openrouter.ai/api/v1/chat/completions"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
API_KEY_FILE = os.path.join(SCRIPT_DIR, "api_key.txt")
GREEN = "\033[32m"  
WHITE = "\033[37m"  
RESET = "\033[0m"
BOLD = "\033[1m"   

MODELS = {
    "1": "mistralai/devstral-small-2505:free",
    "2": "deepseek/deepseek-chat-v3.1:free",
    "3": "meta-llama/llama-4-maverick:free",
    "4": "qwen/qwen3-30b-a3b:free",
    "5": "openai/gpt-oss-120b:free",
    "6": "google/gemma-3-27b-it:free",
}

def format_text(text):
    """Format markdown-style text for terminal display"""
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        if line.strip().startswith('###'):
            header_text = line.strip()[3:].strip()
            formatted_lines.append(f"    {BOLD}{header_text}{RESET}{WHITE}")
        elif line.strip().startswith('##'):
            header_text = line.strip()[2:].strip()
            formatted_lines.append(f"  {BOLD}{header_text}{RESET}{WHITE}")
        elif line.strip().startswith('#'):
            header_text = line.strip()[1:].strip()
            formatted_lines.append(f"{BOLD}{header_text}{RESET}{WHITE}")
        else:
            formatted_line = line
            formatted_line = re.sub(r'\*\*(.*?)\*\*', f'{BOLD}\\1{RESET}{WHITE}', formatted_line)
            formatted_line = re.sub(r'\*(.*?)\*', f'{BOLD}\\1{RESET}{WHITE}', formatted_line)
            formatted_lines.append(formatted_line)
    
    return '\n'.join(formatted_lines)

def load_api_key():
    """Load API key from file"""
    try:
        if os.path.exists(API_KEY_FILE):
            with open(API_KEY_FILE, 'r', encoding='utf-8') as f:
                api_key = f.read().strip()
                if api_key:
                    return api_key
        return None
    except Exception as e:
        print(f"{WHITE}Error reading API key file: {e}{RESET}")
        return None

def save_api_key(api_key):
    """Save API key to file"""
    try:
        with open(API_KEY_FILE, 'w', encoding='utf-8') as f:
            f.write(api_key)
        print(f"{GREEN}API key successfully saved to file {API_KEY_FILE}{RESET}")
        return True
    except Exception as e:
        print(f"{WHITE}Error saving API key: {e}{RESET}")
        return False

def request_api_key():
    """Request API key from user"""
    print(f"{GREEN}")
    print("╭─────────────────────────────────────────────────────────────╮")
    print("│                    FIRST RUN                                │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│  OpenRouter API key is required to work with neural networks│")
    print("│                                                             │")
    print("│  Get your key at: https://openrouter.ai/keys                │")
    print("│                                                             │")
    print("│  Key will be saved to api_key.txt in script folder         │")
    print("╰─────────────────────────────────────────────────────────────╯")
    print(f"{RESET}")
    
    while True:
        api_key = input(f"{GREEN}Enter your OpenRouter API key: {RESET}").strip()
        
        if not api_key:
            print(f"{WHITE}API key cannot be empty. Please try again.{RESET}")
            continue
            
        if len(api_key) < 10:
            print(f"{WHITE}API key is too short. Please check your input.{RESET}")
            continue
            
        if not api_key.startswith(('sk-or-', 'sk-')):
            print(f"{WHITE}Warning: API key should start with 'sk-or-' or 'sk-'{RESET}")
            confirm = input(f"{GREEN}Continue with this key? (y/n): {RESET}").lower()
            if confirm not in ['y', 'yes']:
                continue
        
        if save_api_key(api_key):
            return api_key
        else:
            print(f"{WHITE}Failed to save API key. Please try again.{RESET}")

def typewriter_effect(text, delay=0.01):
    """Typewriter effect for text output"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_menu():
    print(f"{GREEN}")
    print("    _______        _______ _______ _______ _    _ _______")
    print("    |______ |      |______ |  |  | |______ | \\  |    |   ")
    print("    |______ |_____ |______ |  |  | |______ |  \\_|    |   ")
    print(f"{RESET}")
    print(f"{GREEN}")
    print("  1.0")
    print(" ╭─────────────────────────────╮  ╭───────────────────────────╮")
    print(" │  Choose AI for chating:     │  │       Other options:      │")
    print(" ├─────────────────────────────┤  ├───────────────────────────┤")
    print(" │   [1] Mistral               │  │   [8] What's new?         │")
    print(" │                             │  │                           │")
    print(" │   [2] DeepSeek              │  │   [9] About               │")
    print(" │                             │  ╰───────────────────────────╯")
    print(" │   [3] Llama                 │  ╭───────────────────────────╮")
    print(" │                             │  │  Powered by Grok 3        │")
    print(" │   [4] Qwen                  │  │  and Claude Sonnet 4      │")
    print(" │                             │  │                           │")
    print(" │   [5] ChatGPT               │  │  GitHub: HyenaGG          │")
    print(" │                             │  │                           │")   
    print(" │   [6] Google Gemma          │  │  For more information     │")   
    print(" │                             │  │  read REDAME.md           │")       
    print(" ╰─────────────────────────────╯  ╰───────────────────────────╯")               
    print(f"{RESET}")

def ask_neural_network(question, model, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 10000
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            if "choices" in response_data and len(response_data["choices"]) > 0:
                return response_data["choices"][0]["message"]["content"].strip()
            else:
                return "Error: Unexpected response format from the API."
        elif response.status_code == 404:
            error_data = response.json() if response.text else {}
            if "No endpoints found matching your data policy" in response.text:
                return "❌ Error in OpenRouter privacy settings:\n\nTo use the free models, you need to:\n1. Go to OpenRouter settings (https://openrouter.ai/settings/privacy)\n2. Enable the option 'Enable free endpoints that may publish prompts'\n3. Save the settings\n\nOr use the paid model."
            else:
                return f"Error 404: Model not found or not accessible"
        else:
            print(f"API issue: {response.status_code} - {response.text}")
            return f"API Error: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"
    except json.JSONDecodeError:
        return "Error: Invalid response format from the server."

def main():
    api_key = load_api_key()
    
    if api_key is None:
        api_key = request_api_key()
        if api_key is None:
            print(f"{WHITE}Failed to get API key. Terminating the script.{RESET}")
            return
    
    display_menu()
    
    while True:
        choice = input(f"{GREEN}Type number of model (1-9): {RESET}")
        if choice in MODELS:
            selected_model = MODELS[choice]
            model_name = {
                "1": "Mistral",
                "2": "DeepSeek",
                "3": "Llama",
                "4": "Qwen",
                "5": "ChatGPT",
                "6": "Google Gemma",
                
            }[choice]
            break
        elif choice == "8":
            print(f"{WHITE}1.0 - release\n\n1.1 - replace models and better chat{RESET}")
            continue
        elif choice == "9":
            print(f"""{WHITE}
   The ELEMENT CHAT script provides the ability to communicate directly in your terminal! 
   New neural networks and other features for the application will be added in the near future.

   NAME                                 CODE NAME    
                              
   Mistral                              mistralai/devstral-small-2505:free    
   DeepSeek                             deepseek/deepseek-chat-v3.1:free                            
   Llama                                meta-llama/llama-4-maverick:free               
   Qwen                                 qwen/qwen3-30b-a3b:free                                   
   ChatGPT                              openai/gpt-oss-120b:free
   Google Gemma                         google/gemma-3-27b-it:free{RESET}
            """)
            continue
        else:
            print(f"{WHITE}Choose a number from 1 to 6: {RESET}")

    if choice in MODELS:
        print(f"{WHITE}Model: {model_name}{RESET}")
        while True:
            user_input = input(f"{GREEN}Ask question to {model_name}: {RESET}")
            if user_input.lower() in ["exit", "quit"]:
                break
            if not user_input.strip():
                print(f"{WHITE}Please, type your question.{RESET}")
                continue
            
            answer = ask_neural_network(user_input, selected_model, api_key)
            formatted_answer = format_text(answer)
            print(f"{GREEN}Answer {model_name}: {WHITE}", end="")
            typewriter_effect(formatted_answer)
            print(f"{RESET}", end="")

if __name__ == "__main__":
    main()
