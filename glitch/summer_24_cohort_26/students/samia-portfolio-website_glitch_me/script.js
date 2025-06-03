// NAVBAR

var ul = document.querySelector('.nav-list ul');
var menuBtn = document.querySelector('.menu-btn i');
var links = document.querySelectorAll('.nav-list .nave');

function menuShow() {
    if (ul.classList.contains('open')) {
        ul.classList.remove('open');
    } else {
        ul.classList.add('open');
    }
}

links.forEach(function (link) {
    link.addEventListener('click', function () {
        if (ul.classList.contains('open')) {
            ul.classList.remove('open');
        }
    });
});

// MUDAR TEMA

var color = "dark";

function mudarTema() {
    document.body.classList.toggle(color);
    
    if (document.body.classList.contains(color)) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
}

function loadPage() {
    const storedTheme = localStorage.getItem('theme');
    
    if (storedTheme === 'dark') {
        document.body.classList.add(color);
    } else {
        document.body.classList.remove(color);
    }
}

loadPage();

// ANIMAÇÃO TECNOLOGIAS

document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll('.tecnologias .item');

    const isInView = (el) => {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    };

    const run = () => {
        items.forEach(item => {
            if (isInView(item)) {
                item.classList.add('in-view');
            } else {
                item.classList.remove('in-view');
            }
        });
    };

    window.addEventListener('load', run);
    window.addEventListener('resize', run);
    window.addEventListener('scroll', run);
});