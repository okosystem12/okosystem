export const initGallery = (elem = null) => {
    if (elem !== null) {
        elem.uploader({
            gallery: true,
            multiple: true
        });
    }
};