import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function CreateBoardsPage() {
  const [CreateBoards, setCreateBoards] = useState([
    { id: 1, name: "Project Alpha" },
    { id: 2, name: "Marketing Plan" },
  ]);

  const [newBoardName, setNewBoardName] = useState("");
  const navigate = useNavigate();

  const createBoard = () => {
    if (!newBoardName.trim()) return;
    const newBoard = {
      id: Date.now(),
      name: newBoardName,
    };
    setCreateBoards([...CreateBoards, newBoard]);
    setNewBoardName("");
  };

  const deleteBoard = (id) => {
    setCreateBoards(CreateBoards.filter(board => board.id !== id));
  };

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Task Boards</h1>

      <div className="input-group mb-4">
        <input 
          type="text" 
          className="form-control" 
          placeholder="New Board Name" 
          value={newBoardName} 
          onChange={(e) => setNewBoardName(e.target.value)}
        />
        <button className="btn btn-primary" onClick={createBoard}>
          Create Board
        </button>
      </div>

      <div className="row">
        {CreateBoards.map(board => (
          <div 
            key={board.id} 
            className="col-md-4 mb-3"
          >
            <div 
              className="card h-100" 
              onClick={() => navigate(`/boards/${board.id}`)} 
              style={{ cursor: 'pointer' }}
            >
              <div className="card-body d-flex justify-content-between align-items-center">
                <h5 className="card-title">{board.name}</h5>
                <button 
                  className="btn btn-sm btn-danger"
                  onClick={(e) => { e.stopPropagation(); deleteBoard(board.id); }}
                >
                  X
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
