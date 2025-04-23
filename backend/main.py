from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from openai import OpenAI
from config import AI_TOKEN
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import re
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

client = OpenAI(
    base_url="https://api.openai.com/v1",
    api_key=AI_TOKEN,
)

YOUTUBE_LINKS = {
    "sensory_regulation": [
        {"description": "Бинауральная музыка для детей – глубокое расслабление", "link": "https://youtu.be/Fps2bqFV5nM"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/F5Tt3LoygCQ"},
    ],
    "focus": [
        {"description": "Музыка для концентрации", "link": "https://youtu.be/3SMhJep65TI"},
        {"description": "Музыка для концентрации", "link": "https://youtu.be/S-RQFsxH4kI"}
    ],
    "emotional_development": [
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/iCEDfZgDPS8"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/F5V1jg9Hstk"},
    ]
}

class UserData(BaseModel):
    age: str
    diagnosis: str
    features: List[str]
    difficulties: List[str]
    goals: List[str]
    time: str
    piano: str

class ChatQuestion(BaseModel):
    question: str
    context: Optional[str] = None

def clean_formatting(text):
    return re.sub(r'(\*\*|\*|__|_|~~|`|#+)', '', text)

def get_random_youtube_links(category: str, count: int = 2) -> List[dict]:
    """Get random YouTube links from a specific category"""
    if category not in YOUTUBE_LINKS:
        return []
    
    links = YOUTUBE_LINKS[category]
    return random.sample(links, min(count, len(links)))

@app.get("/")
async def root():
    return {"message": "Neuharmony API is running!"}

