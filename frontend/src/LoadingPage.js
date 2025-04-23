import React from 'react';

const LoadingPage = () => {
  return (
    <div className="loading-page" style={{ textAlign: 'center', paddingTop: '100px' }}>
      <h2>Генерируем ваш музыкальный план...</h2>
      <div className="spinner" style={{ marginTop: '30px' }}>
        <div className="loading-spinner"></div>
      </div>
    </div>
  );
};

export default LoadingPage;
