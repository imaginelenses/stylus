// Callback hell
userInput((details) => {
    dbCall(details, (password) => {
        passwordAuth(password, (match) => {
            if (match) {
                login()
            }
        })
    })
})

