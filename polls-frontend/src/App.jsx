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
    <div>
      {questions.map(question => (
        <div key={question.id}>
          <h1>{question.question_text}</h1>
          <p>{question.pub_date}</p>
        </div>
      ))}
    </div>
  )
}

export default App
