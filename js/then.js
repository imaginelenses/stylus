fetch('https://randomuser.me/api')
    .then((response) => {
        return response.json()
    })
    .then((json) => {
        return json['results'][0]
    })
    .then((person) => {
        console.log(person.gender)
    })
    .catch((e) => {
        console.log(e)
    })