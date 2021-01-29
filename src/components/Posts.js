import React, { useState, useEffect } from 'react';
 
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
            <div key={item.id}>
            <p>{item.user}</p>
            <p>{item.title}</p>
            <p>{item.content}</p>
            <p>{item.creation_date}</p>
            </div>
        ))}
    </div>
  );
}
 
export default Posts;