import { useEffect, useState } from "react";
import { Link, useNavigate } from 'react-router-dom'
import {API_URL } from '../../config.jsx'
import './admin_childs.css'

const AdminChilds = () => {
    const [childs, setChild] = useState([]);
    const navigate = useNavigate()
    useEffect(() => {
        fetch(`${API_URL}/child/`, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        })
          .then((res) => res.json())
          .then((data) => {
            setChild(data);
          })
          .catch((err) => {
            console.log(err);
          });
      }, []);
      
    if(childs === null) {
        return <div>Loading...</div>
    }


    return ( 
        <>
            <ul className="admin-child-list">
                {childs.map((child) => (
                    <li key={child.id} className="admin-child-item">
                        <p className="admin-child-id">{child.id}</p>
                        <div className="admin-child-item-content">
                            <Link to={`/admin/child/${child.id}`}>
                                <img src={`${API_URL}/img/${child.img}`} alt={child.name} />
                                <p>{child.FML}</p>
                            </Link>
                        </div>
                    </li>
                ))}
            </ul>
            
        </>
     );
}
 
export default AdminChilds;