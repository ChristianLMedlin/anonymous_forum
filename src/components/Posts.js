import React, { useState, useEffect } from 'react';
import "./Posts.css"
 
function Posts() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
    fetch("/api/posts")
    .then(response => response.json())
    .then(data => setPosts(data))
    }, []);

    return (
    <div>
        {posts.map(item => (
            <article key={item.id}>
                <h1>{item.title}</h1>
                <p>{item.user}</p>
                <p>{item.content}</p>
                <p>{item.creation_date}</p>
            </article>
        ))}
    </div>
    );
}
 
export default Posts;