fetch('https://randomuser.me/api')
    .then((response) => {
        return response.json()
    })
    .then((json) => {
        return json['result']
    })
    .then((x) => {
        console.log(x)
    })