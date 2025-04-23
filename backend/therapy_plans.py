def clean_youtube_url(url: str) -> str:
    """Clean YouTube URL to standard format"""
    if not url:
        return ""
    if 'youtu.be' in url:
        return url.split('?')[0]  
    elif 'youtube.com' in url:
        return url.split('&')[0]  
    return url

YOUTUBE_LINKS = {
    "sensory_regulation": [
        {"description": "Бинауральная музыка для детей – глубокое расслабление", "link": clean_youtube_url("https://youtu.be/Fps2bqFV5nM")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/F5Tt3LoygCQ")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/vLEek3I3wac")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/sBOLxexuUSI")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/live/jDoblNn1qvs")},
        {"description": "Лёгкий дождь и пение птиц – звуки природы", "link": clean_youtube_url("https://www.youtube.com/watch?v=OdIJ2x3nxzQ")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/515an742WVg")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/eNUpTV9BGac")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/ipf7ifVSeDU")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/UyZfCrrdbm8")},
        {"description": "Ритмическая игра с хлопками и песенкой", "link": clean_youtube_url("https://youtu.be/WivrnJFPb-Q")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=Cm926T-GwsU")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/jAd4pYDM1T8")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=zDuxn61UeGk")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=HXpZhiPPTls")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/vjm8iGIm-0Q")},
        {"description": "Энергичная музыка для вовлечения в движения", "link": clean_youtube_url("https://youtu.be/2pmkBsknKLw")},
        {"description": "Билатеральная координация через музыкальные указания", "link": clean_youtube_url("https://youtu.be/j24_xH5uvdA")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=nJq3LynIo6U")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=VMaJHzZ_CjU")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=TR-ue9SSUmM")},
        {"description": "Метроном 60 BPM", "link": clean_youtube_url("https://youtu.be/IvUU8joBb1Q")},
        {"description": "Метроном 70 BPM", "link": clean_youtube_url("https://www.youtube.com/watch?v=wo-wr_tRkCw")},
        {"description": "Метроном 80 BPM", "link": clean_youtube_url("https://www.youtube.com/watch?v=SdTP5qQG8IY")},
        {"description": "Музыкальные игры 'Что изменилось?'", "link": clean_youtube_url("https://www.youtube.com/watch?v=IvUU8joBb1Q")},
        {"description": "Бинауральные биты", "link": clean_youtube_url("https://youtu.be/lkkGlVWvkLk")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/1ZYbU82GVz4")},
        {"description": "Музыка для сенсорной регуляции", "link": clean_youtube_url("https://youtu.be/ewgvSvm_EwQ")}
    ],
    "focus": [
        {"description": "Музыка для концентрации", "link": clean_youtube_url("https://youtu.be/3SMhJep65TI")},
        {"description": "Музыка для концентрации", "link": clean_youtube_url("https://youtu.be/S-RQFsxH4kI")}
    ],
    "emotional_development": [
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/iCEDfZgDPS8")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/F5V1jg9Hstk")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/WVYuKFGRFUY")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/l2bfx2vpWMo")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=ZtIW2r1EalM")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://www.youtube.com/watch?v=c7O91GDWGPU")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/0WYUx79E9MQ")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/a8rNv7O3zOU")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/V2sWl5ow3rM")},
        {"description": "Музыка для эмоциональной регуляции", "link": clean_youtube_url("https://youtu.be/V7-2V0YnUZw")}
    ]
}

