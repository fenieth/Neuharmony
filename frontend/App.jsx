import React, { useState } from 'react';
import './styles.css';

const questions = [
  { key: 'age', label: 'Сколько лет вашему ребёнку?', options: ['2–3 года', '4–5 лет', '6–7 лет', '8–9 лет', '10+'] },
  { key: 'diagnosis', label: 'Подтверждён ли у ребёнка диагноз аутизма?', options: ['Да', 'Нет, но есть подозрение', 'Нет'] },
  { key: 'features', label: 'У ребёнка также присутствуют следующие особенности:', options: ['Сенсорная чувствительность', 'Нарушения мелкой моторики', 'Проблемы с концентрацией', 'Эмоциональные вспышки / тревожность'], multiple: true },
  { key: 'difficulties', label: 'Какие основные трудности вы замечаете у ребёнка?', options: ['Не может долго концентрироваться', 'Избегает определённых звуков / текстур', 'Не может удерживать внимание на заданиях', 'Плохо реагирует на инструкции', 'Сложности с координацией движений', 'Часто тревожится, неусидчив', 'Ему трудно выражать эмоции'], multiple: true },
  { key: 'goal', label: 'Какие цели вы ставите для занятий?', options: ['Улучшение сенсорной регуляции', 'Развитие мелкой моторики и координации', 'Повышение концентрации внимания', 'Помочь ребёнку лучше распознавать и выражать эмоции', 'Расширение музыкального кругозора', 'Просто удовольствие и отдых'] },
  { key: 'frequency', label: 'Сколько времени вы готовы уделять музыкальной терапии в неделю?', options: ['1 раз в неделю', '2 раза в неделю', '3 раза в неделю', 'Хочу сам(а) определить'] },
  { key: 'instrument', label: 'Есть ли у вас дома фортепиано или синтезатор?', options: ['Да', 'Нет, но есть доступ к онлайн-пианино'] }
];

export default function App() {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState({ name: 'Родитель' });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const current = questions[step];

  const handleChange = (option) => {
    if (current.multiple) {
      const selected = answers[current.key] || [];
      const updated = selected.includes(option)
        ? selected.filter(o => o !== option)
        : [...selected, option];
      setAnswers({ ...answers, [current.key]: updated });
    } else {
      setAnswers({ ...answers, [current.key]: option });
    }
  };

  const handleNext = async () => {
    if (step < questions.length - 1) {
      setStep(step + 1);
    } else {
      setLoading(true);
      try {
        const response = await fetch('http://localhost:8000/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(answers)
        });
        const data = await response.text();
        setResult(data);
      } catch (e) {
        setResult('Произошла ошибка при получении плана.');
      } finally {
        setLoading(false);
      }
    }
  };

  if (loading) return <div className="container"><h2>⏳ Генерируем план...</h2></div>;
  if (result) return <div className="container result"><h2>🎵 Индивидуальный план</h2><p>{result}</p></div>;

  return (
    <div className="container">
      <h2>{current.label}</h2>
      <div className="options">
        {current.options.map(option => (
          <button
            key={option}
            className={
              current.multiple
                ? (answers[current.key]?.includes(option) ? 'selected' : '')
                : (answers[current.key] === option ? 'selected' : '')
            }
            onClick={() => handleChange(option)}
          >
            {option}
          </button>
        ))}
      </div>
      <button className="next" onClick={handleNext}>
        {step < questions.length - 1 ? 'Далее →' : 'Сгенерировать план'}
      </button>
    </div>
  );
}
