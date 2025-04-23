import React, { useState } from 'react';

const FormPage = ({ onSubmit, initialAnswers }) => {
  const [answers, setAnswers] = useState(initialAnswers);
  const [currentQuestion, setCurrentQuestion] = useState(0);

  const questions = [
    {
      id: 'age',
      text: '1. Сколько лет вашему ребёнку?',
      options: ['2–3 года', '4–5 лет', '6–7 лет', '8–9 лет', '10+'],
      type: 'radio'
    },
    {
      id: 'diagnosis',
      text: '2. Подтверждён ли у ребёнка диагноз аутизма?',
      options: ['Да', 'Нет, но есть подозрение', 'Нет'],
      type: 'radio',
      warning: answers.diagnosis === 'Нет' ? 'На данный момент продукт ориентирован на детей с подтверждённым РАС' : null
    },
    {
      id: 'features',
      text: '3. У ребёнка также присутствуют следующие особенности:',
      options: ['Сенсорная чувствительность', 'Нарушения мелкой моторики', 'Проблемы с концентрацией', 'Эмоциональные вспышки / тревожность'],
      type: 'checkbox'
    },
    {
      id: 'difficulties',
      text: '4. Какие основные трудности вы замечаете у ребёнка?',
      options: [
        'Не может долго концентрироваться',
        'Избегает определённых звуков / текстур',
        'Не может удерживать внимание на заданиях',
        'Плохо реагирует на инструкции',
        'Сложности с координацией движений',
        'Часто тревожится, неусидчив',
        'Ему трудно выражать эмоции'
      ],
      type: 'checkbox'
    },
    {
      id: 'goals',
      text: '5. Какие цели вы ставите для занятий?',
      options: [
        'Улучшение сенсорной регуляции',
        'Развитие мелкой моторики и координации',
        'Повышение концентрации внимания',
        'Помочь ребёнку лучше распознавать и выражать эмоции',
        'Расширение музыкального кругозора',
        'Просто удовольствие и отдых'
      ],
      type: 'checkbox'
    },
    {
      id: 'time',
      text: '6. Сколько времени вы готовы уделять музыкальной терапии в неделю?',
      options: ['1 раз в неделю', '2 раза в неделю', '3 раза в неделю', 'Хочу сам(а) определить'],
      type: 'radio'
    },
    {
      id: 'piano',
      text: '7. Есть ли у вас дома фортепиано или синтезатор?',
      options: ['Да', 'Нет, но есть доступ к онлайн-пианино'],
      type: 'radio'
    }
  ];

  const question = questions[currentQuestion];

  const handleChange = (questionId, value) => {
    setAnswers(prev => ({ ...prev, [questionId]: value }));
  };

  const handleMultipleSelect = (questionId, value, isChecked) => {
    setAnswers(prev => {
      const currentValues = prev[questionId] || [];
      return {
        ...prev,
        [questionId]: isChecked
          ? [...currentValues, value]
          : currentValues.filter(item => item !== value)
      };
    });
  };

  const handleNext = () => {
    if (question.type === 'radio' && !answers[question.id]) {
      alert('Пожалуйста, выберите один из вариантов');
      return;
    }

    if (question.type === 'checkbox' && (!answers[question.id] || answers[question.id].length === 0)) {
      alert('Пожалуйста, выберите хотя бы один вариант');
      return;
    }

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    }
  };

  const handlePrev = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();

    if (question.type === 'radio' && !answers[question.id]) {
      alert('Пожалуйста, выберите один из вариантов');
      return;
    }

    if (question.type === 'checkbox' && (!answers[question.id] || answers[question.id].length === 0)) {
      alert('Пожалуйста, выберите хотя бы один вариант');
      return;
    }

    const requiredQuestions = ['age', 'diagnosis', 'time', 'piano'];
    const missingAnswers = requiredQuestions.filter(q => !answers[q]);

    if (missingAnswers.length > 0) {
      alert('Пожалуйста, ответьте на все обязательные вопросы');
      return;
    }

    onSubmit(answers);
  };

  return (
    <div className="form-page">
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <div className="question-block">
            <h2 className="question-text">{question.text}</h2>

            {question.warning && (
              <div className="warning-message">{question.warning}</div>
            )}

            <div className="options-container">
              {question.options.map((option, index) => (
                <div key={index} className="option-item">
                  {question.type === 'radio' ? (
                    <label className="radio-label">
                      <input
                        type="radio"
                        name={question.id}
                        value={option}
                        checked={answers[question.id] === option}
                        onChange={() => handleChange(question.id, option)}
                        required={currentQuestion === 0 && !answers.age}
                      />
                      <span className="radio-custom"></span>
                      {option}
                    </label>
                  ) : (
                    <label className="checkbox-label">
                      <input
                        type="checkbox"
                        value={option}
                        checked={answers[question.id]?.includes(option) || false}
                        onChange={(e) => handleMultipleSelect(question.id, option, e.target.checked)}
                      />
                      <span className="checkbox-custom"></span>
                      {option}
                    </label>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div className="navigation-buttons">
            {currentQuestion > 0 && (
              <button type="button" onClick={handlePrev} className="nav-button prev-button">
                Назад
              </button>
            )}

            {currentQuestion < questions.length - 1 ? (
              <button
                type="button"
                onClick={handleNext}
                className="nav-button next-button"
                disabled={
                  (question.type === 'radio' && !answers[question.id]) ||
                  (question.type === 'checkbox' && (!answers[question.id] || answers[question.id].length === 0))
                }
              >
                Далее
              </button>
            ) : (
              <button
                type="submit"
                className="submit-button"
                disabled={!answers[question.id]}
              >
                Сгенерировать план
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};

export default FormPage;
