const button2 = document.querySelector('#dark-mode-button-presist');
const body = document.querySelector('body');
const darkThemeCSS = document.querySelector('#dark-theme-css');
const striped = document.querySelector('.table-striped');
const filterform = document.querySelector('.card.card-body');
const actionButton = document.querySelector('.btn.dropdown-toggle');
const dropdowntheme = document.querySelector('.dropdown-menu');

function toggleDarkTheme() {
  body.classList.toggle('dark-theme');
  filterform.classList.toggle('black-background');
  striped.classList.toggle('table-striped');
  // actionButton.classList.toggle('btn-dark');
  // dropdowntheme.classList.toggle('dropdown-menu-dark');
  localStorage.setItem('darkThemeEnabled',
                       body.classList.contains('dark-theme'));
}

function applySavedTheme() {
  if (localStorage.getItem('darkThemeEnabled') === 'true') {
    body.classList.add('dark-theme');
    filterform.classList.add('black-background');
    striped.classList.remove('table-striped');
    // dropdowntheme.classList.add('dropdown-menu-dark');
    // actionButton.classList.remove('btn-light');
    // actionButton.classList.add('btn-dark');
  } else {
    body.classList.remove('dark-theme');
    filterform.classList.remove('black-background');
    striped.classList.add('table-striped');
    // actionButton.classList.add('btn-light');
    // actionButton.classList.remove('btn-dark');
    // dropdowntheme.classList.remove('dropdown-menu-dark');
  }
}

applySavedTheme();

