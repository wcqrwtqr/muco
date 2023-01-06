const button = document.querySelector('#dark-mode-button');
const body = document.querySelector('body');
const darkThemeCSS = document.querySelector('#dark-theme-css');
const striped = document.querySelector('.table-striped');


button.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
    striped.classList.toggle('table-striped');
    if (body.classList.contains('dark-theme')) {
        document.documentElement.style.setProperty('--bg-color', '#333');
        document.documentElement.style.setProperty('--text-color', '#fff');
        document.documentElement.style.setProperty('--link-color', '#5cacee');
    } else {
        document.documentElement.style.setProperty('--bg-color', '#fff');
        document.documentElement.style.setProperty('--text-color', '#333');
        document.documentElement.style.setProperty('--link-color', '#0000ff');
    }
});