async def generate_therapy_response(user_data):
    try:
        age_raw = user_data.get('age', '')
        match = re.search(r'\d+', age_raw)
        age = int(match.group()) if match else 0
        diagnosis = user_data.get('diagnosis', '')
        features = user_data.get('features', [])
        difficulties = user_data.get('difficulties', [])
        goals = user_data.get('goals', [])
        frequency = user_data.get('time', '')
        has_piano = user_data.get('piano', '') == 'Да'

        youtube_links_section = ""
        if any("сенсор" in goal.lower() for goal in goals):
            links = get_random_youtube_links("sensory_regulation", 2)
            youtube_links_section = "\n\nСсылки для сенсорной регуляции:\n" + "\n".join(
                [f"- {link['description']}: {link['link']}" for link in links]
            )
        
        if any("концентр" in goal.lower() or "вниман" in goal.lower() for goal in goals):
            links = get_random_youtube_links("focus", 2)
            youtube_links_section += "\n\nСсылки для концентрации внимания:\n" + "\n".join(
                [f"- {link['description']}: {link['link']}" for link in links]
            )
        
        if any("эмоц" in goal.lower() for goal in goals):
            links = get_random_youtube_links("emotional_development", 2)
            youtube_links_section += "\n\nСсылки для эмоционального развития:\n" + "\n".join(
                [f"- {link['description']}: {link['link']}" for link in links]
            )

        motor_skills_section = ""
        if age and int(age) >= 8 and "Развитие моторики" in goals:
            motor_skills_section = (
                "\n\nАвтоматические команды по моторике:\n"
                "- Арифметические карточки с цветными нотами (тренировка моторной памяти и счёта)\n"
                "- Цветные песни для чтения и игры (отработка моторики через зрительно-аудиальное восприятие)\n\n"
                "Обязательные ссылки:\n"
                "- Онлайн-пианино: https://toytheater.com/piano-c-major/\n"
                "- Документы и карточки: https://drive.google.com/drive/folders/1gC0l3il0mfkWF4NB1L-io9iFP-dFcKvD?usp=sharing\n\n"
                "Уточнение по инструменту: Если у родителя нет пианино, предложи использовать онлайн-пианино по ссылке выше. Объясни, что даже базовые упражнения возможны без физического инструмента.\n\n"
                "Инструкции:\n"
                "- Арифметические карточки: соединяйте 3–4 цветные ноты в простые комбинации. Повторяйте, пока движения не станут автоматическими.\n"
                "- Цветные песни: выбирайте по одной песне в неделю, играйте с родительской помощью, опираясь на цветовую схему.\n\n"
                "Встраивание в план: Добавляйте эти задания во 2–4 недели плана, в зависимости от частоты занятий и готовности ребёнка."
            )

        prompt = (
            "Ты эксперт по музыкальной терапии для детей с РАС. Создай индивидуальный план:\n\n"
            f"1. Возраст: Адаптируй план под ребёнка {age} лет с учётом речевых, моторных и поведенческих особенностей возраста.\n"
            f"2. Диагноз: У ребёнка {diagnosis.lower()}. {'При подозрении — адаптируй как при лёгкой форме аутизма.' if 'подозрение' in diagnosis else ''}\n"
            f"3. Особенности: Учитывай: {', '.join(features)}.\n"
            f"4. Поведение: Учти трудности: {', '.join(difficulties)}.\n"
            f"5. Цель: Цель терапии: {', '.join(goals)}.\n"
            f"6. Частота: Разработай программу с частотой {frequency} занятия(ий) в неделю с учётом повторения и усложнения.\n"
            f"7. Инструменты: {'Используй фортепиано/синтезатор.' if has_piano else 'Используй альтернативы: телесный ритм, голос, метроном, настольные клавиши.'}\n\n"
            "Дополнительные указания:\n"
            "- Создай 6-недельный план с постепенным усложнением\n"
            "- Включи 2-3 уровня сложности для каждого упражнения\n"
            "- Добавь подходящие YouTube-ссылки на музыкальные примеры (уже предоставлены ниже)\n"
            "- Предоставь чёткие инструкции для родителей\n"
            "- Учитывай сенсорные особенности ребёнка\n\n"
            "Формат вывода:\n"
            "1. Краткое описание плана (3-4 предложения)\n"
            "2. Недельные блоки с упражнениями\n"
            "3. Рекомендации для родителей\n"
            "4. Ссылки на музыкальные материалы (используй только те, что предоставлены ниже)\n\n"
            "Предоставленные YouTube ссылки:\n"
            f"{youtube_links_section}\n\n"
            f"{motor_skills_section}\n\n"
            "(Не используй markdown или специальное форматирование)"
        )

        completion = client.chat.completions.create(
            model="gpt-4",  
            messages=[{"role": "system", "content": "Ты эксперт по музыкальной терапии для детей с РАС."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500
        )

        raw_text = completion.choices[0].message.content
        cleaned_text = clean_formatting(raw_text)
        return cleaned_text

    except Exception as e:
        return f"⚠️ Ошибка генерации плана: {str(e)}"

async def generate_chat_response(question: str, context: str = None):
    try:
        prompt = (
            "Ты эксперт по музыкальной терапии для детей с РАС. "
            "Ответь на вопрос пациента/родителя на основе твоего профессионального опыта."
            f"\n\nКонтекст (если есть):\n{context}\n\n"
            f"Вопрос: {question}\n\n"
            "Ответь подробно и профессионально, но простым языком. "
            "Если вопрос не связан с музыкальной терапией, вежливо укажи на это."
        )

        completion = client.chat.completions.create(
            model="gpt-4",  
            messages=[{"role": "system", "content": "Ты эксперт по музыкальной терапии для детей с РАС."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )

        raw_text = completion.choices[0].message.content
        cleaned_text = clean_formatting(raw_text)
        return cleaned_text

    except Exception as e:
        return f"⚠️ Ошибка при обработке вопроса: {str(e)}"

@app.post("/therapy")
async def create_therapy_plan(user_data: UserData):
    try:
        plan = await generate_therapy_response(user_data.dict())
        return {"plan": plan}
    except Exception as e:
        return {"error": f"Ошибка при генерации плана: {str(e)}"}

@app.post("/therapy/chat")
async def handle_chat_question(chat_data: ChatQuestion):
    try:
        response = await generate_chat_response(
            question=chat_data.question,
            context=chat_data.context
        )
        return {"response": response}
    except Exception as e:
        return {"error": f"Ошибка при обработке вопроса: {str(e)}"}

@app.post("/therapy-form/")
async def get_plan_form(
    name: str = Form(...),
    age: str = Form(...),
    sensory: str = Form(...),
    sleep: str = Form(...),
    genre: str = Form(...),
    active: str = Form(...),
):
    user_data = {
        "name": name,
        "age": age,
        "sensory": sensory,
        "sleep": sleep,
        "genre": genre,
        "active": active
    }
    response = await generate_therapy_response(user_data)
    return {"response": response}

@app.options("/therapy")
async def handle_options():
    return {}

@app.options("/therapy-form/") 
async def handle_options_form():
    return {}

@app.options("/therapy/chat")
async def handle_options_chat():
    return {}