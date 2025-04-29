import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { boardApi } from '../api';

export default function CreateBoardsPage() {
  // const [CreateBoards, setCreateBoards] = useState([
  //   { id: 1, name: "Project Alpha" },
  //   { id: 2, name: "Marketing Plan" },
  // ]);
  const [taskBoards, setTaskBoards] = useState([]);
  const [newBoardName, setNewBoardName] = useState("");
  const [editBoardName, setEditBoardName] = useState("");
  const [editBoardId, setEditBoardId] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    boardApi.get("/boards/")
    .then(response => setTaskBoards(response.data))
    .catch(error => console.error("Error fetching boards:", error));
  }, []);

  const createBoard = () => {
    if (!newBoardName.trim()) return;

    boardApi.post("/boards/", { name: newBoardName })
      .then(response => {
        setTaskBoards([...taskBoards, response.data]);
        setNewBoardName("");
      })
      .catch(error => console.error("Error creating board:", error));
  };

  const openEditPopup = (board) => {
    setEditBoardId(board.id);
    setEditBoardName(board.name);
  };

  const submitEdit = async () => {
    if (!editBoardName.trim()) return;
    try {
      const response = await boardApi.put(`/boards/${editBoardId}`, { name: editBoardName });
      setTaskBoards(taskBoards.map(board => 
        board.id === editBoardId ? response.data : board
      ));
      setEditBoardId(null);
      setEditBoardName("");
    } catch (error) {
      console.error("Error updating board:", error);
    }
  };

  const cancelEdit = () => {
    setEditBoardId(null);
    setEditBoardName("");
  };

  const deleteBoard = (id) => {
    boardApi.delete(`/boards/${id}`)
      .then(() => {
        setTaskBoards(taskBoards.filter(board => board.id !== id));
      })
      .catch(error => console.error("Error deleting board:", error));
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
        {taskBoards.map(board => (
          <div 
            key={board.id} 
            className="col-md-4 mb-3"
          >
            <div 
              className="card h-100" 
              style={{ cursor: 'pointer' }}
            >
              <div className="card-body d-flex flex-column">
                <h5 
                  className="card-title"
                  onClick={() => navigate(`/boards/${board.id}`)}
                >
                  {board.name}
                </h5>

                <div className="mt-auto d-flex justify-content-between">
                  <button 
                    className="btn btn-sm btn-warning"
                    onClick={() => openEditPopup(board)}
                  >
                    Edit
                  </button>
                  <button 
                    className="btn btn-sm btn-danger"
                    onClick={() => deleteBoard(board.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Edit Popup Modal */}
      {editBoardId && (
        <div 
          className="modal d-block"
          style={{
            backgroundColor: "rgba(0,0,0,0.5)"
          }}
        >
          <div className="modal-dialog">
            <div className="modal-content">

              <div className="modal-header">
                <h5 className="modal-title">Edit Board</h5>
                <button type="button" className="btn-close" onClick={cancelEdit}></button>
              </div>

              <div className="modal-body">
                <input
                  type="text"
                  className="form-control"
                  value={editBoardName}
                  onChange={(e) => setEditBoardName(e.target.value)}
                />
              </div>

              <div className="modal-footer">
                <button className="btn btn-secondary" onClick={cancelEdit}>Cancel</button>
                <button className="btn btn-primary" onClick={submitEdit}>Save Changes</button>
              </div>

            </div>
          </div>
        </div>
      )}
    </div>

    
  );
}
