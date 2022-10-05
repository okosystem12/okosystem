export const removeRowById = (table, id) =>
    table.row(`#${id}`).remove().draw(false);