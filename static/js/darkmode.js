const button2 = document.querySelector('#dark-mode-button-presist');
const body = document.querySelector('body');
const darkThemeCSS = document.querySelector('#dark-theme-css');
const striped = document.querySelector('.table-striped');
const filterform = document.querySelector('.card.card-body');
const detailCardBody = document.querySelector('.card-body');
const actionButton = document.querySelector('.btn.dropdown-toggle');
const dropdowntheme = document.querySelector('.dropdown-menu');
const detailCard = document.querySelector('.card-header');
const cardFooter = document.querySelector('.card-footer');
const dailyImg = document.getElementById('daily-img');
// const formFields = document.querySelectorAll('.form-control');

function toggleDarkTheme() {
  body.classList.toggle('dark-theme');
  filterform && filterform.classList.toggle('black-background');
  striped && striped.classList.toggle('table-striped');
  detailCard && detailCard.classList.toggle('bg-dark');
  detailCardBody && detailCardBody.classList.toggle('bg-dark');
  cardFooter && cardFooter.classList.toggle('bg-dark');
  // if (dailyImg != null){
  //   dailyImg.src = "{% static 'images/detail.png' %}";
  // }
  // actionButton.classList.add('btn-dark');
  // dropdowntheme.classList.toggle('dropdown-menu-dark');
  localStorage.setItem('darkThemeEnabled',
                       body.classList.contains('dark-theme'));
}

function applySavedTheme() {
  if (localStorage.getItem('darkThemeEnabled') === 'true') {
    body.classList.add('dark-theme');
    filterform && filterform.classList.add('black-background');
    striped && striped.classList.remove('table-striped');
    detailCard && detailCard.classList.add('bg-dark');
    detailCardBody && detailCardBody.classList.add('bg-dark');
    cardFooter && cardFooter.classList.add('bg-dark');
    // dailyImg.src = "{% static 'images/detailw.png' %}"
    // dropdowntheme.classList.add('dropdown-menu-dark');
    // actionButton.classList.remove('btn-light');
    // actionButton.classList.add('btn-dark');
  } else {
    body.classList.remove('dark-theme');
    filterform && filterform.classList.remove('black-background');
    striped && striped.classList.add('table-striped');
    detailCard && detailCard.classList.remove('bg-dark');
    detailCardBody && detailCardBody.classList.remove('bg-dark');
    cardFooter && cardFooter.classList.remove('bg-dark');
    // dailyImg.src = "{% static 'images/detail.png' %}"
    // actionButton.classList.add('btn-light');
    // actionButton.classList.remove('btn-dark');
    // dropdowntheme.classList.remove('dropdown-menu-dark');
  }
}

applySavedTheme();

