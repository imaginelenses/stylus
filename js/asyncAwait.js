async function randomUser() {
    let response = await fetch('https://randomuser.me/api')
    response = await response.json()

    let results = await response['results']
    let person = await results[0]

    return person.gender
}

randomUser()