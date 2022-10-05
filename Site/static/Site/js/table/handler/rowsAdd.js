export const rowsAdd = (table, dataList = [], reset = true, clear = true) => {
    if (clear) {
        table.clear();
    }

    table.rows.add(dataList);
    table.draw(reset);
};