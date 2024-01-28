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

// 6개 추출하기
// post에서 body 추출
fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            console.log(post.title);
        });
    });
