export const componentData = (elem = null) => {
    if (elem !== null) {
        const componentItemList = $(elem).find('.component__item');
        const componentData = [];
        componentItemList.map(el => {
            const item = $(componentItemList[el]);
            const id = item.attr('data-component-id');
            const value = item.find('.component__input').val().trim();
            componentData.push({
                id: isNaN(id) ? null : id,
                value
            })
        });

        return componentData
    }
};