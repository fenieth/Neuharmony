import React, { useState } from 'react';
import FormPage from './FormPage';
import PlanPage from './PlanPage';
import LoadingPage from './LoadingPage'; 
import './App.css';

function App() {
  const [currentPage, setCurrentPage] = useState('form');
  const [answers, setAnswers] = useState({
    age: '',
    diagnosis: '',
    features: [],
    difficulties: [],
    goals: [],
    time: '',
    piano: ''
  });
  const [plan, setPlan] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (formData) => {
    console.log("Form data submitted: ", formData);
    setAnswers(formData);
    setLoading(true);
    setError('');
    try {
      const response = await fetch('http://localhost:8000/therapy/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log("Backend response: ", data);
      setPlan(data.plan);
      setCurrentPage('plan');
    } catch (err) {
      console.error("Error:", err);
      setError('Ошибка при получении плана. Попробуйте ещё раз.');
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    setCurrentPage('form');
    setPlan('');
    setError('');
  };

  return (
    <div className="app">
      {loading ? (
        <LoadingPage />
      ) : currentPage === 'form' ? (
        <FormPage onSubmit={handleSubmit} initialAnswers={answers} />
      ) : error ? (
        <div className="error-message">
          {error}
          <button onClick={handleBack}>Назад</button>
        </div>
      ) : (
        <PlanPage answers={answers} plan={plan} onBack={handleBack} />
      )}
    </div>
  );
}

export default App;
