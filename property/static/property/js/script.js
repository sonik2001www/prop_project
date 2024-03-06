
const swiper = new Swiper('.swiper-condos', {
    loop: true,
    pagination: {
        el: '.swiper-pagination',
    },
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
    autoplay: {
        delay: 5000,
    },
});

const swiperG = new Swiper('.swiper-gallery', {
    loop: true,
    pagination: {
        el: '.swiper-gallery-pagination',
    },
    autoplay: {
        delay: 5000,
    },
    spaceBetween: 20,
    navigation: {
        nextEl: ".swiper-gallery-button-next",
        prevEl: ".swiper-gallery-button-prev",
    },
});

const swiperP = new Swiper('.swiper-property', {
    autoplay: {
        delay: 5000,
    },
    loop: true,
    breakpoints: {
        320: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        576: {
            slidesPerView: 4,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 6,
            spaceBetween: 20
        },
        992: {
            slidesPerView: 4,
            spaceBetween: 20
        },
        1200: {
            slidesPerView: 6,
            spaceBetween: 20
        }
    }
});

const swiperP2 = new Swiper('.swiper-property-with-img', {
    autoplay: {
        delay: 5000,
    },
    loop: true,
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        576: {
            slidesPerView: 2,
            spaceBetween: 20
        }
    }
});

var swiperM = new Swiper(".mySwiper", {
    loop: true,
    spaceBetween: 20,
    slidesPerView: 4,
    watchSlidesProgress: true,
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        576: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 20
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 20
        }
    }
});
var swiperM2 = new Swiper(".mySwiper2", {
    loop: true,
    spaceBetween: 20,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    thumbs: {
        swiper: swiperM,
    },
    autoplay: {
        delay: 5000,
    },
});

function initMap() {
    var mapOpts = {
        center: { lat: 32.348289, lng: -90.430576 },
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.TERRAIN,
        styles:
            [
                {
                    "featureType": "road.local",
                    "stylers": [
                        {
                            "weight": 4.5
                        }
                    ]
                }
            ]
    };

    var map = new google.maps.Map(document.getElementById('sp-map'), mapOpts);

    var bicyclayer = new google.maps.BicyclingLayer();
    bicyclayer.setMap(map);

    var infowincontent = '<div class="sp-map__inner">CONTENT</div>';

    var marker0 = new google.maps.Marker({
        position: { lat: 32.354902, lng: -90.452267 },
        map: map,
        title: 'Title',
        animation: google.maps.Animation.DROP
    });

    var infowindow0 = new google.maps.InfoWindow({
        content: infowincontent.replace('CONTENT',
            '<img src="img/bg-blog.jpeg">'
        )
    });

    marker0.addListener('click', function () {
        infowindow0.open(map, marker0);
    });

    var marker1 = new google.maps.Marker({
        position: { lat: 32.334517, lng: -90.357348 },
        map: map,
        title: 'Title',
        animation: google.maps.Animation.DROP
    });

    var infowindow1 = new google.maps.InfoWindow({
        content: infowincontent.replace('CONTENT',
            '<img src="img/bg-blog.jpeg">'
        )
    });

    marker1.addListener('click', function () {
        infowindow1.open(map, marker1);
    });
}

/* Initialize the map, set the variable for "lmall" (Lawton Mall), provide the lat-lng (latitude-longitude),
      center on "lmall" and set the zoom level. */



//$(document).ready(function() {
//
//    // required elements
//    var imgPopup = $('.img-popup');
//    var imgCont  = $('.container__img-holder');
//    var popupImage = $('.img-popup img');
//    var closeBtn = $('.close-btn');
//
//    // handle events
//    imgCont.on('click', function() {
//      var img_src = $(this).children('img').attr('src');
//      imgPopup.children('img').attr('src', img_src);
//      imgPopup.addClass('opened');
//    });
//
//    $(imgPopup, closeBtn).on('click', function() {
//      imgPopup.removeClass('opened');
//      imgPopup.children('img').attr('src', '');
//    });
//
//    popupImage.on('click', function(e) {
//      e.stopPropagation();
//    });
//
//});


    document.getElementById('CurrencySwitcher').addEventListener('change', function() {
        var currencySwitcher = document.getElementById('CurrencySwitcher');
        var selectedValue = currencySwitcher.value;

        // Збережіть вибране значення валюти у сесію
        sessionStorage.setItem('currencySwitcher', selectedValue);

        // Створюємо об'єкт FormData та додаємо дані до нього
        var formData = new FormData();
        formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
        formData.append('CurrencySwitcher', selectedValue);

        // Відправляємо дані на сервер за допомогою AJAX-запиту
        var xhr = new XMLHttpRequest();
        xhr.open('POST', window.location.href, true);
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // Встановлюємо заголовок X-CSRFToken

        xhr.onload = function() {
            if (xhr.status === 200) {
                // Оновлюємо сторінку після успішної відповіді
                location.reload();
            }
        };

        xhr.send(formData);
    });


// Функція для отримання значення CSRF-токена з cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



