import React, { useState } from 'react';

const PlanPage = ({ plan, onBack, loading }) => {
  const [question, setQuestion] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const [isChatLoading, setIsChatLoading] = useState(false);

  const handleQuestionSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;
  
    setIsChatLoading(true);

    setChatMessages(prev => [...prev, { sender: 'user', text: question }]);
  
    try {
      const response = await fetch('http://localhost:8000/therapy/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          question: question,
          context: plan
        })
      });
  
      const data = await response.json();
  
      setChatMessages(prev => [
        ...prev,
        {
          sender: 'bot',
          text: data.response || 'Не удалось получить ответ от ИИ.'
        }
      ]);
    } catch (error) {
      setChatMessages(prev => [
        ...prev,
        { sender: 'bot', text: 'Произошла ошибка при обращении к ИИ.' }
      ]);
    } finally {
      setIsChatLoading(false);
      setQuestion('');
    }
  };
  

  return (
    <div className="plan-page">
      <button onClick={onBack} className="back-button">
        ← Вернуться к анкете
      </button>

      <h2>Ваш индивидуальный план музыкальной терапии</h2>

      {loading ? (
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p>Генерируем ваш персональный план...</p>
        </div>
      ) : (
        <div className="plan-content">
          <pre>{plan}</pre>
          
          <div className="chat-container">
            <h3>Задайте вопрос нашему ИИ специалисту</h3>
            
            <div className="chat-messages">
              {chatMessages.map((message, index) => (
                <div 
                  key={index} 
                  className={`message ${message.sender}`}
                >
                  <div className="message-content">
                    {message.text}
                  </div>
                </div>
              ))}
              {isChatLoading && (
                <div className="message bot">
                  <div className="message-content typing">
                    <div className="typing-indicator">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                </div>
              )}
            </div>
            
            <form onSubmit={handleQuestionSubmit} className="chat-input">
              <textarea
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Введите ваш вопрос о плане терапии..."
                rows="3"
                disabled={isChatLoading}
              />
              <button 
                type="submit" 
                disabled={!question.trim() || isChatLoading}
              >
                {isChatLoading ? 'Отправка...' : 'Отправить'}
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default PlanPage;