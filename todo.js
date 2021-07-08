document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#foo').onsubmit = () => {

        const li = document.createElement('li');
        const task = document.querySelector('#task');

        li.innerHTML = task.value;

        task.value = '';

        document.querySelector('.tasks').append(li);

        return false
    };
});