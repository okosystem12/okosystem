
export const highlight = (table) => {
    const body = $(table.table().body());

    body.unhighlight();
    if (table.rows({filter: 'applied'}).data().length) {
        body.highlight(table.search());
    }
};