// https://jsonplaceholder.typicode.com/

// https://jsonplaceholder.typicode.com/users
// zipcode만 추출하기

/*
fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        for (let i = 0; i < 10; i++) {
            console.log(users[i].address.zipcode);
        }
    });

fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const { zipcode } = user.address;
            console.log(zipcode);
        });
    });
    
    fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((titles) => {
        titles.forEach((title) => {
            // console.log(title);
            console.log(`userId: ${title.userId} title: ${title.title}`);
        });
    });


fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((comment) => {
            console.log(
                `postId: ${comment.postId} name: ${comment.name} email: ${comment.email}`
            );
        });
    });
    
fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
    albums.forEach((album) => {
        console.log(
            `userId: ${album.userId} id: ${album.id} title: ${album.title}`
            );
        });
    });

fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            console.log(
                `albumId: ${album.albumId} title: ${album.title} url: ${album.url} thumbnailUrl: ${album.thumbnailUrl}`
            );
        });
    });

fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            console.log(
                `userId: ${todo.userId} id: ${todo.id} title: ${todo.title} completed: ${todo.completed}`
            );
        });
    });
*/

fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then((response) => response.json())
    .then((titles) => {
        console.log(titles);
    });

//postId가 1인 사람이 남긴 것만 출력
fetch("https://jsonplaceholder.typicode.com/posts/1/comments")
    .then((response) => response.json())
    .then((titles) => {
        console.log(titles);
    });

fetch("https://jsonplaceholder.typicode.com/comments?postId=1")
    .then((response) => response.json())
    .then((titles) => {
        console.log(titles);
    });

fetch("https://jsonplaceholder.typicode.com/comments?postId=1")
    .then((response) => response.json())
    .then((titles) => {
        console.log(titles);
    });
