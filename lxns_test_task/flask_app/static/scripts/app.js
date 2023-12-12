function openModal (imageNum) {
  var n = 'modalGallery' + imageNum
  document.getElementById(n).style.display = 'block'
}

function closeModal (imageNum) {
  var n = 'modalGallery' + imageNum
  document.getElementById(n).style.display = 'none'
}

var slideIndex = 1
showSlides(slideIndex)

function plusSlides (n, imageNum) {
  showSlides((slideIndex += n), imageNum)
}

function currentSlide (n, imageNum) {
  showSlides((slideIndex = n), imageNum)
}

function showSlides (n, imageNum) {
  var i
  var cn = 'modalSlides' + imageNum
  var dn = 'imgRow' + imageNum
  var slides = document.getElementsByClassName(cn)
  var dots = document.getElementsByClassName(dn)
  var captionText = document.getElementById('caption')
  if (n > slides.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex = slides.length
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none'
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(' active', '')
  }
  slides[slideIndex - 1].style.display = 'block'
  dots[slideIndex - 1].className += ' active'
  captionText.innerHTML = dots[slideIndex - 1].alt
}
