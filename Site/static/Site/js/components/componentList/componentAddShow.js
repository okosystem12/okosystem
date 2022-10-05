export const componentAddShow = (elem = null, show = true) => {
    if (elem !== null) {
        const btn = $(elem).find('.component__add');
        console.log(show);
        if (show) {
            btn.show();
        }
        else {
            btn.hide();
        }
    }
};