// https://jsonplaceholder.typicode.com/posts
// title 만 추출하기
// fetch("https://jsonplaceholder.typicode.com/posts")
//     .then((response) => response.json())
//     .then((posts) => {
//         // console.log(titles);
//         posts.forEach((title) => {
//             console.log(title.title);
//         });
//     });

// https://jsonplaceholder.typicode.com/comments
// id와 email 추출하기
// fetch("https://jsonplaceholder.typicode.com/comments")
//     .then((response) => response.json())
//     .then((comments) => {
//         comments.forEach((post) => {
//             console.log("id:" + post.id, "email:" + post.email);
//         });
//     });

// https://jsonplaceholder.typicode.com/albums
// userId 만 추출하기
// fetch("https://jsonplaceholder.typicode.com/albums")
//     .then((response) => response.json())
//     .then((albums) => {
//         albums.forEach((post) => {
//             console.log(post.userId);
//         });
//     });

// https://jsonplaceholder.typicode.com/photos
// albumId 와 url 추출하기
// fetch("https://jsonplaceholder.typicode.com/photos")
//     .then((response) => response.json())
//     .then((photos) => {
//         photos.forEach((post) => {
//             console.log(post.albumId, post.url);
//         });
//     });

// https://jsonplaceholder.typicode.com/todos
// completed 추출하기
// fetch("https://jsonplaceholder.typicode.com/todos")
//     .then((response) => response.json())
//     .then((todos) => {
//         todos.forEach((todo) => {
//             console.log(todo.completed);
//         });
//     });

// https://jsonplaceholder.typicode.com/users
// city만 추출하기
// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((users) => {
//         users.forEach((user) => {
//             // const { city } = user.address;
//             // console.log(city);
//         });
//     });

// 1번째  posts 추출
// fetch("https://jsonplaceholder.typicode.com/posts/1")
//     .then((response) => response.json())
//     .then((posts) => {
//         console.log(posts);
//     });

//postId가 1인 사람이 남긴 것만 추출
// fetch("https://jsonplaceholder.typicode.com/posts/1/comments")
//     .then((response) => response.json())
//     .then((posts) => {
//         console.log(posts);
//     });

// fetch("https://jsonplaceholder.typicode.com/comments?postId=1")
//     .then((response) => response.json())
//     .then((titles) => {
//         console.log(titles);
//     });

// fetch("https://jsonplaceholder.typicode.com/comments?postId=1")
//     .then((response) => response.json())
//     .then((titles) => {
//         console.log(titles);
//     });
