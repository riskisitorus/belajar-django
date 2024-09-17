// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let allertWrapper = document.querySelector('.alert')
let allertClose = document.querySelector('.alert__close')

if (allertWrapper) {
  console.log('Alert wrapper clicked');
  allertClose.addEventListener('click', ()=>
    allertWrapper.style.display = 'none'
  )
}