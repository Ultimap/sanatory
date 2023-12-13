import { Link, useLocation, useNavigate } from 'react-router-dom'
import './admin_header.css'
import { useEffect, useState } from 'react';
import { API_URL } from '../../config';
const AdminHeader = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const [isadmin, setIsAdmin] = useState(false);
    useEffect(() => {
        fetch(`${API_URL}/user/is_admin`, {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
        })
        .then((res) => {
            if (res.status !== 200) {
                navigate('/error');
            }
            return res.json();
        })
        .then((data) => setIsAdmin(data.is_admin))
        .catch((error) => {
            // console.error("Error:", error);
        });
    }, []);
    if(isadmin === false) {
        navigate('/error');
    } 
    
    const AdminLogout = () => {
        localStorage.removeItem("token");
        navigate('/')
    }
    

    if(location.pathname.includes('/admin'))
    {

        return ( 
            <div className='admin-header-container'>
                <div className="admin-header">
                    <div className="admin-header-title">
                        <h1>Admin Panel</h1>
                    </div>
                    <div className="admin-header-links">
                        <ul>
                            <Link to="/admin/child">
                                <li className={location.pathname.includes("/admin/child") ? "admin-header-link-active" : ""}>
                                    Child
                                </li>
                            </Link>
                            <Link to="/admin/medcard">
                                <li className={location.pathname.includes("/admin/medcard") ? "admin-header-link-active" : ""}>
                                        Medcard
                                </li>
                            </Link>
                            <Link to="/admin/parent">
                                <li className={location.pathname.includes("/admin/parent") ? "admin-header-link-active" : ""}>
                                        Parent
                                </li>
                            </Link>
                            <Link to="/admin/doctorr">
                                <li className={location.pathname.includes("/admin/doctor") ? "admin-header-link-active" : ""}>
                                        Doctor
                                </li>
                            </Link>
                        </ul>              
                    </div>
                    <div className='admin-logout'>
                        {
                        localStorage.getItem('token') ? (
                            <Link to="/admin/logout" onClick={() => AdminLogout()}>Logout</Link>
                        ) : (
                            <Link to="/admin/login">Login</Link>
                        )}
                        </div> 
                </div>
    
            </div>
         );
    }
}
 
export default AdminHeader;