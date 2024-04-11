const playBtns = document.querySelectorAll(".play-button");

playBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        video = btn.nextElementSibling;
        img = btn.querySelector("img");
        circle = btn.querySelector(".circle");

        if (video.paused) {
            img.src = "./assets/pause-icon.svg";
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
    autoplay: {
        delay: 2000
    },
    loop: true,

})

const catalogThumb = new Swiper(".catalog-slider_thumbs", {
    slidesPerView: 2.2,
    spaceBetween: 16,
    loop: true,
    watchSlidesProgress: true,
});
const catalogMain = new Swiper(".catalog-slider_main", {
    spaceBetween: 16,
    loop: true,
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
})


const news = new Swiper(".news-slider", {
    slidesPerView: 1,
    initialSlide: 0,
    centeredSlides: true,
    effect: 'cards',
    loop: false,
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
})

const videoReview = new Swiper(".video-reviews-slider", {
    slidesPerView: 2.3,
    spaceBetween: 12,
    slideToClickedSlide: true,
    loop: true,
    navigation: {
        nextEl: ".video-reviews-button-next",
        prevEl: ".video-reviews-button-prev",
    }
})

const imgReview = new Swiper(".img-reviews-slider", {
    slidesPerView: 2.3,
    spaceBetween: 12,
    autoplay: {
        delay: 3000
    },
    loop: true,
})