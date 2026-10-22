# 🌍 CrewAI Travel Planner

An AI-powered destination recommender built with [CrewAI](https://github.com/crewAIInc/crewAI) and OpenAI. Users provide any destination or city name, and a specialized **Travel Guide & Planner Agent** generates the top three must-visit places, complete with descriptions and practical local travel tips.

---

## 📋 Features

- **Autonomous Agent**: Leverages a dedicated `Expert Travel Guide & Planner` role with a tailored backstory and mission.
- **Dynamic User Input**: Dynamically prompts for any city or destination from the terminal.
- **Structured Recommendations**: Provides exactly 3 curated spots with visitor tips (e.g., best times, entry details, local etiquette).
- **Clean Output**: Configured with suppressed internal logs and disabled telemetry prompts for a streamlined CLI experience.

---

## 🛠️ Tech Stack & Requirements

- **Python**: Version 3.10 to 3.12 recommended
- **CrewAI**: Core multi-agent orchestration framework
- **OpenAI API**: Powering the agent's LLM reasoning
- **python-dotenv**: For environment variable management

---

## 🚀 Getting Started

### 1. Clone or Download the Project

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Set Up a Virtual Environment

It is recommended to use an isolated Python environment:

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt / PowerShell)
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install crewai python-dotenv
```

### 4. Configure Your API Key

Create a `.env` file in the root directory of your project:

```bash
touch .env
```

Add your OpenAI API key into the `.env` file:

```env
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

---

## 💻 Usage

Run the main application script:

```bash
python main.py
```

### Example Interaction

```text
Which city? Bangalore

==================================================
TRAVEL SUGGESTIONS FOR BANGALORE:
==================================================
1. Lalbagh Botanical Garden
   - Why it's special: A historic 240-acre botanical garden featuring rare tropical plants and a Victorian glasshouse.
   - Visitor Tip: Visit early around 6:30 AM to beat the mid-day heat and witness morning walkers in peaceful greenery.

2. Bangalore Palace
   - Why it's special: Modeled after London’s Windsor Castle, featuring Tudor-style architecture, ornate wood carvings, and royal memorabilia.
   - Visitor Tip: Rent an audio guide at the entrance to fully appreciate the private history of the Wadiyar dynasty.

3. Cubbon Park & Vidhana Soudha
   - Why it's special: A sprawling green retreat located right next to the neo-Dravidian architecture of Karnataka’s state legislature.
   - Visitor Tip: Visit on Sunday mornings when vehicular traffic is restricted, making it ideal for walking and photography.
```

---

## ⚙️ Configuration Notes

- **Verbose Logs**: If you want to see the agent's internal thought process and steps, set `verbose=True` in both the `Agent` and `Crew` constructors.
- **Telemetry**: `os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"` is included in the script to suppress CrewAI's prompt asking to submit execution traces after every run.
