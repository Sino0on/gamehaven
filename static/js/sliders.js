document.addEventListener("DOMContentLoaded", function () {
    const playBtns = document.querySelectorAll(".play-button");
    const videoReviewSwiperEl = document.querySelector('.video-reviews-slider');
    const slides = videoReviewSwiperEl.querySelectorAll('.swiper-slide');
    const videos = videoReviewSwiperEl.querySelectorAll('video');

    slides.forEach((slide) => {
        const slideEl = slide.querySelector('.swiper-slide-video');

        const img = slide.querySelector(".circle img");
        const circle = slide.querySelector(".circle");





        slide.addEventListener("click", (e) => {
            // const idx = +slide.getAttribute('data-swiper-slide-index');
            // if (!slide.classList.contains('swiper-slide-active')) {
            //     videoReviewSwiperEl.swiper.slideToLoop(idx);
            // }

            slideEl.classList.toggle('active-video-slide');

            const video = slide.querySelector('video')


            if (video.paused) {
                img.src = "{% static './assets/pause-icon.svg' %}";
                video.play(); // Start playing if the video is paused
                circle.classList.add("active");

            } else {
                img.src = "./assets/play-icon.svg";
                video.pause(); // Pause the video if it's already playing
                circle.classList.remove("active");
            }

        })
    })


    const heroSliderStart = new Swiper(".hero-slider_swiper_start", {
        slidesPerView: 2,
        direction: "vertical",
        spaceBetween: 12,
        speed: 1000,
        autoplay: {
            delay: 2000,
            reverseDirection: true,
        },
        loop: true,
    });

    const heroSliderEnd = new Swiper(".hero-slider_swiper_end", {
        slidesPerView: 3,
        direction: "vertical",
        spaceBetween: 12,
        speed: 1000,
        autoplay: {
            delay: 2000,
            reverseDirection: true,

        },
        loop: true,

    })

    const heroSliderCenter = new Swiper(".hero-slider_swiper_center", {
        slidesPerView: 3,
        direction: "vertical",
        spaceBetween: 30,
        centeredSlides: true,
        initialSlide: 1,
        speed: 1000,

        autoplay: {
            delay: 2000
        },
        loop: true,

    })

    const catalogThumb = new Swiper(".catalog-slider_thumbs", {
        slidesPerView: 2.2,
        spaceBetween: 16,
        watchSlidesProgress: true,
        initialSlide: 1,
        navigation: {
            nextEl: ".catalog-button-next",
            prevEl: ".catalog-button-prev",
        },
        breakpoints: {
            768: {
                slidesPerView: 3.2
            },
            1024: {
                slidesPerView: 5.5
            },
            1200: {
                slidesPerView: 7,
                spaceBetween: 0,

            }
        }
    });
    const catalogMain = new Swiper(".catalog-slider_main", {
        spaceBetween: 16,
        initialSlide: 1,
        thumbs: {
            swiper: catalogThumb,
        },
        navigation: {
            nextEl: ".catalog-button-next",
            prevEl: ".catalog-button-prev",
        },
    });

    const advantages = new Swiper(".advantages-slider_swiper", {
        slidesPerView: 1.6,
        spaceBetween: 20,
        navigation: {
            nextEl: ".advantages-button-next",
            prevEl: ".advantages-button-prev",
        },
        breakpoints: {
            768: {
                slidesPerView: 3.2
            },
            1024: {
                slidesPerView: 4.2
            },
            1200:{
                slidesPerView: 5
            }
        }
    })


    const news = new Swiper(".news-slider", {
        slidesPerView: 1,
        initialSlide: 0,
        centeredSlides: true,
        effect: 'cards',
        loop: true,
        cardsEffect: {
            perSlideOffset: 14,
            rotate: 0,
            perSlideRotate: 0,
            slideShadows: false,
        },
        navigation: {
            nextEl: ".news-button-next",
            prevEl: ".news-button-prev",
        },
        breakpoints: {
            768: {
                cardsEffect: {
                    perSlideOffset: 8.5,
                    rotate: 0,
                    perSlideRotate: 0,
                    slideShadows: false,
                }
            }
        }
    })

    const videoReview = new Swiper(".video-reviews-slider", {
        slidesPerView: 2.3,
        spaceBetween: 12,
        initialSlide: 1,
        loop: true,
        navigation: {
            nextEl: ".video-reviews-button-next",
            prevEl: ".video-reviews-button-prev",
        },
        breakpoints: {
            768: {
                slidesPerView: 3.2
            },
            992: {
                slidesPerView: 4,

            },
            1200: {
                slidesPerView: 5
            }
        }
    })

    const imgReview = new Swiper(".img-reviews-slider", {
        slidesPerView: 2.3,
        spaceBetween: 12,
        breakpoints: {
            768: {
                slidesPerView: 3.2
            },
            1200:{
                slidesPerView: 5.5
            }
        }
    })
})