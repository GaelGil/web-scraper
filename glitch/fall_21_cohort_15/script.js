function searchFunction() {
  var input, filter, cardimagetext, i, x;
  input = document.getElementById('myinput');
  filter = input.value.toUpperCase();
  cardimagetext = document.getElementsByClassName('cardImageText');

  for (x = 0; x < cardimagetext.length; x++) {
    i = cardimagetext[x].getElementsByClassName('card-key')[0];
    if (i.innerHTML.toUpperCase().indexOf(filter) > -1) {
      cardimagetext[x].style.display = '';
    }
    else {
      cardimagetext[x].style.display = 'none';
    }
  }
}

