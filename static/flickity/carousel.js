var element = document.querySelector('.main-carousel');
var flkty = new Flickity( element, {
  // options
  cellAlign: 'center',
  contain: true,
  wrapAround: true,
  autoPlay: 2000,
  groupCell: true
});