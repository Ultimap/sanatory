import './admin_child.css'
import { useEffect, useState } from 'react';
import { useNavigate, useParams, useLocation, Link } from 'react-router-dom';
import { API_URL } from '../../config';
const AdminChild = () => {
    const { child_id } = useParams()
    const [child, setChild] = useState(null);
    const [medcard, setMedcard] = useState(null);
    const [parent, setParent] = useState(null);
    const token = localStorage.getItem('token');
    const [isListVisible, setListVisible] = useState(false);
    const [img, setImg] = useState(null);
    const [title, settitle] = useState(null);
    const [description, setdescription] = useState(null);
    const [unique_key, setunique_key] = useState(null);
    const handleChangeUnique_key = (e) => {
        setunique_key(e.target.value);
    }
    const handleChangeTitle = (e) => {
        settitle(e.target.value)
    }   
    const submitAddMedcard = (e) => {
        e.preventDefault();
        fetch(`${API_URL}/medcard/create`, {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            method: 'POST',
            body: JSON.stringify({
                unique_key: unique_key,
                child_id: child_id,
            })
        })
      .then((res) => res.json())
      .then((data)  =>  {
        console.log(data);
        window.location.reload();
       })
       .catch((err) => {
        console.log(err);
       })
    }
    const handleChangeDescription = (e) => {
        setdescription(e.target.value)
    }
    const submitAddEnties = (e) => {
        e.preventDefault();
        const raw = {
            title: title,
            description: description
        }
        fetch(`${API_URL}/medcard/${child.medcard_id}/add/entries`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            method: 'POST',
            body: JSON.stringify(raw)
        })
          .then(res => res.json())
          .then(data => {
                console.log(data)
                window.location.reload();
            })
            .catch(err => console.log(err))
    }
    const handleChangeImg = (e) => {
        setImg(e.target.files[0]);
        console.log(e.target.files[0]);
    };
    const submitChangeImg = (e) => {
        e.preventDefault();
        if(img != null) {
            const formData = new FormData();
            formData.append('img', img, img.name);
            const headers = new Headers();
            headers.append('Authorization', `Bearer ${token}`);
            fetch(`${API_URL}/child/${child_id}/add/img`, {
                method: 'PUT',
                headers: headers,
                body: formData,
            })
            .then((res) => res.json())
            .then((data) => {
                    console.log(data);
                    window.location.reload();
                })
            .catch((err) => {
                    console.log(err);
                });
        }
    };
    
    const toggleListVisibility = () => {
        setListVisible(!isListVisible);
      };
    useEffect(() => {
        fetch(`${API_URL}/child/${child_id}`, {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            setChild(data);
          })
        .catch((err) => {
            console.log(err);
          });
    }, [])
    if (child === null) {
        return <div>Loading...</div>
    }
    if(child.medcard_id && medcard === null) {
            fetch(`${API_URL}/medcard/${child.medcard_id}`, {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
            })
           .then((res) => res.json())
           .then((data) => {
            setMedcard(data);
           })
           .catch((err) => {
            console.log(err);
           })
        }
    if(child.parent_id && parent === null) {
        fetch(`${API_URL}/parent/${child.parent_id}/`, {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },})
            .then((res) => res.json())
            .then((data) => {
                setParent(data);
            })
            .catch((err) => {
                console.log(err);
            })
    }
    if(parent === null) {
        return <div>Loading...</div>
    }
    return ( 
        <>
            <div className='admin-child-info'>
                <div className='admin-child-img'>
                    <img src={`${API_URL}/img/${child.img}`} alt={child.name} />
                    <form>
                        <input type="file" onChange={handleChangeImg}/>
                        <button className='admin-child-update-img' onClick={submitChangeImg}>Change</button>   
                    </form>
                </div>
                <div className='admin-child-name'>
                    <h1 >{child.FML}</h1>
                    <Link to={`/admin/parent/${parent.id}/`}><p className='admin-child-parent'>Родитель {parent.FML}</p></Link>
                    {medcard !== null && <button className={`admin-child-medcard-button ${isListVisible ? 'show' : ''}`} onClick={toggleListVisibility}>Мед карта: {medcard.medcard.unique_key}
                    {!isListVisible ? '  ⬇️' : '  ⬆️'} </button>}
                    {(
                        <ul className={`admin-child-entries ${isListVisible ? 'show' : ''}`}>
                        {medcard !== null &&

                            medcard.entries.length > 0 ? (
                                medcard.entries.map((entry) => (
                                <li className='admin-child-entries-item' key={entry.id}>
                                    <h3>{entry.title}</h3>
                                    <p>{entry.description}</p>
                                </li>
                                ))
                            ) : (
                                <h3>Нет записей</h3>
                            )}
  
                            
                        </ul>
                    )}
                </div>
                <div className='admin-child-form'>
                    {medcard!== null && 
                        <form onSubmit={submitAddEnties}>
                            <label>Добавить запись в медкарту</label>
                            <input type="text" onChange={handleChangeTitle} />
                            <textarea onChange={handleChangeDescription} />
                            <button className='admin-child-update-form' type='submit'>Добавить</button>
                        </form>
                    }
                    {medcard === null && 
                        <form onSubmit={submitAddMedcard}>
                            <label>Добавить медкарту</label>
                            <input type="text" onChange={handleChangeUnique_key} />
                            <button className='admin-child-update-form' type='submit'>Добавить</button>
                        </form>
                    }
                </div>
            </div>
        </>
     );
}
 
export default AdminChild;