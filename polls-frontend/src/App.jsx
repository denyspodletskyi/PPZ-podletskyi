import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [questions, setQuestions] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/questions/')
      .then(res => res.json())
      .then(data => setQuestions(data))
  }, [])

  return (
    <div className="container">
      <h1 className="title">Список питань</h1>
      <div className="question-list">
        {questions.map(question => (
          <div key={question.id} className="question-card">
            <h2>{question.question_text}</h2>
            <p>📅 {new Date(question.pub_date).toLocaleDateString()}</p>
            <ul className="choices-list">
              {question.choices.map(choice => (
                <li key={choice.id} className="choice-item">
                  <span>{choice.choice_text}</span>
                  <span className="votes">🗳 {choice.votes}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App
