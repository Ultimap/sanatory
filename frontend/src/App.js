import './App.css';
import AdminChild from './Components/AdminChild/admin_child.jsx';
import AdminChilds from './Components/AdminChilds/admin_childs.jsx';
import AdminHeader from './Components/AdminHeader/admin_header.jsx';
import { Routes, Route } from 'react-router-dom';
import Error from './Components/Error/error.jsx';

function App() {

  return (
    <div className="App">
      <div style={{display: 'flex'}}>
      <AdminHeader />
        <Routes>  
            <Route  path='/error' Component={Error} />
            <Route  path='/admin/child' Component={AdminChilds} />
            <Route  path='/admin/child/:child_id' Component={AdminChild} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
