

export const imgPrep = (elem = null, imgSrc = "/static/Site/images/nophoto.png", alt = 'Фото не указано') => {
    if (elem !== null) {
        elem.attr('src', imgSrc);
        elem.attr('alt', alt);
    }
};