THERAPY_PLANS = {
    "sensory_regulation": {
        "title": "Сенсорная регуляция через музыку",
        "description": "План направлен на снижение сенсорной перегрузки и улучшение саморегуляции",
        "weeks": {
            1: {
                "goal": "Sensory Regulation",
                "activities": [
                    "Аудиопауза с бинауральными ритмами (15–20 минут)",
                    "Дыхание под музыку методом 4–4–4"
                ],
                "parent_instructions": [
                    "Организуйте 2 сенсорных музыкальных перерыва в день",
                    "Используйте бинауральную музыку с массажем или растяжкой",
                    "Адаптируйте продолжительность при перевозбуждении"
                ],
                "music_types": [
                    "Бинауральные ритмы для детей",
                    "Естественные звуки природы"
                ],
                "youtube_links": YOUTUBE_LINKS["sensory_regulation"],
                "resources": [
                    "https://www.frontiersin.org/articles/10.3389/fnint.2024.1403876"
                ],
                "adaptations": {
                    "2-4": "5 минут естественных звуков без наушников",
                    "5-8": "Добавить дыхательные игры с визуальными подсказками",
                    "sensitive": "Только природные звуки, низкая громкость",
                    "active": "Добавить качающие движения"
                }
            }
        },
        "facts": [
            "Бинауральные ритмы помогают синхронизировать работу полушарий мозга",
            "Регулярные сенсорные паузы снижают частоту эмоциональных вспышек"
        ]
    },
    "motor_skills": {
        "title": "Развитие моторных навыков через ритм",
        "description": "Программа улучшает координацию и мелкую моторику с помощью музыкальных игр",
        "weeks": {
            1: {
                "goal": "Motor Skills",
                "activities": [
                    "Ритмичная игра телом с музыкой (10–15 минут)",
                    "Пальчиковая разминка под музыку"
                ],
                "parent_instructions": [
                    "2 занятия в день по 15-20 минут",
                    "Используйте любимую музыку ребёнка с чётким ритмом",
                    "Физически помогайте при сложностях с движениями"
                ],
                "music_types": [
                    "Ритмические игры",
                    "Танцевальные инструкции"
                ],
                "youtube_links": [
                    {"description": "Ритмическая игра с хлопками и песенкой", "link": "https://youtu.be/WivrnJFPb-Q"},
                    {"description": "Музыка для моторных навыков", "link": "https://youtu.be/jAd4pYDM1T8"},
                    {"description": "Энергичная музыка для вовлечения в движения", "link": "https://youtu.be/2pmkBsknKLw"},
                    {"description": "Билатеральная координация через музыкальные указания", "link": "https://youtu.be/j24_xH5uvdA"}
                ],
                "resources": [
                    "https://www.mdpi.com/2227-9067/12/3/335"
                ],
                "adaptations": {
                    "2-4": "Простые движения 5-10 минут",
                    "5-8": "Сложные ритмы и инструменты",
                    "sensitive": "Мягкий спокойный ритм",
                    "active": "Энергичная музыка с танцами"
                }
            }
        },
        "facts": [
            "Ритмичные движения улучшают билатеральную координацию",
            "Музыкальные игры развивают моторное планирование"
        ]
    },
    "focus": {
        "title": "Улучшение концентрации внимания",
        "description": "Музыкальные техники для развития устойчивого внимания",
        "weeks": {
            1: {
                "goal": "Focus",
                "activities": [
                    "Ритмичные движения с метрономом",
                    "Игра 'Что изменилось?' (адаптивная версия)",
                    "Концентрация через пазлы с фоновой музыкой"
                ],
                "parent_instructions": [
                    "Используйте чёткий ритм (60-80 BPM)",
                    "Для невербальных детей применяйте визуальные подсказки",
                    "Разбивайте задания на короткие этапы"
                ],
                "music_types": [
                    "Метроном для концентрации",
                    "Расслабляющее фортепиано"
                ],
                "youtube_links": YOUTUBE_LINKS["focus"],
                "resources": [
                    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9100336/"
                ],
                "adaptations": {
                    "2-4": "Одно простое упражнение 5-7 минут",
                    "5-8": "Сложные различия в музыке + таймер",
                    "nonverbal": "Карточки/планшет вместо вопросов",
                    "hyperactive": "Короткие активные микроблоки"
                }
            }
        },
        "facts": [
            "Метроном помогает синхронизировать движения и внимание",
            "Музыкальные различия развивают слуховую память"
        ]
    },
    "emotional_development": {
        "title": "Эмоциональное развитие через музыку",
        "description": "Программа помогает распознавать и выражать эмоции",
        "weeks": {
            1: {
                "goal": "Emotional Recognition",
                "activities": [
                    "Музыкальные эмоции с карточками",
                    "Музыкальные истории",
                    "Релаксационные упражнения"
                ],
                "parent_instructions": [
                    "15-20 минут ежедневных занятий",
                    "Используйте визуальные подсказки для эмоций",
                    "Адаптируйте громкость для чувствительных детей"
                ],
                "music_types": [
                    "Классические эмоциональные отрывки",
                    "Релаксационные композиции"
                ],
                "youtube_links": YOUTUBE_LINKS["emotional_development"],
                "resources": [
                    "https://www.mdpi.com/2076-3425/12/6/704",
                    "https://pubmed.ncbi.nlm.nih.gov/34329821/"
                ],
                "adaptations": {
                    "2-4": "Короткие отрывки до 10 минут",
                    "5-8": "Сложные истории с обсуждением",
                    "nonverbal": "Жесты/карточки вместо речи",
                    "sensitive": "Только спокойные композиции"
                }
            }
        },
        "facts": [
            "Музыка активирует те же нейронные пути, что и эмоции",
            "Регулярные занятия улучшают эмоциональный интеллект"
        ]
    }
}

def select_plan(user_data):
    primary_goal = user_data.get('goals', [])[0].lower() if user_data.get('goals') else None
    
    plan_mapping = {
        'сенсорная регуляция': 'sensory_regulation',
        'развитие мелкой моторики': 'motor_skills',
        'концентрация': 'focus',
        'эмоциональное развитие': 'emotional_development'
    }
    
    for goal, plan_key in plan_mapping.items():
        if goal in primary_goal:
            return THERAPY_PLANS[plan_key]
    
    return THERAPY_PLANS['sensory_regulation']