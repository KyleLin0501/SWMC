let navItem = document.querySelectorAll('.top-nav');
let active = document.querySelector('.nav-item .nav-link.active');

document.querySelectorAll('.dropdown-btn').forEach(element => {
    element.addEventListener('click', (event) => {
        element.parentElement.nextElementSibling.classList.toggle('show');
    });
});

navItem.forEach(element => {
    if (window.innerWidth >= 992) {
        element.addEventListener('mouseover', (event) => {
            element.querySelector('.dropdown-menu')?.classList.add('show');
            element.querySelector('.nav-link').classList.add('hover');
            active?.classList.remove('active');
        });

        element.addEventListener('mouseout', (event) => {
            element.querySelector('.dropdown-menu')?.classList.remove('show');
            element.querySelector('.nav-link').classList.remove('hover');
            active?.classList.add('active');
        });
    }
});
