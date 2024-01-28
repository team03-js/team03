fetch('https://jsonplaceholder.typicode.com/photos')
    .then((response) => response.json())
    .then((photos) => {
        photos.forEach((photo) => {
            console.log(photo.url);
        });
    });