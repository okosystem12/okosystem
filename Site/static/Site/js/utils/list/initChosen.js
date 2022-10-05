export const initChosen = (elem) => {
    elem.chosen({
        no_results_text: 'По вашему запросу ничего не найдено!',
        placeholder_text: 'Выберите значение...',
        disable_search_threshold: 10,
        allow_single_deselect: true,
        width: '100%'
    }).on('change', () => {
        elem.click();
    });

    elem.trigger("chosen:updated");
};