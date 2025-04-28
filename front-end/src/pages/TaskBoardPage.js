import { useParams } from "react-router-dom";
import { useState } from "react";

export default function TaskBoardPage() {
  const { boardId } = useParams();

  const [columns, setColumns] = useState([
    { id: 1, title: "To Do", tasks: [{ id: 1, name: "Design Homepage" }] },
    { id: 2, title: "In Progress", tasks: [{ id: 2, name: "Build API" }] },
    { id: 3, title: "Done", tasks: [{ id: 3, name: "Setup Project" }] },
  ]);

  const addColumn = () => {
    const newTitle = prompt("Enter column title:");
    if (newTitle) {
      setColumns([...columns, { id: Date.now(), title: newTitle, tasks: [] }]);
    }
  };

  const addTask = (columnId) => {
    const taskName = prompt("Enter task name:");
    if (taskName) {
      setColumns(columns.map(col => {
        if (col.id === columnId) {
          return { ...col, tasks: [...col.tasks, { id: Date.now(), name: taskName }] };
        }
        return col;
      }));
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Board ID: {boardId}</h1>

      <div className="d-flex flex-row overflow-auto">
        {columns.map(col => (
          <div key={col.id} className="card me-3" style={{ minWidth: '250px' }}>
            <div className="card-body">
              <h5 className="card-title">{col.title}</h5>

              {col.tasks.map(task => (
                <div key={task.id} className="alert alert-secondary p-2 mb-2">
                  {task.name}
                </div>
              ))}

              <button 
                className="btn btn-sm btn-primary w-100 mt-2"
                onClick={() => addTask(col.id)}
              >
                + Add Task
              </button>
            </div>
          </div>
        ))}

        <button 
          className="btn btn-success align-self-start"
          onClick={addColumn}
        >
          + Add Column
        </button>
      </div>
    </div>
  );
}
