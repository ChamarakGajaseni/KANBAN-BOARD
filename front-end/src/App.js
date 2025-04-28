import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CreateBoardsPage from "./pages/CreateBoardsPage";
import TaskBoardPage from "./pages/TaskBoardPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CreateBoardsPage />} />
        <Route path="/boards/:boardId" element={<TaskBoardPage />} />
      </Routes>
    </Router>
  );
}

export default App;
