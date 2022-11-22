export const initChosen = (elem) => {
    elem.chosen({
        no_results_text: 'По вашему запросу ничего не найдено!',
        placeholder_text: 'Выберите значение...',
        disable_search_threshold: 5,
        allow_single_deselect: true,
        search_contains: true,
        width: '100%'
    });

    if (elem.attr('multiple') !== 'multiple') {
        elem.on('change', () => {
            elem.click();
        });
    }

    elem.trigger("chosen:updated");
};