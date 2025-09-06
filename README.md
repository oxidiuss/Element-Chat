# ELEMENT AI CHAT

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

**ELEMENT AI CHAT** is a powerful terminal-based chatbot that provides access to various AI models through the OpenRouter API directly in your terminal.

---

## 🤖 Default models

| # | Model | API Endpoint | Description |
|---|-------|--------------|-------------|
| 1 | **Mistral** | `mistralai/devstral-small-2505:free` | Fast and efficient model |
| 2 | **DeepSeek** | `deepseek/deepseek-chat-v3.1:free` | Advanced reasoning capabilities |
| 3 | **Llama** | `meta-llama/llama-4-maverick:free` | Meta's powerful language model |
| 4 | **Qwen** | `qwen/qwen3-30b-a3b:free` | Alibaba's multilingual model |
| 5 | **ChatGPT** | `openai/gpt-oss-120b:free` | OpenAI's flagship model |
| 6 | **Google Gemma** | `google/gemma-3-27b-it:free` | Google's instruction-tuned model |

## 📋 Requirements

- Python 3.6+
- `requests` library
- OpenRouter API key
- Terminal with UTF-8 support (for proper display)

## 🚀 Installation

1. **Clone or download the script:**
   ```bash
   git clone https://github.com/oxidiuss/Element-Chat.git
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Get API key:**
   - Go to [OpenRouter](https://openrouter.ai/keys)
   - Register and create an API key
   - Copy the key for use

### Chatting with AI

1. Select a model (1-6)
2. Ask questions to the AI
3. Type `exit` to quit the chat

## 🔧 OpenRouter Settings

To use free models, you need to:

1. Go to [OpenRouter Privacy Settings](https://openrouter.ai/settings/privacy)
2. Enable **"Enable free endpoints that may publish prompts"**
3. Save settings

**Important**: Free models may publish your prompts for training purposes. Use paid models for sensitive conversations.

## 🆕 Version History

### v1.0 (Current)

## 🔗 Useful Links

- [OpenRouter API Documentation](https://openrouter.ai/docs)
- [Get OpenRouter API Key](https://openrouter.ai/keys)
- [OpenRouter Models List](https://openrouter.ai/models)
- [Privacy Settings](https://openrouter.ai/settings/privacy)

## 📄 License

MIT License - feel free to use for personal and commercial projects.

---
