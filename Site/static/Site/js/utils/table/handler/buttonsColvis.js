export const buttonsColvis = (colList = []) => {
    return {
        extend: 'collection',
        className: 'custom-html-collection',
        text: 'Настройки',
        buttons: colList.length !== 0 ? [
            '<h3>Столбцы</h3>',
            {
                extend: 'colvis',
                collectionLayout: 'fixed columns',
                collectionTitle: 'Отображение столбцов',
                columnText: (dt, idx, title) => (idx + 1) + ': ' + title,
                columns: ':not(.noVis)'
            },
            {
                extend: 'colvisGroup',
                text: 'Показывать все',
                show: ':hidden'
            },
        ] : [],
    }
};