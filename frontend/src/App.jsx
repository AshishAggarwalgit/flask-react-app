import { useState } from 'react'

function App() {
  const [task, setTask] = useState("")
  const [todos, setTodos] = useState([])

  const API_URL = "http://localhost:5000/todos"

  const deleteTodo = async (id) => {
    await fetch(`${API_URL}/${id}`, {
      method: 'DELETE'
    })
    fetchTodos();
  }

  const fetchTodos = async () => {
    const res = await fetch(API_URL);
    const data = await res.json()
    setTodos(data);
  }

  const addTodo = async () => {
    if(!task.trim()) return;

    await fetch(API_URL, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({task})
    })

    setTask("")
    fetchTodos();

  }

  return (
    <>
      <h1>Todo App (React + Flask)</h1> 

      <input
        type="text"
        placeholder='Enter task'
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />

      <button onClick={addTodo}>Add</button>

      <hr/>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.task}
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>

    </>
  )
}

export default App
