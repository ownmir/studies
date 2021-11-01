const domain = 'http://localhost:8000/bboard/';
let list = document.getElementById('list');
let listLoader = new XMLHttpRequest();
listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            // window.alert(data);
            let s = '<ul>', d;
            for (let i = 0; i < data.length; i++) {
                d = data[i];
                // Выводим рядом с названием каждой рубрики ссылку на сведения о рубрике
                // Привязали к каждой ссылке класс detail
                // Записали интернет адреса для загрузки рубрик в тегах a
                s += '<li>' + d.name + ' <a href="' + domain +
                    'api/rubrics/' + d.id +
                    '/" class="detail">Вывести</a></li>';
                // s += '<li>' + d.name + '</li>';
            }
            s += '</ul>';
            list.innerHTML = s;
            // Мы привязали к каждой ссылке обработчик события click
            let links = list.querySelectorAll('ul li a.detail');
            links.forEach((link) =>
            {link.addEventListener('click', rubricLoad);});
        } else
            window.alert(listLoader.statusText);
    }
}) ;
function listLoad() {
    listLoader.open('GET', domain + 'api/rubrics/', true);
    listLoader.send();
}

let id = document.getElementById('id');
let name = document.getElementById('name');
let rubricLoader = new XMLHttpRequest();

rubricLoader.addEventListener('readystatechange', () =>{
    if (rubricLoader.readyState == 4) {
        if (rubricLoader.status == 200) {
            let data = JSON.parse(rubricLoader.responseText);
            id.value = data.id;
            name.value = data.name;
        } else
            window.alert(rubricLoader.statusText);
    }
});

function rubricLoad(evt) {
    evt.preventDefault();
    rubricLoader.open('GET', evt.target.href, true);
    rubricLoader.send();
}
listLoad();