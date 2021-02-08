const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
  return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')     //replace & with '-and-'
    .replace(/[\s\W-]+/g, '-')  //reaplce spaces, non word chars and dashes with a single dash
};

titleInput.addEventListener('keyup', (e) => {
  console.log(titleInput.val)
  slugInput.setAttribute('value', slugify(titleInput.value))
});