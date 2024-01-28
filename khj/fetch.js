// https://jsonplaceholder.typicode.com/users
// zipcode만 추출하기
// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((users) => {
//         users.forEach((user) => {
//             const { zipcode } = user.address;
//             test(zipcode);
//         });
//     });

// function test(zipcode) {
//     console.log(zipcode);
// }

// 1. post에서 title 추출
fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            const { title } = post;
            extract(title);
        });
    });

function extract(title) {
    console.log(title);
}

// 2. comments에서 postId가 1인 id가 2인 email 추출
fetch("https://jsonplaceholder.typicode.com/posts/1/comments")
    .then((response) => response.json())
    .then((posts) => {
        // posts[1].email은 이미 하나의 값이기 때문에 비구조화 할당이 필요없음
        const email = posts[1].email;
        extract(email);
    });

function extract(email) {
    console.log(email);
}

// 3. albums에서 id, title 동시 추출
fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            const { id, title } = album;
            extract(id, title);
        });
    });

function extract(id, title) {
    console.log("iD:", id);
    console.log("title:", title);
}

// 4. photos에서 id, title, url 동시 추출
fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => {
        photos.forEach((photo) => {
            const { id, title, url } = photo;
            extract(id, title, url);
        });
    });

function extract(id, title, url) {
    console.log("iD:", id);
    console.log("title:", title);
    console.log("url:", url);
}

// 5. todos에서 title만 추출
fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const { title } = todo;
            extract(title);
        });
    });

function extract(title) {
    console.log(title);
}

// 6. users에서 마지막 user 회사이름만 추출
fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        const companyName = users[0].company.name;
        extract(companyName);
    });

function extract(companyName) {
    console.log(companyName);
}
