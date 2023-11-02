document.getElementById(username)

async function getdata()  {
    const response = await fetch('http://localhost:8000/api/user',
    {
        method: 'GET',
    }).then(response => {
        if (response.ok) {
          response.json().then(json => {
            console.log(json);
          });
        }
      });

}