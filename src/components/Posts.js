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
        <div className="post-summary-container">
            {posts.map(item => (
                <article className="post-summary" key={item.id}>
                    <h1 className="post-title">{item.title}</h1>
                    <p className="test">{item.author}</p>
                    <p>{item.content}</p>
                    <p>{item.creation_date}</p>
                </article>
            ))}
        </div>
    );
}
 
export default Posts;