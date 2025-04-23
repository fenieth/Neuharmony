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
    base_url="https://api.openai.com/v1",  # Ensure you're using the OpenAI API base URL
    api_key=AI_TOKEN,
)

YOUTUBE_LINKS = {
    "sensory_regulation": [
        {"description": "Бинауральная музыка для детей – глубокое расслабление", "link": "https://youtu.be/Fps2bqFV5nM"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/F5Tt3LoygCQ"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/vLEek3I3wac"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/sBOLxexuUSI"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/live/jDoblNn1qvs"},
        {"description": "Лёгкий дождь и пение птиц – звуки природы", "link": "https://www.youtube.com/watch?v=OdIJ2x3nxzQ"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/515an742WVg"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/eNUpTV9BGac"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/ipf7ifVSeDU"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/UyZfCrrdbm8"},
        {"description": "Ритмическая игра с хлопками и песенкой", "link": "https://youtu.be/WivrnJFPb-Q"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/watch?v=Cm926T-GwsU"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/jAd4pYDM1T8"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/watch?v=zDuxn61UeGk"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/watch?v=HXpZhiPPTls"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/vjm8iGIm-0Q"},
        {"description": "Энергичная музыка для вовлечения в движения", "link": "https://youtu.be/2pmkBsknKLw"},
        {"description": "Билатеральная координация через музыкальные указания", "link": "https://youtu.be/j24_xH5uvdA"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/watch?v=nJq3LynIo6U"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/watch?v=VMaJHzZ_CjU"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://www.youtube.com/watch?v=TR-ue9SSUmM"},
        {"description": "Метроном 60 BPM", "link": "https://youtu.be/IvUU8joBb1Q"},
        {"description": "Метроном 70 BPM", "link": "https://www.youtube.com/watch?v=wo-wr_tRkCw"},
        {"description": "Метроном 80 BPM", "link": "https://www.youtube.com/watch?v=SdTP5qQG8IY"},
        {"description": "Музыкальные игры 'Что изменилось?'", "link": "https://www.youtube.com/watch?v=IvUU8joBb1Q"},
        {"description": "Бинауральные биты", "link": "https://youtu.be/lkkGlVWvkLk"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/1ZYbU82GVz4"},
        {"description": "Музыка для сенсорной регуляции", "link": "https://youtu.be/ewgvSvm_EwQ"}
    ],
    "focus": [
        {"description": "Музыка для концентрации", "link": "https://youtu.be/3SMhJep65TI"},
        {"description": "Музыка для концентрации", "link": "https://youtu.be/S-RQFsxH4kI"}
    ],
    "emotional_development": [
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/iCEDfZgDPS8"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/F5V1jg9Hstk"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/WVYuKFGRFUY"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/l2bfx2vpWMo"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://www.youtube.com/watch?v=ZtIW2r1EalM"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://www.youtube.com/watch?v=c7O91GDWGPU"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/0WYUx79E9MQ"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/a8rNv7O3zOU"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/V2sWl5ow3rM"},
        {"description": "Музыка для эмоциональной регуляции", "link": "https://youtu.be/V7-2V0YnUZw"}
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
        age = user_data.get('age', '')
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
            "(Не используй markdown или специальное форматирование)"
        )

        completion = client.chat.completions.create(
            model="gpt-4",  # Updated model to GPT-4
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
            model="gpt-4",  # Updated model to GPT-4
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