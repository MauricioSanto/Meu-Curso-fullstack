/*
function classToggle() {
    var el = document.querySelector('.icon-cards__content');
    el.classList.toggle('step-animation');
  }
  
  document.querySelector('#toggle-animation').addEventListener('click', classToggle);
  */
/*
$('.slider').slick({
    arrows: true,
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    centerMode: true,
    variableWidth: true,
    draggable: false
  });
  
  $('.slider')
    .on('beforeChange', function(event, slick, currentSlide, nextSlide){
      $('.slick-list').addClass('do-transition')
    })
    .on('afterChange', function(){
      $('.slick-list').removeClass('do-transition')
    });
    */
    const carousel = document.querySelector('.carousel');
    const cards = document.querySelectorAll('.card');
    const cardWidth = cards[0].offsetWidth;
    let currentIndex = 0;

    function moveCarousel() {
        currentIndex++;
        if (currentIndex >= cards.length) {
            currentIndex = 0;
        }
        const translateX = -currentIndex * cardWidth;
        carousel.style.transform = `translateX(${translateX}px)`;
    }

    setInterval(moveCarousel, 3000); // Altere o intervalo conforme desejad