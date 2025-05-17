# TalkToAnyone: A Conversational Graph-based Agent

This project allows you to have a conversation with **any person you want**, at **any age you specify**. Under the hood, it uses **LangGraph**, **LangChain** tools, and an LLM to simulate dynamic conversations.

## 📦 Project Structure

```
main.py
app/
├── config.py
├── graph.py
└── llm.py
.env
README.md
```

---

## 🚀 How It Works

1. **You input who you want to talk to, and at what age.**
2. The system parses the name and age.
3. Then, it simulates a conversation with that person, using the LLM.
4. Optionally, the LLM can call tools (like TavilySearch) to enrich the conversation.
5. The flow is orchestrated by LangGraph.

---

## 🛠️ Installation

1. Clone this repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Edit .env file with your API keys:
   ```
   mv .env.template .env
   # edit .env and add your api keys:
   LLM_API_KEY=your_deepseek_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## ▶️ Usage

Run the main script:

```
python main.py
```

You'll be prompted:

```
Who do you want to talk to, at what age?
```

For example:

```
Napoleon, 25
```

Then you can chat:

```
User: What do you think about modern warfare?
```

Type quit, exit, or q to end the conversation.

## 🧰 Dependencies

- LangGraph

- LangChain

- DeepSeek Chat API

- Tavily Search API

## ✅ Example

```
Who do you want to talk to, at what age? Napoleon at the age of 26
================================ Human Message =================================

Napoleon at the age of 26
================================== Ai Message ==================================

{"name": "Napoleon", "age": 26}
content='Ah, at 26 years old—what a time! I was already making my mark in the military, rising through the ranks with ambition and determination. Corsica was behind me, and France was my stage. What would you like to discuss? My early campaigns, my thoughts on leadership, or perhaps something more personal? Speak freely!' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 68, 'prompt_tokens': 1576, 'total_tokens': 1644, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 1576}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_8802369eaa_prod0425fp8', 'id': 'dd7eae46-3054-4242-923c-4895ff4d8fd5', 'service_tier': None, 'finish_reason': 'stop', 'logprobs': None} id='run--b15f3f35-9c9b-442d-9782-68060fc5a4af-0' usage_metadata={'input_tokens': 1576, 'output_tokens': 68, 'total_tokens': 1644, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}}
================================== Ai Message ==================================

Ah, at 26 years old—what a time! I was already making my mark in the military, rising through the ranks with ambition and determination. Corsica was behind me, and France was my stage. What would you like to discuss? My early campaigns, my thoughts on leadership, or perhaps something more personal? Speak freely!
User:
```
