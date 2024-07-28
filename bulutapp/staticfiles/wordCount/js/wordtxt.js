let inputTextArea = document.getElementById("input-textarea");

let characCount = document.getElementById("character-count");

let wordCount = document.getElementById("word-count");

inputTextArea.addEventListener("input", () => {
    fetch('/count/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: 'text=' + encodeURIComponent(inputTextArea.value)
    })
    .then(response => response.json())
    .then(data => {
        characCount.textContent = data.char_count;
        wordCount.textContent = data.word_count;
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
